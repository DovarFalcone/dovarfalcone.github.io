---
layout: post
title: The Deepest Classes and Average Field Sizes
subtitle: Where a placing means beating the most horses — and how big each discipline's fields really run
category: Project
tags: [Project, AQHA, Data Analysis, Horse Show, Equine]
comments: true
---

# The Deepest Classes and Average Field Sizes

A placing in a 5-horse class isn't the same as a placing in a 224-horse class. The deepest class in the database ran **226 scheduled entries**, and across **72,316 placed classes** — **426,597 placings** in all — average field size differs enormously, from the seventies down to just three.

This page lists the deepest classes — where a placing means beating the most horses — and how big each discipline's fields run on average. It also does something the earlier cuts couldn't: the database now holds the **published draw sheets** as well as the show schedules, so for 2,549 classes there are two independent measures of "how many horses were in this class" — and they disagree far more often than you'd expect.

*Analysis refreshed 16 October 2026 · computed fresh from the production database.*

> **Updated 16 October 2026.** The corpus is now several times larger than the September cut, and — more importantly — the draw sheets are in. That matters because the two "field size" numbers in the data measure different things: `entrycount` comes from the **schedule** (how many entries the class was scheduled to have) while the draw sheet records **how many riders actually drew into that go**. For 1,746 of 2,549 classes the draw sheet is larger, occasionally by more than 100. The averages below use the schedule, because that's the only measure available for every class; the draw-sheet comparison is its own section, and it changes how the deepest-classes list should be read.

---

## The deepest classes

Two rankings, because the database holds two things. `Scheduled` is the entry count on the show's schedule; `Placed` is the number of riders who actually received a numeric placing — and as you'll see, those are very different numbers.

**By scheduled entries:**

| Show | Class | Discipline | Scheduled | Placed |
|---|---|---|---|---|
| 2026 Congress | 4D Open Barrel Racing Congress | Barrels | **226** | 15 |
| 2025 Congress | NRHA Open Reining Level 4 Futurity Congress | Reining | 171 | 31 |
| Cactus Reining Classic I | Open SL1 | Reining | 170 | 34 |
| 2025 Congress | Senior Barrel Racing Congress | Barrels | 162 | 15 |
| 2026 Redbud Spectacular | Junior Reining SC1 | Reining | 152 | 10 |
| 2026 Congress | NRHA Rookie Reining Level 2 Congress | Reining | 151 | 15 |
| 2024 Redbud Spectacular | Junior Reining RB2 | Reining | 139 | 15 |
| 2024 Congress | NRHA Green Reiner Level 2 Congress | Reining | 134 | 15 |
| 2026 Redbud Spectacular | Junior Reining SC2 | Reining | 129 | 8 |
| 2025 Congress | NRHA Green Reiner Level 2 Congress | Reining | 125 | 15 |
| 2024 Congress | Level 1 Ranch Trail Congress | Ranch Trail | 123 | 15 |
| 2024 Redbud Spectacular | Junior Reining RB1 | Reining | 120 | 17 |

**By the published draw sheet** — the number of riders who actually drew into the go:

| Show | Class | Discipline | Drawn | Placed |
|---|---|---|---|---|
| 2026 Congress | 4D Open Barrel Racing Congress | Barrels | **224** | 15 |
| 2026 Congress | All Star Reining Stakes Open Derby Level 1 Congress | Reining | 166 | 15 |
| 2026 Congress | All Star Reining Stakes Open Derby Level 2 Congress | Reining | 166 | 16 |
| 2026 Congress | All Star Reining Stakes Open Derby Level 3 Congress | Reining | 166 | 16 |
| 2026 Congress | All Star Reining Stakes Open Derby Level 4 Congress | Reining | 166 | 15 |
| 2026 Congress | NRHA Intermediate Open Reining Congress | Reining | 166 | 16 |
| 2026 Congress | NRHA Prime Time Open Reining Congress | Reining | 166 | 15 |
| 2026 Congress | NRHA Limited Open Reining Congress | Reining | 166 | 18 |
| 2026 Congress | NRHA Open Reining Congress | Reining | 166 | — |
| 2026 Congress | NRHA Novice Horse Level 1 — Open Congress | Reining | 158 | 15 |

