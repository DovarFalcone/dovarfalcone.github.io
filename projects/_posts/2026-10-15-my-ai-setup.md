---
layout: post
title: My AI Setup
subtitle: Five agents, one task board, two memory stores, and a router deciding who gets paid
category: Project
tags: [AI, Agents, Hermes, Ollama, Memory, Homelab]
comments: true
thumbnail-img: /projects/assets/images/agent-fleet-hierarchy.png
redirect_from:
  - /2026-07-29-hermes-ai-lab/
  - /2026-10-06-agent-fleet-kanban/
  - /2026-10-06-agent-memory-two-stores/
  - /2026-10-06-2026-10-06-agent-memory-two-stores/
---

In July I set out to build an AI lab that ran entirely on my own workstation, on local models and free tiers. I wanted four things: privacy, no network latency, control of the whole stack down to the model weights, and no subscriptions.

Most of that didn't survive contact with real work. A model that fits on a 10 GB graphics card is fine for sorting and titling things, but not for long coding sessions. With the full 256K context loaded it ran at about 19 tokens per second. Free models rate-limit, disappear, and vary in quality. So the setup is now a hybrid. I pay for Claude Pro and OpenCode Go, keep small prepaid balances with a couple of API providers, and most of the real work goes to cloud models. My notes, memory, and agent state still live on my machine, and I still own everything except the weights.

This post covers what runs today. What it costs is in [a separate post](/2026-10-16-what-my-ai-setup-costs/).

## The Hardware and Local Models

Everything runs on one Arch Linux workstation with an NVIDIA RTX 3080 (10 GB). I picked a rolling-release distribution for the newest kernel and driver support.

Ollama runs in a container. I use `gemma4:12b-256k` as the main local model, `qwen3:8b` for cheap background jobs, and a small embedding model for search. Local is now the last fallback, not the first choice.

## The Model Router

None of my agents call a provider directly. They go through 9router, a small router in a container on the same machine. It serves named combos, and each combo is an ordered list. The router tries the first entry and moves to the next only when one fails or hits a cap.

- `DEEPSEEK-FLASH` is the default for most agents: prepaid OpenRouter credit first, then the OpenCode Go plan, then a free lane, then DeepSeek's own API.
- `PI-CODER` is for the coding agent. Every entry is paid, because the free endpoints I tried log prompts and my repositories are private.
- `FREE` is 25 free models ranked best to worst. A scheduled job rebuilds it every Monday and Thursday.

Behind the router, each agent has its own fallback chain that ends with the local Gemma model on my GPU.

The order of a combo decides what bills. Whatever sits first takes the traffic, and a paid entry after a flaky free one bills every time the free one says no. That cost me real money before I caught it.

## The Agent Fleet

The agents run on Hermes Agent. In Hermes a bot is a profile: a directory with its own config, its own SOUL file (personality and operating rules), its own tools, its own scheduled jobs, and its own state. There is one binary, and talking to a specific bot is a flag:

```bash
# Ask the infrastructure bot for the array status
hermes -p kaladin chat -q "What's the Unraid array status?"

# Ask the research bot for a cited answer
hermes -p jasnah chat -q "Research this topic and give me a cited summary"

# List every profile on the machine
hermes profile list
```

That makes a new specialist cheap. It's a new profile, not new infrastructure. The names come from the Stormlight Archive.

| Bot | Profile | Domain | What it owns |
|---|---|---|---|
| Orchestrator | `default` | Coordination | Triage, splitting work into cards, routing, review, and the final gate on risky changes |
| Navani | `coder` | Engineering | Plans, implements, and verifies code changes; hard cases go to Claude |
| Kaladin | `kaladin` | Infrastructure | Unraid array health, disk temperatures, parity, Docker, the Pi sensor |
| Shallan | `shallan` | Knowledge base | The Obsidian vault, note links, and the search index |
| Jasnah | `jasnah` | Research | RSS and market-data lookups with cited answers, on demand only |

![The fleet: Claude Code and chat reach the Orchestrator, which fans cards out over the board to Navani, Kaladin, Shallan and Jasnah. Navani consults Claude only for hard cases.](/projects/assets/images/agent-fleet-hierarchy.png){: .mx-auto.d-block :}

The Orchestrator runs on DeepSeek Flash through the router. I talk to it directly in chat, but most days my front door is Claude Code, which sends quick questions to the Orchestrator and anything bigger to the board.

