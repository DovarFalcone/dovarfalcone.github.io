---
layout: post
title: One Bot Per Domain — How My Agent Fleet Runs on a Kanban Board 🗂️
subtitle: Four specialist profiles, a dispatcher, and a review gate that nothing ships without
category: Project
tags: [AI, Agents, Hermes, Kanban, Automation, Workflow]
comments: true
---

# One Bot Per Domain — How My Agent Fleet Runs on a Kanban Board

I run a small fleet of AI agents on a single workstation. The interesting part isn't the models — it's the *structure*: each agent is a separate profile with its own personality, tools, and permissions, and the only way work moves between them is a Kanban board.

This post is the mechanics of that setup: what a "bot" actually is, how work gets routed to the right one, and why nothing ships without a second pass.

## A bot is a profile, not a program

The mental model that makes this understandable is blunt: **a bot is just a Hermes profile.**

A profile is a directory — its own config, its own SOUL file (the personality and operating rules), its own tool grants, its own scheduled jobs, and its own runtime state. There's one binary. The profile is the *identity*.

Because of that, talking to a specific bot is a command-line flag, not a separate daemon:

```bash
# Ask the infrastructure bot for the array status
hermes -p kaladin chat -q "What's the Unraid array status?"

# Ask the research bot for a cited digest
hermes -p jasnah chat -q "Summarise today's AI feeds with sources"

# List every profile on the machine
hermes profile list
```

That single idea — profile-as-identity — is what makes the rest of the system cheap. A new specialist is a new profile, not new infrastructure.

## The roster

Five profiles carry work right now. Four of them are specialists; the fifth is the dispatcher.

| Bot | Profile | Domain | What it owns |
|---|---|---|---|
| **Kaladin** | `kaladin` | Infrastructure | Unraid array health, disk temperatures, parity, Docker, the little Pi sensor |
| **Shallan** | `shallan` | Knowledge base | The Obsidian vault, note links, semantic search index health |
| **Jasnah** | `jasnah` | Research | Feeds, market data, grounded and cited digests |
| **Navani** | `coder` | Implementation | Code, builds, tests, deployments |
| **Orchestrator** | `default` | Coordination | Triage, decomposition, routing, review |

![The fleet hierarchy: one orchestrator, four domain specialists, and the board between them](/projects/assets/images/agent-fleet-hierarchy.png){: .mx-auto.d-block :}

Each has a distinct voice. All four run with a shell and file access too — that turned out to be unavoidable for agents that fetch feeds, run scripts, and touch files, so pretending a specialist could do its job without one would just be theatre. What actually differs is the **integrations** each one is wired to. Kaladin holds the Unraid integration and never touches the vault. Shallan holds the Obsidian vault and the semantic-search index, and nothing that can reach the server. Jasnah holds neither — the open web and citations are her whole world. Navani gets the full engineering set — browser, image generation, delegation — because implementation genuinely needs it.

**Least privilege is real, but a missing shell isn't what enforces it.** Every specialist has one, so a research bot that reads a hostile page could in principle act on it. What limits the blast radius is the structure around the work: one narrow domain per bot, one assignee per card, and a review gate nothing clears without a second pass. A worker's report is a claim; review is where it meets the artifact.

## Routing by domain

When a request comes in, the first question is *which domain does this belong to?*

- Something is wrong with the server → **kaladin**.
- A note needs finding or linking → **shallan**.
- A question needs the open web and citations → **jasnah**.
- A repo needs changing → **coder**.
- It spans several of those, or it's unclear → **default**, which decomposes it.

That last case matters. A vague, multi-domain ask doesn't get one agent guessing across four specialties — it gets broken into child cards, each addressed to exactly one specialist.

## Why only one profile holds a gateway

All of these bots live in the same chat platform. But **only the orchestrator profile runs a gateway.**