**Reining and Barrels** dominate both lists — they are the disciplines where a single class can hold 150+ horses. But note two things in the columns:

- **Most Congress classes publish 15 placings** regardless of how many entered. A 224-horse barrel race and a 15-horse local class both produce a 15-line result sheet. So "deepest class" and "deepest result list" are different rankings, and any per-placing statistic inherited from the result sheet carries that ceiling with it.
- **The draw-sheet list is not the schedule list reordered.** The All Star Reining Stakes Derby runs four levels at once, so one 166-rider draw sheet covers classes whose schedules say 42, 57, 73 and 75. That is the structural quirk behind almost every large disagreement below.

---

## Average field size by discipline

Mean scheduled entries per class within each discipline. `Classes` is the count behind each figure — the small-`n` rows are noisy and shown only so you can see how much of the dataset is halter and pleasure:

| Discipline | Avg entries | Classes |
|---|---|---|
| Barrels | **73.8** | 37 |
| Working Western Rail | 51.5 | 34 |
| Equitation Over Fences | 20.5 | 32 |
| Cow Work | 18.0 | 127 |
| Stock Horse Pleasure | 16.8 | 182 |
| Reining | 15.3 | 2,206 |
| Roping | 14.5 | 642 |
| Ranch Rail Pleasure | 13.6 | 39 |
| Pole Bending | 11.9 | 200 |
| Boxing | 10.9 | 127 |
| Ranch Riding | 9.8 | 4,087 |
| Barrel Racing | 9.5 | 285 |
| Ranch Trail | 9.3 | 3,165 |
| Trail | 8.7 | 6,478 |
| Showmanship | 8.6 | 4,763 |
| Horsemanship | 8.1 | 5,000 |
| Cutting | 8.0 | 430 |
| Western Rail | 7.6 | 1,049 |
| Western Pleasure | 7.0 | 6,492 |
| Ranch Rail | 7.0 | 1,276 |
| Conformation | 6.8 | 550 |
| Longe Line | 6.7 | 424 |
| Working Hunter | 6.7 | 766 |
| Western Riding | 6.6 | 2,244 |
| Hunter Under Saddle | 6.5 | 5,801 |
| Hunt Seat Equitation | 6.3 | 3,998 |
| Halter | **5.2** | 8,815 |
| Pleasure Driving | 3.2 | 299 |
| Jumping | 3.0 | 104 |

<svg viewBox="0 0 560 210" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Average field size by discipline">
  <line x1="150" y1="16" x2="150" y2="180" stroke="#999" stroke-width="1"/>
  <g font-size="11">
    <text x="140" y="36" text-anchor="end" fill="#555">Barrels</text>
    <rect x="150" y="26" width="160" height="16" fill="#6a9e78"/>
    <text x="316" y="39" fill="#444">73.8</text>
    <text x="140" y="60" text-anchor="end" fill="#555">Working Western Rail</text>
    <rect x="150" y="50" width="112" height="16" fill="#6a9e78"/>
    <text x="268" y="63" fill="#444">51.5</text>
    <text x="140" y="84" text-anchor="end" fill="#555">Reining</text>
    <rect x="150" y="74" width="33" height="16" fill="#6a9e78"/>
    <text x="189" y="87" fill="#444">15.3</text>
    <text x="140" y="108" text-anchor="end" fill="#555">Ranch Riding</text>
    <rect x="150" y="98" width="21" height="16" fill="#d0a65e"/>
    <text x="177" y="111" fill="#444">9.8</text>
    <text x="140" y="132" text-anchor="end" fill="#555">Trail</text>
    <rect x="150" y="122" width="19" height="16" fill="#d0a65e"/>
    <text x="175" y="135" fill="#444">8.7</text>
    <text x="140" y="156" text-anchor="end" fill="#555">Western Riding</text>
    <rect x="150" y="146" width="14" height="16" fill="#d0a65e"/>
    <text x="170" y="159" fill="#444">6.6</text>
    <text x="140" y="180" text-anchor="end" fill="#555">Halter</text>
    <rect x="150" y="170" width="11" height="16" fill="#d0a65e"/>
    <text x="167" y="183" fill="#444">5.2</text>
  </g>
  <text x="150" y="202" fill="#777" font-size="11">Mean scheduled entries per class (green = deepest tiers, tan = mid-pack and smaller)</text>