Every specialist has a shell and file access. An agent that fetches feeds, runs scripts, and edits files can't do its job without one. What differs is the integrations. Kaladin has Unraid and never touches the vault. Shallan has the vault and nothing that reaches the server. Jasnah has neither. Navani gets the full engineering set, including a browser and delegation. So the shell isn't what keeps a bot in its lane. The narrow domain, one assignee per card, and the review step do that.

Only the Orchestrator runs a chat gateway. Every profile was cloned from the same base and carries a copy of the same bot token, so a second gateway would mean two processes answering as the same bot.

## The Kanban Board

Work moves between agents on a Kanban board, and every move is a recorded state change.

1. A card lands in backlog or triage.
2. The Orchestrator reads it and splits it into child cards, each with one assignee.
3. The dispatcher starts `hermes -p <assignee>` for each child card.
4. The worker does the work and reports back with evidence.
5. The worker hands the card to review, which runs on the Orchestrator with a review rubric.
6. Review approves it or sends it back with specific changes.

Most engineering work takes a light path: one card, one implementation pass, one review. The full chain with several child cards is only for risky changes, like a production migration, a scraper or ingest change, auth or secrets, or deploy plumbing.

Two rules matter most. The worker never reviews its own work, so "deployed and verified" is a claim until review checks it against the real output. And a worker can't unblock itself. If it hits a missing credential or a decision only I should make, it blocks the card with a reason and stops. Only the Orchestrator can clear a block, so a blocked card always means something real. A card that keeps getting blocked for the same reason escalates instead of looping.

Not everything goes on the board. A lookup, a status check, or a small edit stays in chat. Anything that touches a repo, runs a build, crawls the web, or will take longer than a few moments becomes a card. The board is a database driven from the command line, so it's scriptable and I can audit every state change after the fact.

## Memory

Without memory, every session starts from zero, and the agent that spent an hour learning my backup rotation asks me about it the next morning. I keep two stores and one rule for choosing between them.

![Memory layer map: Hermes, OpenCode and Claude Code all reach the same SQLite memory and the same Obsidian vault over MCP](/projects/assets/images/memory-01-layer-map.png){: .mx-auto.d-block :}

**Mnemosyne** is a local SQLite database the agents write to. It holds short facts, preferences, corrections, and compressed summaries of past sessions. When I wrote this up on October 6 it held 1,324 working memories, 332 episodic summaries, 456 facts, 124 standing instructions, 59 preferences, and 3 permanent persona rules.

**The vault** is an Obsidian vault of 153 Markdown notes in a PARA layout (Projects, Areas, Resources, Archives). I own it, and it's committed to git every hour. Design decisions, project notes, and plans live here.

The rule: a one- or two-line fact goes to memory, and a paragraph, a decision, or a document goes to the vault. When it's unclear, the note goes to the vault and a one-line pointer goes to memory.

I use three harnesses (Hermes, OpenCode, and Claude Code), and all three read and write the same two stores over MCP. Mnemosyne is a single local file, so sharing it just means every process opens the same path. There's no sync step.

A session starts with a recall pass against memory and ends with a write pass that saves new facts and files longer notes in the vault, linked from a parent index. On a schedule:

- At 04:00, memory consolidates old session records into summaries.
- Every hour, the vault is committed to git and its search index picks up new notes.
- At 04:30, the memory database is backed up with SQLite's online backup, read back and counted, and copied to my NAS.

Three things I learned the hard way:

- **The search index lags.** It used to rebuild nightly, so a note written in the morning didn't show up in search until 23:30, and search just returned nothing. It now refreshes hourly, which is cheap because the index commands are incremental.
- **Automatic recall is a hint.** Hermes injects memories into context ranked by similarity, and similar isn't the same as important. A rule that matters can fail to surface because it doesn't look like the question. That's why recall at the start of a session is a deliberate step.
- **The memory database had no backup.** The vault had history because it was already in git. The database held over a thousand memories and nothing protected it until I added the 04:30 job.

## Keeping an Eye on It

A hybrid setup needs watching, so three things run in the background:

- **Budget watch.** An hourly script with no model in it posts to Discord when a prepaid balance runs low, OpenCode Go hits its cap, or the Claude plan window passes 80 percent.
- **Router health.** A check every five minutes tells me if the router or the local model proxy stops answering, and again when it recovers.
- **Agent Ops dashboard.** A read-only plugin for the Hermes desktop app that shows the agents, the infrastructure, plan caps, balances, and spend. The fleet built it.

Because I own the router, the agents, the memory, and the notes, I can swap out any model the day its price, quality, or terms change. That turned out to be the control worth having.
