---
layout: post
title: The Deepest Classes and Average Field Sizes 📏
subtitle: Where a placing means beating the most horses — and how big each discipline's fields really run
category: Project
tags: [Project, AQHA, Data Analysis, Horse Show, Equine]
comments: true
---

# The Deepest Classes and Average Field Sizes

A placing in a 5-horse class isn't the same as a placing in a 170-horse class. The deepest class in the database ran **171 entries**, and across **5,787 placed classes in 50 disciplines**, average field size differs enormously — from 81 horses down to just 2.

This page lists the deepest classes — where a placing means beating the most horses — and how big each discipline's fields run on average.

*Based on 191,605 placings · analysis refreshed 22 Sept 2026.*

> **Updated 27 September 2026.** The August cut of this article covered a much smaller slice of the database. Two things changed with the added shows: the **deepest classes** list is no longer Congress-only — the AQHA World Championship Show and NSBA World Championship Show now appear — and the **average field sizes fell almost everywhere**, because the new classes ingested skew smaller (a typical Congress class is deeper than a typical class at a smaller show). Read the two sections together: the top of the sport got no deeper, the middle of the dataset got shallower.

---

## The deepest classes

Top classes by entries, from the shows in the database. `Placed` is the number of riders with a posted numeric placing (entries can exceed it — not everyone who enters places):

| Show | Class | Discipline | Entries | Placed |
|---|---|---|---|---|
| 2025 Congress | NRHA Open Reining Level 4 Futurity Congress | Reining | **171** | 31 |
| 2025 Congress | Senior Barrel Racing Congress | Barrels | 162 | 15 |
| 2025 Congress | NRHA Green Reiner Level 2 Congress | Reining | 125 | 15 |
| 2025 Congress | Level 1 Youth Horsemanship 14-18 Congress | Horsemanship | 115 | 15 |
| 2025 Congress | NRHA Rookie Reining Level 2 Congress | Reining | 114 | 15 |
| 2025 Congress | Congress Barrel Racing Sweepstakes Congress | Barrels | 110 | 15 |
| 2025 Congress | NRHA Open Reining Level 2 Futurity Congress | Reining | 108 | 30 |
| 2025 Congress | Level 1 Ranch Trail Congress | Ranch Trail | 107 | 15 |
| 2025 AQHA World Show | L3 Junior Dally Team Roping — Heeling WS | Roping | 105 | **90** |
| 2025 Congress | Amateur Showmanship Congress | Showmanship | 105 | 15 |
| 2025 Congress | Youth Showmanship 15-18 Congress | Showmanship | 103 | 15 |
| 2026 NSBA World Show | NSBA Senior Trail — Limited Rider WS | Trail | 103 | 15 |

The top of the list is still **Congress, with Reining and Barrels** doing most of the work — but the AQHA World Show and NSBA World Show now make it in, which they couldn't when this article was first cut. Note the `Placed` column: most Congress classes publish **15 placings** regardless of how many entered, while the World Show's 105-entry Roping class published **90**. How deep a result sheet goes is a *show's* choice, not a property of the class — so "deepest class" and "deepest result list" are different rankings.

---

## Average field size by discipline

Mean entries per class within each discipline, over the same placed-class set. Disciplines with fewer than 10 classes are omitted (too noisy to read); `Classes` is the count behind each figure:

| Discipline | Avg entries | Classes |
|---|---|---|
| Barrels | **81.3** | 12 |
| Working Western Rail | 48.5 | 12 |
| Reining | 23.3 | 174 |
| Roping | 22.6 | 60 |
| Equitation Over Fences | 19.8 | 12 |
| VRH Ranch Riding | 17.8 | 11 |
| Ranch Riding | 16.0 | 341 |
| Trail | 15.7 | 548 |
| Longe Line | 15.6 | 33 |
| Showmanship | 15.4 | 351 |
| Working Cow Horse | 15.2 | 24 |
| Ranch Trail | 14.7 | 280 |
| Horsemanship | 14.6 | 390 |
| Pole Bending | 14.6 | 40 |
| Cutting | 14.6 | 14 |
| Ranch Rail Pleasure | 13.9 | 19 |
| Western Rail | 12.4 | 70 |
| Ranch Pleasure | 12.3 | 22 |
| Western Pleasure | 12.0 | 680 |
| Hunt Seat Equitation | 12.0 | 363 |
| Western Riding | 11.3 | 226 |
| Conformation | 11.3 | 25 |
| Hunter Under Saddle | 11.2 | 637 |
| Ranch Rail | 10.8 | 110 |
| Working Hunter | 10.0 | 115 |
| Barrel Racing | 9.2 | 37 |
| Hunter Hack | 9.1 | 96 |
| Equitation over Fences | 7.9 | 52 |
| Halter | 6.2 | 858 |
| Pleasure Driving | 4.0 | 55 |
| Stake Race | 3.7 | 19 |
| All Around | 2.0 | 18 |

