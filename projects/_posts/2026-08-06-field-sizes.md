---
layout: post
title: The Deepest Classes and Average Field Sizes 📏
subtitle: Where a placing means beating the most horses — and how big each discipline's fields really run
category: Project
tags: [Project, AQHA, Data Analysis, Horse Show, Equine]
comments: true
---

# The Deepest Classes and Average Field Sizes

A placing in a 5-horse class isn't the same as a placing in a 170-horse class. The deepest class in the database ran **171 entries**, and across the classes I've collected, average field size differs enormously by discipline — from 81 horses down to just 2.

This page lists the deepest classes — where a placing means beating the most horses — and how big each discipline's fields run on average.

*Based on 86,281 placings · analysis refreshed Aug 2026.*

---

## The deepest classes

Top classes by entries, from the shows in the database. `Placed` is the number of riders with a posted numeric placing (entries can exceed it — not everyone who enters places):

| Class | Discipline | Entries | Placed |
|---|---|---|---|
| NRHA Open Reining Level 4 Futurity Congress | Reining | **171** | 31 |
| Senior Barrel Racing Congress | Barrels | 162 | 15 |
| NRHA Green Reiner Level 2 Congress | Reining | 125 | 15 |
| Level 1 Youth Horsemanship 14-18 Congress | Horsemanship | 115 | 15 |
| NRHA Rookie Reining Level 2 Congress | Reining | 114 | 15 |
| Congress Barrel Racing Sweepstakes Congress | Barrels | 110 | 15 |
| NRHA Open Reining Level 2 Futurity Congress | Reining | 108 | 30 |
| Level 1 Ranch Trail Congress | Ranch Trail | 107 | 15 |

Every single class in the top 8 is from **the 2025 All American Quarter Horse Congress** — the sport's biggest show — and **Reining and Barrels** dominate the deepest classes. Note how many classes show only **15 placed** despite 100+ entries: entrycounts reflect who's *in the class*, not who actually shows up and places.

---

## Average field size by discipline

Mean entries per class within each discipline, over the same placed-class set. Disciplines with few classes are noisy — treat small `Classes` counts as hints:

| Discipline | Avg entries | Classes |
|---|---|---|
| Barrels | **81.3** | 12 |
| Working Western Rail | 48.5 | 12 |
| Reining | 39.0 | 80 |
| Roping | 28.3 | 40 |
| Western Rail | 22.2 | 30 |
| Pole Bending | 21.4 | 24 |
| Ranch Riding | 20.5 | 165 |
| Showmanship | 19.1 | 175 |
| Ranch Trail | 18.9 | 124 |
| Horsemanship | 18.6 | 180 |
| Trail | 17.5 | 265 |
| Western Pleasure | 15.9 | 296 |
| Hunt Seat Equitation | 14.0 | 182 |
| Hunter Under Saddle | 13.7 | 282 |
| Western Riding | 12.3 | 127 |
| Halter | 6.6 | 506 |

<svg viewBox="0 0 560 210" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Average field size by discipline">
  <line x1="150" y1="16" x2="150" y2="180" stroke="#999" stroke-width="1"/>
  <g font-size="11">
    <text x="140" y="36" text-anchor="end" fill="#555">Barrels</text>
    <rect x="150" y="26" width="160" height="16" fill="#6a9e78"/>
    <text x="316" y="39" fill="#444">81.3</text>
    <text x="140" y="60" text-anchor="end" fill="#555">Reining</text>
    <rect x="150" y="50" width="77" height="16" fill="#6a9e78"/>
    <text x="233" y="63" fill="#444">39.0</text>
    <text x="140" y="84" text-anchor="end" fill="#555">Roping</text>
    <rect x="150" y="74" width="56" height="16" fill="#6a9e78"/>
    <text x="212" y="87" fill="#444">28.3</text>
    <text x="140" y="108" text-anchor="end" fill="#555">Ranch Riding</text>
    <rect x="150" y="98" width="41" height="16" fill="#d0a65e"/>
    <text x="197" y="111" fill="#444">20.5</text>
    <text x="140" y="132" text-anchor="end" fill="#555">Trail</text>
    <rect x="150" y="122" width="35" height="16" fill="#d0a65e"/>
    <text x="191" y="135" fill="#444">17.5</text>
    <text x="140" y="156" text-anchor="end" fill="#555">Western Riding</text>
    <rect x="150" y="146" width="25" height="16" fill="#d0a65e"/>
    <text x="181" y="159" fill="#444">12.3</text>
    <text x="140" y="180" text-anchor="end" fill="#555">Halter</text>
    <rect x="150" y="170" width="13" height="16" fill="#d0a65e"/>
    <text x="169" y="183" fill="#444">6.6</text>
  </g>
  <text x="150" y="202" fill="#777" font-size="11">Mean entries per class (green = highest, tan = smallest)</text>
</svg>

A clear three-tier structure emerges:
- **Speed events run deep** — Barrels (81) and Reining (39) draw the biggest fields by far.
- **Pattern and rail classes sit mid-pack** — Ranch Riding, Showmanship, Horsemanship, Trail all average roughly 17–21.
- **Halter is enormous in participation but tiny in field size** — 506 classes averaging just 6.6 entries, a reflection of how many separate halter divisions there are versus how few horses enter each.

---

## Methodology & caveats

- Classes are those with at least one Combined Judges numeric placing; the entrycount comes from the show schedule, deduped per class (the schedule holds duplicate rows for some classes).
- **Entrycounts are the scheduled entries**, not the number of riders who actually showed up and placed — a scratch-heavy class can place far fewer than it entered.
- **"Deepest in the database" is not "deepest in the sport."** The database covers the shows I've ingested so far, so the ranking reflects which shows are in the dataset — the 2025 Congress dominates because that's a huge show — not every show ever run.

---

*This is one of a series of data articles built on my equine-data results database — a personal AQHA show-results explorer that analyzes every class in the dataset.*