</svg>

The three-tier structure is clear, and it is much flatter than the earlier cuts of this page suggested:

- **Speed events run deep** — Barrels (74) and Working Western Rail (52) are in a league of their own, with Equitation Over Fences and Cow Work next in the twenties.
- **The pattern and rail classes sit at 6–10.** Trail, Showmanship, Horsemanship, Western Pleasure and Hunter Under Saddle — the disciplines with the *most* classes in the dataset — average fewer than ten horses each. The August version of this table showed these in the mid-teens; the number fell not because fields shrank but because the corpus grew by thousands of small local classes, which dominate by count.
- **Halter is enormous in participation but tiny in field size** — **8,815 classes averaging 5.2 entries**, more classes than any other discipline. That's the structure of halter: hundreds of narrow divisions, few horses in each.
- **The bottom is real too** — Pleasure Driving averages 3.2 entries and Jumping 3.0. A win there is worth having, but it isn't beating a field.

---

## How many horses were actually in the class?

The database now stores the **draw sheets** — the published starting order for each go, with a rider on every line. That gives a second, independent measure of field size, and it is not the same as the schedule's entrycount for the same class:

| Relationship | Classes |
|---|---|
| Draw sheet exactly matches the schedule | 502 |
| Draw sheet **larger** than the schedule | 1,746 |
| Draw sheet **smaller** than the schedule | 301 |

The median absolute disagreement is **4 horses**, but the ninetieth percentile is **32** and the largest is **144**. The big ones are structural, not errors:

- **Drawn-together classes.** Four levels of the All Star Reining Stakes Derby share one 166-rider draw sheet while their schedules say 42, 57, 73 and 75. A draw sheet is a *go*, not a class.
- **Co-sanctioned and combined divisions.** NRHA Novice Horse Level 2 — Open draws 158 against a scheduled 55. The schedule counts *this class*; the draw sheet counts *everyone in the arena*.
- **Schedule entries are intentions.** A scheduled 173-entry reining futurity can draw 51 and place 15.

> **Read the two sections together.** "Deepest class" depends entirely on which of the three numbers you use — scheduled entries, drawn riders, or published placings — and they can differ by a factor of three. The safest statement about the sport's biggest class is the one where all three agree: the 4D Open Barrel Racing at Congress, scheduled 226, drawn **224**, with 15 placings published.

---

## Methodology & caveats

- Classes are those with at least one Combined Judges numeric placing (72,316 classes, 426,597 placings). The scheduled entrycount comes from the show schedule, deduped per class because the schedule holds duplicate rows for some classes. **Both rankings are restricted to classes that actually produced a placing** — the raw schedule also carries 8,549 non-class line items (stall blocks, parking permits, camping passes), and a few of those have larger "entry counts" than any real class. Ranking the schedule unfiltered puts a barn-stall block at 298 on top; that is a data-quality artefact, not a horse show class.
- **40.2% of scheduled classes place fewer riders than they entered** (26,105 of 65,008), and **1,505 classes publish exactly 15 placings** — the scrape ceiling. `Placed` is therefore a floor on the field, never the field itself.
- **The draw-sheet figures cover 2,549 draw sheets** (2,293 of the placed classes have one), the draws that were published and captured. They are a biased sample: big shows publish draws, small ones often don't.
- **Averages depend on which classes are in the database.** Reining averages 15.3 here across 2,206 classes; it averaged 39.0 in the August version across 80. Same discipline, different sample — the change is which shows have been ingested, not the sport.
- **"Deepest in the database" is not "deepest in the sport."** The database covers the shows I've ingested so far, currently dominated by Congress and the championship shows, not every show ever run.

---

*This is one of a series of data articles built on my equine-data results database — a personal AQHA show-results explorer that analyzes every class in the dataset.*