<svg viewBox="0 0 560 210" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Average field size by discipline">
  <line x1="150" y1="16" x2="150" y2="180" stroke="#999" stroke-width="1"/>
  <g font-size="11">
    <text x="140" y="36" text-anchor="end" fill="#555">Barrels</text>
    <rect x="150" y="26" width="160" height="16" fill="#6a9e78"/>
    <text x="316" y="39" fill="#444">81.3</text>
    <text x="140" y="60" text-anchor="end" fill="#555">Reining</text>
    <rect x="150" y="50" width="46" height="16" fill="#6a9e78"/>
    <text x="202" y="63" fill="#444">23.3</text>
    <text x="140" y="84" text-anchor="end" fill="#555">Roping</text>
    <rect x="150" y="74" width="44" height="16" fill="#6a9e78"/>
    <text x="200" y="87" fill="#444">22.6</text>
    <text x="140" y="108" text-anchor="end" fill="#555">Ranch Riding</text>
    <rect x="150" y="98" width="32" height="16" fill="#d0a65e"/>
    <text x="188" y="111" fill="#444">16.0</text>
    <text x="140" y="132" text-anchor="end" fill="#555">Trail</text>
    <rect x="150" y="122" width="31" height="16" fill="#d0a65e"/>
    <text x="187" y="135" fill="#444">15.7</text>
    <text x="140" y="156" text-anchor="end" fill="#555">Western Riding</text>
    <rect x="150" y="146" width="22" height="16" fill="#d0a65e"/>
    <text x="178" y="159" fill="#444">11.3</text>
    <text x="140" y="180" text-anchor="end" fill="#555">Halter</text>
    <rect x="150" y="170" width="12" height="16" fill="#d0a65e"/>
    <text x="168" y="183" fill="#444">6.2</text>
  </g>
  <text x="150" y="202" fill="#777" font-size="11">Mean entries per class (green = deepest tiers, tan = mid-pack and smaller)</text>
</svg>

The three-tier structure is still there, but the middle tier moved down:

- **Speed events and reining-style classes run deep** — Barrels (81) and Working Western Rail (49) are in a league of their own, with Reining (23) and Roping (23) next.
- **Pattern and rail classes sit mid-pack at 11–16** — Trail, Ranch Riding, Showmanship, Horsemanship and Ranch Trail all cluster there. In August these sat at 17–21; the drop is the new dataset's smaller classes, not the sport shrinking.
- **Halter is enormous in participation but tiny in field size** — 858 classes averaging just **6.2** entries, more than any other discipline. That's the structure of halter: hundreds of narrow divisions, few horses in each.
- **The very bottom is real too** — All Around averages 2.0 entries per class (18 classes), and Stake Race 3.7 (19). A win there is worth having, but it isn't beating a field.

---

## Methodology & caveats

- Classes are those with at least one Combined Judges numeric placing; the entrycount comes from the show schedule, deduped per class (the schedule holds duplicate rows for some classes).
- **Entrycounts are the scheduled entries**, not the number of riders who actually showed up and placed — a scratch-heavy class can place far fewer than it entered, and most Congress classes publish only 15 placings no matter how big they were.
- **Averages depend on which classes are in the database.** The August version of this table showed Reining at 39.0 and Western Rail at 22.2 — those figures didn't change because reining got easier, they changed because 94 more reining classes and 40 more western rail classes entered the dataset, most of them small. Treat any single-discipline average as a picture of the *current sample*, not of the discipline.
- **"Deepest in the database" is not "deepest in the sport."** The database covers the shows I've ingested — Congress, the AQHA World Show and NSBA World Show dominate so far — not every show ever run.

---

*This is one of a series of data articles built on my equine-data results database — a personal AQHA show-results explorer that analyzes every class in the dataset.*
