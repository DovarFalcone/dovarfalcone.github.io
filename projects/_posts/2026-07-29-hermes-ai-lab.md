---
layout: post
title: Building an Autonomous Local AI Lab
subtitle: "A guide to setting up an AI development environment, and an honest update: it started local and free, and it is now a hybrid"
category: Project
tags: [Project, AI, Local-LLM, Hermes, Privacy, Workflow]
comments: true
---

# Building an Autonomous Local AI Lab

> **Updated 10 October 2026.** I wrote this page in July, when the whole setup ran on local hardware and free model tiers. It no longer does. The stack is now a hybrid: two paid subscriptions, a router with ordered fallback, cloud models doing most of the work, and local Ollama as the last fallback. A single agent has grown into a small fleet, memory is two stores instead of one, and I now track cost and health. I have rewritten the page to describe what runs today, and I say plainly below which of my original goals held and which did not.

This is a high-level walkthrough of how I architect an AI-assisted development lab on one workstation: the host, the models, the router, the agents and the memory. Each deeper topic has its own post, linked where it comes up.

## The original goals, and how they held up

In July I set out four principles. Here is the honest scorecard.

1.  **Privacy: "If the code is on my machine, the intelligence should be too."** *Partly.* My notes, memory and agent state still live on my own machine, and the small background jobs can still run on local models. But most of the real work now goes to cloud models, so prompts and code do leave the machine. My original claim that nothing is ever sent off-machine is no longer true, and I should not have promised it so absolutely.
2.  **Speed: no network latency for local inferences.** *Did not hold up for serious work.* The local model is the fallback of last resort, not the front line. When I measured it with the full 256K context loaded, it ran at about 19 tokens per second with some spill into system memory, and the hosted models are the ones I reach for.
3.  **Control: I own the stack from the OS up to the model weights.** *Held for the stack, not for the weights.* I still own the OS, the containers, the router, the agents and the data. I do not own the weights of the models that do most of the work.
4.  **No subscriptions.** *Did not hold.* I pay for Claude Pro and for OpenCode Go, and I keep small prepaid balances with a couple of API providers.

I also claimed "zero marginal cost" and "the same model version every day". Neither survived: hosted models cost money per use or per plan window, and they change underneath you.

## Why it moved from "all local and free" to hybrid

Free tiers and a single local model were enough to prove the idea. They were not enough to run a fleet of agents that write code, review each other's work and keep a task board moving. Free models rate-limit, disappear and vary in quality. A local model that fits on a 10 GB graphics card is fine for classification and session titles, but a poor fit for long coding sessions.

So I kept the free and local lanes for the frequent, low-stakes work and put paid models where quality matters. I measured the real spend rather than guessing: the cost post linked below walks through eight weeks of logged calls, where the money actually went, and what I changed.

## The architecture today

### 1. The host
A Linux workstation on Arch with an NVIDIA RTX 3080 (10 GB). A rolling-release distribution still gives me the newest kernel and driver support, which matters when you lean on a GPU.

### 2. The local inference engine (Ollama)
Ollama still runs in a container. The models I actually use from it are `gemma4:12b-256k` as the main local model, with a 256K-token context window, and `qwen3:8b` as the small one for cheap background jobs. A small embedding model sits alongside them. Local inference is now the last fallback in the chain, not the front line.

### 3. The model router (9router)
9router is a small router running in a container on the same machine. The July version of this page described it as a round-robin over free OpenRouter models. That is no longer how it works. It now serves named **combos**, each an *ordered* list that is tried in sequence, falling to the next entry when one fails or is capped:

- **`DEEPSEEK-FLASH`** is the everyday default for most of the fleet: a prepaid OpenRouter slot first, then the OpenCode Go subscription, then a free lane, then a direct paid DeepSeek slot.
- **`PI-CODER`** is for the coding agent. All three of its entries are paid, deliberately, because the free endpoints I tried log prompts and my repositories are private.
- **`FREE`** is 25 free models, ranked best to worst and rebuilt automatically twice a week.

Order matters. With in-order fallback the first entry takes the traffic until it fails, so where a paid model sits in a combo decides whether it bills. I learned that the hard way, and the cost post covers it.

Each agent also has its own fallback chain behind the router: the combo first, then direct provider slots, then the free combo, and finally the local Gemma model on my own GPU.

### 4. The agents: a fleet, not a single bot
The July version had one Hermes Agent. Today **Hermes** is the framework behind a small fleet of specialist agents, each its own profile with its own personality, tools and permissions:

- An **Orchestrator**, the general agent I talk to directly, which routes work and reviews results. It runs on Claude.
- **Dalinar**, the engineering lead, who plans and reviews.
- **Navani**, the coding lane.
- **Kaladin**, who watches the infrastructure.
- **Shallan**, who looks after the notes vault.
- **Jasnah**, who does research.

Work moves between them on a Kanban board with a review gate. **Claude Code** is my primary point of contact and acts as my proxy into the fleet, sending quick questions straight to the Orchestrator and tracked work to the board. The full story is in [One Bot Per Domain: How My Agent Fleet Runs on a Kanban Board](/2026-10-06-agent-fleet-kanban/).

### 5. Memory: two stores, not one
The July post said my memory was an Obsidian vault. It is now two stores with a clear boundary. A local SQLite memory (Mnemosyne) holds small durable facts and preferences. The Obsidian-compatible PARA vault holds long-form notes, with a local semantic search index over it. See [Two Stores and One Rule](/2026-10-06-agent-memory-two-stores/) for how it works, including the honest part about recall being a deliberate step.

## Keeping an eye on it

A hybrid setup needs watching, so I added things that did not exist in July:

- **Budget watch.** An hourly script, with no model involved, posts to Discord only when something changes: a prepaid balance running low, the OpenCode Go plan hitting its cap, or the Claude plan window passing 80 percent.
- **Router health.** A check every five minutes tells me if the router or the local model proxy stops answering, and says when it recovers.
- **Agent Ops dashboard.** A plugin for the Hermes desktop app, built by the fleet itself, shows the agents, the infrastructure, plan caps and balances, and spend at a glance. It is read-only and still growing.

## The "second brain" workflow still holds

The part of the July post that has aged best is the workflow. My research and project notes still follow a strict PARA layout (Projects, Areas, Resources, Archives), the notes are still Obsidian-compatible Markdown, and the agents can still read my notes, update project pages and generate code that follows patterns I have established. What changed is where the thinking happens, not how the notes are organised.

## Why build this anyway?

A local-first lab is still worth building, just for different reasons than I first gave:

- **Control of the plumbing.** Because the router, agents, memory and notes are mine, I can swap any model out the moment its price, quality or terms change. That is the real autonomy.
- **Cost you can see.** Every call is logged locally with token counts and an estimated cost, so I can measure spend instead of guessing. The numbers are in [My AI Fleet Cost $24.68 in Eight Weeks](/2026-09-23-ai-fleet-costs/).
- **Privacy by routing, not by promise.** Sensitive or boring jobs stay on local models. The work that needs a stronger model goes to one deliberately, and I choose which lanes are allowed to see private repositories.

---

*This project is an evolving lab. The goal is still to maximize developer productivity while keeping the "Second Brain" under my control. The difference from July is that I now say out loud where that control has limits.*
