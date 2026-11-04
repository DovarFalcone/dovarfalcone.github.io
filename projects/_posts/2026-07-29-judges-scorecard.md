---
layout: post
title: "Rosette: Offline Horse Show Scorecards"
subtitle: "A scorecard app for judges, scribes, and judging teams that works with no signal"
category: Project
tags: [Project, AQHA, Judging, Scorecard, Horse Show]
comments: true
topic: horse-shows
---

[Rosette](https://rosette.maradara.com/) is a scorecard app for horse show judges, scribes, and judging teams. It started as Judges Scorecard, a tool I built because I sat in the stands at AQHA shows and wanted to know how the judges got to their numbers. Rosette is the version built for the people filling out the cards.

## Why Offline

Show barns and arenas are bad places to count on a cell signal. Rosette runs in the browser, saves everything on the device, and keeps working once it's loaded, even with no connection. Scorecards are stored in a local SQLite database (`sql-wasm`), so nothing needs an account or a server.

On a phone or tablet you can add it to the home screen and it opens full screen like a regular app.

## Scoring

Rosette uses the AQHA scoring system for pattern classes like Reining, Ranch Riding, Trail, and Western Riding:

- Every run starts at 70.
- Each maneuver gets a score from -1.5 to +1.5.
- Penalties come off the total, and each class has its own penalty buttons. Reining uses 0.5, 1, 2, and 5. Ranch Riding uses 1, 3, 5, and 10.

Add the exhibitors by back number, score each maneuver, apply penalties, and the app adds it up and ranks the class.

## The Rulebook

The full 2026 AQHA rulebook is built in and searchable. That's 2,739 rules across 42 chapters, covering all 29 judged class chapters plus the show rules and judges' rules. You can filter by class, so when a penalty call comes up you can look up the exact wording without leaving the scorecard. The rulebook is cached with the app, so search works offline too.

## Try It

[Open Rosette](https://rosette.maradara.com/). No account needed.
