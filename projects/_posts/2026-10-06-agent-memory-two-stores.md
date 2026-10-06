---
layout: post
title: "Two Stores and One Rule — How My Agents Actually Remember Things 🧠"
subtitle: "A local SQLite memory, a 153-note Obsidian vault, and the honest part: recall is a deliberate step, not a background miracle"
category: Project
tags: [AI, Agents, Memory, Obsidian, SQLite, Hermes]
comments: true
thumbnail-img: /projects/assets/images/memory-01-layer-map.png
redirect_from: /2026-10-06-2026-10-06-agent-memory-two-stores/
---

# Two Stores and One Rule — How My Agents Actually Remember Things

Every agent harness has the same embarrassing failure: you finish a long session, the context window closes, and the next session starts from zero. The agent that spent an hour working out how your backup rotation works asks you what a backup rotation is the following morning.

I run AI agents on my own workstation — coding, infrastructure, research, writing about my vault — and I got tired of that. So there's a real memory layer now, and this post is how it works, what the numbers actually are, and the trade-offs I'm not going to pretend away.

## Two stores, and one rule that decides between them

The design is deliberately boring: **two places to keep things, and a rule that says which one a given piece of knowledge belongs in.**

![Memory layer map: two stores, their access paths, and the harnesses that reach them](/projects/assets/images/memory-01-layer-map.png){: .mx-auto.d-block :}

**Store A — the agent's own memory.** A local SQLite database, one file, private to the machine. It holds the small, durable stuff: facts, preferences, corrections, and a compressed record of past sessions. As of the day I wrote this, that file contains **1,324 working memories, 332 episodic summaries, 456 extracted facts, 124 standing instructions, 59 preferences, and 3 permanent persona rules.** It's written by the agent, not by hand, and it grows while I do other things.

**Store B — the vault.** An Obsidian vault of **153 Markdown notes**, human-owned, organised PARA-style, and committed to git every hour so it has history. This is where the long-form things live: design decisions, project notes, architecture records, the document you're reading the basis of.

The rule that separates them is one sentence long:

> A one- or two-line fact goes to the agent's memory. A paragraph, a decision, or an artifact goes to the vault.

That's it. A date that a drive failed on, a preference about how I like summaries, a correction the agent should never repeat — memory. The reasoning behind an architecture choice, three paragraphs of context, a plan with steps — vault. When it's genuinely unclear, the note goes to the vault and a one-line pointer fact goes into memory so the next session knows the note exists.

The reason the boundary matters is that the two stores fail differently. The database is good at *finding a needle* — "what's my preference for X" — and bad at being read end to end. The vault is the opposite: it's the thing a human reads, that grows into structure, and that survives on its own if the agents all disappeared tomorrow. Mixing them produces a database full of essays and a vault full of crumbs.

## Same two stores, both harnesses

I don't use one agent tool. So the constraint was that both harnesses had to reach the same memory, rather than each keeping its own private one.

The memory database is the native provider for my main harness, and it's also exposed over MCP, so the second harness reads and writes the exact same file. The vault is reached the same way in both: one MCP server for reading and writing notes, a second for semantic and keyword search. Neither harness gets a copy. There is one database and one vault.

That's the whole trick — no sync protocol, no export step, no reconciliation. The only reason it works is that the memory store was already a single local file, so "shared memory" is just "both processes open the same path."

## What actually happens in a session

![Session and nightly memory lifecycle](/projects/assets/images/memory-02-lifecycle.png){: .mx-auto.d-block :}

**At the start**, a recall pass runs against the memory store — a lookup, not a dump. Then I work, and along the way relevant memories get injected into the agent's context automatically.

**At the end**, there's a write pass. This is the part I care about most, because it's where a session stops being disposable. Durable facts from the session get written to memory, and anything long-form gets written to the vault as a note, linked from its parent index so it isn't an orphan.

**Overnight, three things happen on a schedule.** At 04:00 the memory store consolidates: old session records get compressed into summaries, so the store stays useful instead of drowning in raw history. Every hour, the vault gets committed to git and the search index is refreshed with anything new. And at 04:30, the memory database is backed up — a change I made the same day I wrote this, for reasons I'll come to.

## One question, four paths

![Retrieval flow: one question, four converging search paths](/projects/assets/images/memory-03-retrieval.png){: .mx-auto.d-block :}

Ask the agent a question and up to four things fire in parallel: whatever memory was injected into the context already, a direct recall against the memory database, an exact text search across the vault, and a semantic search over the vault that combines keyword matching with vector similarity. They converge on one answer, and the useful bit is that the answer can say *which store a claim came from* — the difference between "I remember you said this" and "this is in your architecture note from September."

## The honest part

None of the above is automatic in the way it sounds, and three trade-offs are real enough to be worth writing down.

**The index lags behind a fresh write.** The semantic search over the vault is an index, and an index is only as fresh as its last update. For a long time it was rebuilt once a night, which meant a note written in the morning was invisible to semantic search until 23:30 that evening — and worse, invisibly so. Search just returned "no results," which looks like the note doesn't exist rather than like the index is stale. I narrowed it to an hourly refresh, and kept the nightly full sweep as a backstop. The hourly job is only defensible because both index commands are incremental, so a run with nothing new to index is cheap; if that stopped being true I'd move to every four hours rather than pay for hourly sweeps.

**Injected context is relevance-ranked, and relevance is a guess.** Some memories get pushed into the context window automatically. That's convenient and also the least trustworthy path, because ranking is done by similarity, and *similar* is not *important*. A standing rule that matters to the current task can fail to surface simply because it doesn't look like the question. That's why recall is a deliberate step at the start of a session rather than something I let happen by itself — the automatic path is a bonus, not the mechanism I rely on. My advice for anyone building this: don't treat passive injection as a memory system. Treat it as a hint, and make the lookup explicit.

**The memory database had no backup until very recently.** This is the one that bothers me most in hindsight. The vault was safe — it's git, committed hourly, it has history. The memory database, which by then held over a thousand durable memories, was protected by nothing: no scheduled job, no script, no service. One bad file operation and it's simply gone. It now gets snapshotted nightly, after the consolidation run so the day's writes and the fresh summary are both captured, using the database engine's online backup rather than a file copy — copying an open database can capture a torn write. And the copies are read back and counted, on both ends, because a backup that has never been opened is not a backup; it's a hope. A copy also goes off the workstation to my NAS.

The general lesson generalises past this setup: **the thing you'd miss most is usually the thing you never thought to schedule a job for.** The vault had history because git was already there. The database had none because it looked like an implementation detail.

## What it buys

The point of all of this isn't a clever retrieval stack. It's that a session stops being the unit of work. You can close the laptop, and the next session starts with the context the last one earned — the fix, the preference, the decision, and a pointer to the note where the reasoning lives.

Two stores, one boundary rule, and an honest admission that the automatic part is a hint while the deliberate part is the mechanism. That's not autonomous memory, but it's memory I can check, back up, and explain — and after enough sessions, that turns out to be the part that matters.

---

*Counts in this post are a snapshot from the day it was published; the store grows daily. The memory layer, the vault, and their schedules are exactly as described, and infrastructure specifics are deliberately left out.*
