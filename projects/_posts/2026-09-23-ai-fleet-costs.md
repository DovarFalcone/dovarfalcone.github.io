---
layout: post
title: My AI Fleet Cost $24.68 in Eight Weeks — Then I Starved It to Cents
subtitle: Measured spend from 927 agent sessions — where the money actually went, why the boring tasks now cost nothing, and the routing that got it there
category: Project
tags: [AI, Agents, Cost Optimization, Self-Hosting, Ollama, n8n, Homelab]
comments: true
thumbnail-img: /projects/assets/images/ai-cost-01-weekly-spend.png
---

# My AI Fleet Cost $24.68 in Eight Weeks — Then I Starved It to Cents

> **Update, 10 October 2026.** The rest of this post is a snapshot of the eight weeks to 23 September, and its numbers stand as measured then. Two things were wrong or have changed since. First, a correction: the spend log I used could not see calls that went through my model router, so it missed a paid DeepSeek lane that was already billing about $2.40 to $2.50 a week. Second, a change: call volume went up by an order of magnitude and spend did not stay near zero. The section [What happened next: 23 September to 10 October](#what-happened-next-23-september-to-10-october) has the new numbers. The setup paragraphs below are marked where they describe the September layout.

Every model call my agent stack makes is logged locally with its token counts and an estimated cost. That means I don't have to guess what running a fleet of AI agents costs — I can just ask.

Across **eight weeks** (late July to late September) that log holds **927 model calls** across **418 sessions**. The total: **$24.68** in estimated spend. The more useful number is how it moved: from **$12.71 in the worst week** to **$0.16 in the most recent one**, with the share of sessions served entirely by free tiers climbing from 53 % to 96 %.

Here's what the bill looked like, and why most of it was avoidable.

## The eight-week arc

![Metered spend per week, against the share of sessions served by free tiers](/projects/assets/images/ai-cost-01-weekly-spend.png){: .mx-auto.d-block :}

*Blue bars are metered spend; the yellow line is the share of sessions served entirely by free tiers. The first week runs 100 % free; the mid-August spike is the stretch where the paid fallback models picked up real traffic.*

## The setup: a router, some free tiers, and one small local model

*This section and its diagram describe the September layout. What runs today is in the update section below.*

My agents don't talk to providers directly. Everything goes through a local model router (9router) that exposes a combo called **FREE** — **30 models** at the time, across the Gemini free tier, NVIDIA's NIM free endpoints, OpenRouter's `:free` models, OpenCode's free lane, and my own Ollama instance on the RTX 3080. The combo is regenerated **twice a week** by a scheduled job that re-discovers what's actually free, ranks it best-to-worst, and sets the strategy to *fallback* — try the best, drop to the next on failure.

One paid lane stays available as a quality floor: **`deepseek-v4-flash`**. It's my day-to-day default model, and it shows up in this log two ways — routed through the free combo at no cost, and billed directly for 176 calls ($4.60, almost all of it before the free lane was doing the work).

![The routing map: a local router, free tiers, and one tiny local model](/projects/assets/images/ai-cost-05-architecture.png){: .mx-auto.d-block :}

*September layout: nothing in this diagram touches a paid endpoint except one fallback lane. The email classifier never leaves the house. The first half of that sentence stopped being true in October; see the update below.*

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

## What happened next: 23 September to 10 October

The log in the first half of this post stops on 23 September. The next 17 days did not continue the story of falling spend. Same caveat as before: every figure is an estimate from per-token prices, not an invoice.

### The volume changed first

The "927 model calls" in the opening were rows in the usage log (one row per session, model and billing provider), not requests. Counted as requests, the main Hermes log held about 15,400 through 23 September, and my router had logged 6,015.

Then the bot fleet and its task board went live. From 24 September to 10 October the router alone logged **16,627 requests**, and the six Hermes agent profiles together logged about 17,000. The week starting 5 October reached 9,802 router requests in six days, against 1,519 in the week starting 7 September. The coding agent is the heaviest user: 9,356 logged requests in its own profile since 24 September.

### The log was missing a ledger

Hermes records any call that goes through the router at $0, because it cannot price the endpoint behind it. The router keeps its own request history with a list-rate cost per call. Put the two side by side and the "starved it to cents" story changes:

| Week starting | Router requests | Billed directly (Hermes log) | Billed through the router (DeepSeek, OpenRouter) | Total |
|---|---|---|---|---|
| 7 Sep | 1,519 | $1.27 | $2.49 | $3.77 |
| 14 Sep | 2,463 | $1.45 | $2.37 | $3.83 |
| 21 Sep | 2,148 | $0.42 | $2.42 | $2.85 |
| 28 Sep | 5,918 | $0.03 | $3.70 | $3.74 |
| 5 Oct (to 10 Oct) | 9,802 | $0.75 | $2.18 | $2.93 |

*Totals are summed before rounding, so a row can differ from its parts by a cent. The router's log for 10 October ends in the morning.*

![Metered spend per week across both ledgers, with weekly router requests](/projects/assets/images/ai-cost-06-weekly-both-ledgers.png){: .mx-auto.d-block :}

*Blue is spend billed directly, as in the first chart; red is DeepSeek and OpenRouter billed through the router. The yellow line is router requests per week.*

Up to the original cut-off on 23 September, the router had logged $6.42 of DeepSeek billing that the $24.68 total never included. The "$0.16 in the latest week" headline was true of what that log could see. It was not true of the bill.

### Why it went back up: an ordered combo

The primary combo for my bots is a list in order, not a round-robin. It tries a flat-rate subscription first, then DeepSeek's own metered API, then a free lane. Whenever the flat lane declined a request, the next hop billed. From 24 September to 10 October the router served its 16,627 requests like this:

| Lane | Requests | Share | List-rate value |
|---|---|---|---|
| OpenCode Go (flat plan) | 8,595 | 51.7 % | $13.48, not incremental cash |
| DeepSeek direct (metered) | 4,527 | 27.2 % | $5.75 |
| Free lanes (Kilo Code, Gemini free tier, NVIDIA, local Ollama) | 2,978 | 17.9 % | $0 |
| OpenRouter (prepaid credit, metered) | 526 | 3.2 % | $1.01 |
| Claude | 1 | 0.0 % | $0 |

The peak was 4 October (UTC days): 2,060 DeepSeek requests that day, $2.54 at list rate. Note the unit change. "96 % of sessions on free tiers" in the opening counted sessions in a log that priced router calls at zero; the share of *requests* served by free lanes was 17.9 %.

### Subscriptions are outside the metered log

Since 7 October my Orchestrator, the agent I talk to directly, ran on a Claude plan. Hermes prices those rows at API rates, which comes to about $32 since 24 September, all of it from 7 to 10 October. That is a value estimate, not cash: the plan is flat. My provider notes record OpenCode Go at $10 a month; I have no price on file for the Claude plan, so I will not quote one. From 2026-10-10 the Orchestrator runs on DeepSeek Flash through the local router, and the Claude plan is now used mainly by Claude Code and fallbacks.

So metered spend is no longer the whole bill. My stated goal is to pay for two things only, Claude Pro and OpenCode Go, with metered overflow as close to zero as I can get it. That goal is a design target, not a result.

### What I changed

On 8 and 9 October:

- **The coding agent now runs on a paid-only combo.** It tries two OpenCode Go models first and DeepSeek direct last, so its heavy runs stop spilling into whichever free model is up.
- **The bots' combo was reordered** to spend a prepaid OpenRouter credit first, and a dead model id that had been breaking scheduled jobs was replaced.
- **Three token-heavy scheduled jobs are gone.** An incident-triage loop cost about 1.48 million tokens per run. A nightly session-log wrap-up used about 3.9 million tokens a night. A duplicate infrastructure check-in was paused. Two maintenance jobs became plain scripts with no model, and a daily research digest nobody read was removed.
- **OpenCode Go's weekly cap ran out** early on 8 October. A new hourly budget watch, itself a script with no model, now messages me when a prepaid balance runs low or a plan is capped.
- **The coding agent's context-compression threshold went from 100k to 50k tokens**, because its roughly 115k-token requests were what drained the weekly cap.
- **Session titles moved to the local model.**

I can't yet credit these changes with a result. DeepSeek-direct requests peaked at 2,060 on 4 October and 970 on 5 October, then were already at zero on 6 and 7 October, before any of this. Since the changes, estimated router spend was $0.25 on 8 October, $0.05 on 9 October, and $0.80 on 10 October, when 135 DeepSeek-direct requests came back and the rest was OpenRouter credit. Router traffic itself was also far lower on those days, so three days of small numbers is not a trend.

### What still holds

- **The email classifier is unchanged**: `gemma4:e4b` locally, every 30 minutes, capped at 16 output tokens.
- **The cache-read shape holds**: 15.6× the fresh input since 24 September, against 16.3× before.
- **The `FREE` combo is still regenerated twice a week** (Monday and Thursday), now 25 models, ordered by stability and quality tier before speed. It is a late fallback, not the front door.

### The setup today

- The **Orchestrator** runs on a Claude plan (as of 23 September; DeepSeek Flash since 2026-10-10).
- The **bots** use the ordered `DEEPSEEK-FLASH` combo: prepaid credit, then OpenCode Go, then a free lane, then DeepSeek direct.
- The **coding agent** uses a paid-only combo of OpenCode Go and DeepSeek.
- **`FREE`** is a late fallback, and local Ollama still handles email classification and session titles.

## What I'd tell anyone doing this

- **Meter every ledger.** A log that records router calls at $0 reads "free" by omission. I found out by comparing it with the router's own history.
- **Meter first.** I couldn't have fixed the bill without per-call attribution: model, provider, task, tokens, cost. Most of my assumptions about where the money went were wrong — I would have blamed long chat sessions, not the fallback chain.
- **Audit your fallback chain like it's spending your money, because it is.** The expensive model is usually the one you forgot was in the list, and in an ordered chain the paid hop bills every time the cheap hop says no.
- **Free tiers and small local models are for the *frequent and boring*, not the *hard*.** Titles, approvals, tagging, classification. Keep one paid lane for the work where quality changes the outcome.
- **Prefer local for anything private.** The email pipeline costs nothing and shares nothing.

Eight weeks in, metered spend *in that log* was down **98.7 %** from its peak, and each of the last four weeks of the period came in under $1.50 there. The router ledger above shows that was only part of the picture.

---

*Numbers in this post come from my own instrumented usage log — 927 calls, each attributed to a model, a billing provider and a task, with cost estimated from published per-token prices. Providers don't return per-call actuals, so treat the figures as careful estimates rather than invoices.*

*The update's numbers come from the Hermes usage logs of all six agent profiles plus the router's own request history, from 24 September to the morning of 10 October. Router costs are list rates; flat-plan providers show a non-zero list cost that is not incremental cash. I treated the Hermes direct-billed rows and the router's DeepSeek and OpenRouter rows as separate calls, which I could not verify call by call.*
