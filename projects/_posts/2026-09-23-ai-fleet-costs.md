---
layout: post
title: My AI Fleet Cost $24.68 in Eight Weeks — Then I Starved It to Cents 🧾
subtitle: Measured spend from 927 agent sessions — where the money actually went, why the boring tasks now cost nothing, and the routing that got it there
category: Project
tags: [AI, Agents, Cost Optimization, Self-Hosting, Ollama, n8n, Homelab]
comments: true
thumbnail-img: /projects/assets/images/ai-cost-01-weekly-spend.png
---

# My AI Fleet Cost $24.68 in Eight Weeks — Then I Starved It to Cents

Every model call my agent stack makes is logged locally with its token counts and an estimated cost. That means I don't have to guess what running a fleet of AI agents costs — I can just ask.

Across **eight weeks** (late July to late September) that log holds **927 model calls** across **418 sessions**. The total: **$24.68** in estimated spend. The more useful number is how it moved: from **$12.71 in the worst week** to **$0.16 in the most recent one**, with the share of sessions served entirely by free tiers climbing from 53 % to 96 %.

Here's what the bill looked like, and why most of it was avoidable.

## The eight-week arc

![Metered spend per week, against the share of sessions served by free tiers](/projects/assets/images/ai-cost-01-weekly-spend.png){: .mx-auto.d-block :}

*Blue bars are metered spend; the yellow line is the share of sessions served entirely by free tiers. The first week runs 100 % free; the mid-August spike is the stretch where the paid fallback models picked up real traffic.*

## The setup: a router, some free tiers, and one small local model

My agents don't talk to providers directly. Everything goes through a local model router (9router) that exposes a combo called **FREE** — currently **30 models** across the Gemini free tier, NVIDIA's NIM free endpoints, OpenRouter's `:free` models, OpenCode's free lane, and my own Ollama instance on the RTX 3080. The combo is regenerated **twice a week** by a scheduled job that re-discovers what's actually free, ranks it best-to-worst, and sets the strategy to *fallback* — try the best, drop to the next on failure.

One paid lane stays available as a quality floor: **`deepseek-v4-flash`**. It's my day-to-day default model, and it shows up in this log two ways — routed through the free combo at no cost, and billed directly for 176 calls ($4.60, almost all of it before the free lane was doing the work).

![The routing map: a local router, free tiers, and one tiny local model](/projects/assets/images/ai-cost-05-architecture.png){: .mx-auto.d-block :}

*Nothing in this diagram touches a paid endpoint except one fallback lane. The email classifier never leaves the house.*

## Where the money went

Since every call is attributed to a model and a billing provider, the peak weeks are easy to explain.

![Where the $24.68 went](/projects/assets/images/ai-cost-02-where-money-went.png){: .mx-auto.d-block :}

Two things jump out:

- **`gpt-5.6-luna` cost $12.86 — more than half the entire bill.** It was configured as a fallback model and quietly became a primary one: 163 calls, most of them during a stretch in mid-August where sessions kept landing on it.
- **A single call to `claude-fable-5` cost $3.30.** Two calls to `gpt-5.6-terra` cost $1.58. These aren't workhorse sessions — they're the moments a fallback chain reached for something expensive because the cheap option had rate-limited.

Meanwhile the model that does the day-to-day work, `deepseek-v4-flash`, handled **176 calls for $4.60** — most of it before the free lane was in place.

The lesson from the first two charts is that **fallback chains are where money evaporates**. You set up a list of options, you think of the last one as a safety net, and then one day you notice it's been quietly serving a third of your traffic at 20× the price.

## Weirdly, the boring tasks are now nearly free

This is my favourite chart, because it's the one I couldn't have predicted.

![Metered cost by task, with free-tier share](/projects/assets/images/ai-cost-03-by-task.png){: .mx-auto.d-block :}

My agent stack does a lot of *bookkeeping* work that isn't the thing I'm asking it to do: approving tool calls, generating session titles, compressing context when a conversation gets long, and running background reviews over its own output. That's **423 calls** — nearly half the log.