The reason is boring and important: every bot profile was cloned from the same base, which means each one carries a *copy* of the same bot token. A gateway is a process that connects to that token and consumes messages. Start a second gateway on a second profile and you have two processes answering the same identity — duplicated replies, races, and a genuinely confusing mess.

So there is exactly one gateway, the bots are addressed by profile rather than by their own connection, and the fleet stays a single coherent presence. One token, one gateway, no exceptions.

## The Kanban lifecycle

This is the part I'd want someone else to copy. Work doesn't hop between agents by luck — it moves over a board, and every transition is a recorded state change.

1. A card lands in the backlog or triage lane
2. The orchestrator wakes, reads the card, and checks who's available
3. It decomposes the work into minimal child cards, each with ONE assignee
4. The dispatcher fans out — it spawns `hermes -p <assignee>` per child
5. The assigned worker does the work and reports back with evidence
6. The worker hands off to review (reviewer = the orchestrator profile)
7. Review approves, or returns specific, cited changes

A few properties fall out of that design:

- **One assignee per card.** There's no committee. If two specialists both need to act, that's two cards with a dependency edge, not one ambiguous card.
- **The worker doesn't grade its own homework.** The handoff to review is a distinct step. Review runs on the orchestrator profile with a review rubric loaded, and it looks for scope match, correctness, verification, and simplicity — not just "does it seem fine."
- **Claims are evidence, not authority.** When a worker says "deployed and verified," that's a self-report. The review step is where it gets checked against the actual artifact, the real command output, or the live URL.

The board is also just a database. There's a desktop view for it, but the command line drives it directly, which means the whole fleet is scriptable and every state change is auditable after the fact.

## Workers can't unblock themselves

This is the rule I'd defend hardest.

Any worker can hit a wall: a missing credential, a decision only a human should make, a dependency on another card. When that happens it **blocks the card with a reason and stops.** It does not guess, and it cannot clear its own block.

Only the orchestrator — the profile holding unblock permission — can clear it. That asymmetry is deliberate. If a worker could unblock itself, "blocked" would decay into "retry until something gives," and a genuine missing-credential wall would look identical to a flaky run. Keeping the unblock authority in one place means a blocked card is always a real signal that reaches a human.

The same discipline applies to retries: a transient failure can be re-queued, but a card that keeps getting unblocked and re-blocked for the same reason escalates rather than loops.

## When work goes to the board instead of staying in chat

Not everything deserves a board. Most things don't — and knowing the line is what keeps the fleet from turning every question into a project.

**Stays in chat:** a computation, a status read, a single lookup, a small reversible edit, a direct answer. Anything that finishes in moments.

**Goes to the board:** anything that touches a repo, runs a build or a test suite, crawls the web, changes several files, chains multiple tools, or runs longer than a single sitting. Research, investigation, refactors, audits, setup work — the verbs that quietly turn into an afternoon.

The tell is simple: **if I can't finish it in the next few moments, it becomes a card.** The card gets an ID, the chat gets the ID, and the work happens in the background where it can be reviewed, retried, and audited instead of blocking the conversation. The chat stays a conversation; the board stays a record.

## What this actually buys

Three things, in order of how much I care:

1. **Review is structural, not aspirational.** Because the handoff is a real state change, an unreviewed change is a card in the wrong lane — visible on the board, not lost in a transcript.
2. **Specialisation is enforceable.** Toolsets and integrations are per-profile, so least privilege isn't a policy I have to remember; it's what the profile is actually wired to.
3. **Nothing important lives only in a chat log.** The chat is where I *decide*; the board is where work *happens*. A stalled card sits there in the open, and a blocked one asks for exactly the thing it's missing.

It's not a swarm and it isn't autonomous in any grand sense — it's five narrow agents, one board, and a rule that says the person who does the work isn't the person who signs it off. That's the whole trick.

---

*The fleet runs on Hermes Agent over a local model stack, with specialist profiles cloned from a base profile and routed through a shared Kanban board. Board mechanics and profile commands are exactly as described; provider and infrastructure specifics are deliberately left out.*