Almost all of it now costs nothing:

| Task | Calls | Served free | Metered cost |
|---|---|---|---|
| Title generation | 117 | 117 (100 %) | $0.006 |
| Approval | 201 | 200 (99.5 %) | $0.08 |
| Compression | 28 | 22 (79 %) | $0.15 |
| Background review | 77 | 49 (64 %) | $2.18 |
| Chat / agent work | 504 | 311 (62 %) | $22.26 |

Titles are free. Approvals are free. Compression is nearly free. These are small, high-frequency, low-stakes decisions — exactly the workload a free tier or a 4-billion-parameter model handles fine.

The outlier is **background review**: 64 % free, but still $2.18 — because a review pass re-reads a large amount of context (6.4 M input tokens across 77 calls), so when it *does* land on a paid model it's the most expensive thing in the log per call. It's also the task where a weaker model is most likely to hurt, which is why it stays partly on the paid lane for now. It's my next optimization, and I'm in no hurry.

## The shape of the traffic

![Token mix across eight weeks](/projects/assets/images/ai-cost-04-token-mix.png){: .mx-auto.d-block :}

Across eight weeks the fleet moved about **1.8 billion tokens** — but look at the shape. Only 100 M of that was fresh input, 10 M was output, and **1.67 billion was cache reads**: 16.6× the size of the input.

That's what an agent loop actually looks like. Every turn re-reads the conversation and the tool results, so the same tokens pass through the model over and over. It's also why "price per million tokens" is a bad proxy for what a model will cost you: prompt caching can make real traffic an order of magnitude cheaper than the sticker price, and the cache-read line is the one to watch.

## The email pipeline: local, strict, and free

The other half of keeping the bill down is refusing to use an API for work that a small local model can do.

My mail gets sorted by an **n8n** workflow that runs every 30 minutes: it pulls recent unlabelled threads from Gmail, strips the email down to readable text (killing tracking URLs, base64 blobs, `cid:` references and image tags), asks a local model to pick one category, then applies the matching Gmail label.

The classifier is **`gemma4:e4b` running locally on the RTX 3080**. Classification is a narrow, repeated, low-stakes decision, so:

- **temperature 0**, `format: json`, and a hard cap of **16 output tokens** — it can only answer with `{"category": 6}`;
- the model is told the email is **untrusted data** and must not follow instructions inside it;
- a Code node **validates** the reply — strict JSON parse, must be an integer, must be inside the label range — and fails closed if it isn't;
- obvious cases stay deterministic, and the category precedence (banking beats receipts, security messages are accounts, uncertainty goes to spam review) is written out explicitly rather than left to the model.

The result: **every email classification costs $0**, the mail content never leaves the machine, and the workflow is boring in the best way. It also taught me a lesson worth repeating — the reliable shape for this kind of task is a *chain* that returns raw model text, not an "agent" node with its own internal output parser. The parser is what fails first, and when it does the failure looks like a broken workflow rather than a bad prompt.

## What I'd tell anyone doing this

- **Meter first.** I couldn't have fixed the bill without per-call attribution: model, provider, task, tokens, cost. Most of my assumptions about where the money went were wrong — I would have blamed long chat sessions, not the fallback chain.
- **Audit your fallback chain like it's spending your money, because it is.** The expensive model is usually the one you forgot was in the list.
- **Free tiers and small local models are for the *frequent and boring*, not the *hard*.** Titles, approvals, tagging, classification. Keep one paid lane for the work where quality changes the outcome.
- **Prefer local for anything private.** The email pipeline costs nothing and shares nothing.

Eight weeks in, metered spend is down **98.7 %** from its peak, and every week since mid-August has come in under $1.50. The remaining bill is mostly ordinary conversation — which is exactly where I want the paid quality to go.

---

*Numbers in this post come from my own instrumented usage log — 927 calls, each attributed to a model, a billing provider and a task, with cost estimated from published per-token prices. Providers don't return per-call actuals, so treat the figures as careful estimates rather than invoices.*
