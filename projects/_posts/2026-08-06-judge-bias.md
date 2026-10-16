---
layout: post
title: Do Judges Favor Certain Horses?
subtitle: What bias actually looks like across 68,059 (judge, horse) pairs — where it shows up, and what it can teach us
category: Project
tags: [Project, AQHA, Data Analysis, Horse Show, Judging, Equine]
comments: true
---

# Do Judges Favor Certain Horses?

Judges mostly agree with each other. But when you turn every judge's placings into a single comparable number per (judge, horse) pair — how much better or worse a judge ranks a horse than the horse's average across all judges — a few pairs deviate strongly from the pack.

This article is about **whether** that bias exists, **how it shows itself**, and **what we can learn from it** — so every figure below is anonymized. No judges, horses, or exhibitors are named; the focus is entirely on the patterns in the data.

Across **68,059 (judge, horse) pairs** (each appearing at least 5 times, drawn from **781 judges**), the largest bias is **0.737** in place-percentile units. That's a real signal worth a second look — but with this many comparisons screened at once, some large deviations are expected by chance alone. The goal here is to understand the shape of the phenomenon, not to single anyone out.

*Analysis refreshed 16 October 2026 · all figures from the Combined Judges roll-up, computed fresh from the production database.*

> **Updated 16 October 2026 — the corpus grew eightfold and the metric was fixed.** This page previously reported 8,145 pairs from 142 judges. The database now holds roughly 8× that judging detail, and re-running the analysis surfaced a real defect in how places were normalised: when too few rows were captured for a judge in one class, the divisor used to turn a place into a percentile was too small, which pushed some pairs above the 0–1 range entirely and inflated the extremes. Every figure below is recomputed on the corrected normalisation. The headline finding is unchanged — but the tail is now measured against a defensible denominator, and the scoring-level section has been rebuilt to compare judges **within a discipline** rather than across all of them.

---

## What the metric means

1. **Normalise within each judge's field.** For every individual judge's row, each horse's placing becomes `place_pct = (place − 1) / (n − 1)` against the field *that judge* ranked — 0.0 is a win, 1.0 is last. This makes judges with different class sizes comparable.
2. **Pair up judge and horse.** For each (judge, horse) pair with ≥ 5 appearances: `judge_avg` is the mean `place_pct` that judge gives the horse; `global_avg` is the horse's mean `place_pct` across all judges.
3. **bias = judge_avg − global_avg.** Negative bias means the judge ranks the horse *better* than its all-judge average; positive means worse. All values are in place-percentile units (0–1).

**One correction matters here.** The scraper caps how many placings it captures per class — often the top 15 rows, even in a class of 200. That means a judge can have, say, ten captured rows in a class where their highest recorded placing is 52. Normalising against "the number of rows I happen to have for this judge" would then produce a percentile far outside 0–1. So the denominator used below is the **class's own placing count from the Combined Judges roll-up**, and any per-judge row whose place falls outside `1 … that count` is discarded as unusable. That discards **43,968 of 1,018,114 per-judge rows (4.32%)** — the ones the scrape cut off mid-class — and it is why the extremes reported here are smaller and better behaved than earlier versions of this page.

---

## Does bias exist? The shape of the distribution

The honest answer is: **only a little, and only in a thin tail.** The typical pair is nearly unbiased — the mean absolute bias is just **0.103**, half of all pairs sit below **0.082**, and **90%** fall below **0.220** place-percentile points. Bias of that size is noise-level.

It's the tail that matters:

| Threshold | Pairs exceeding it | Share of all 68,059 |
|---|---|---|
| \|bias\| ≥ 0.20 | 8,931 | 13.1% |
| \|bias\| ≥ 0.30 | 2,209 | 3.25% |
| \|bias\| ≥ 0.40 | 433 | 0.64% |
| \|bias\| ≥ 0.50 | 63 | 0.09% |

So roughly **one pair in a thousand** deviates by half the field's worth or more. Bias is not endemic; it's a rare, isolated signal hiding in a mostly-fair distribution, and the shape of that distribution barely moves as the database grows — 13.1% of pairs cleared 0.20 when this page reported 8,145 pairs, and 13.1% clear it now at 68,059. That stability is itself the most useful finding: **systematic favoritism is not the norm.**

<svg viewBox="0 0 560 130" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Share of pairs exceeding bias thresholds, 68059 pairs">
  <line x1="60" y1="95" x2="500" y2="95" stroke="#888" stroke-width="1"/>
  <g font-size="11" text-anchor="middle">
    <text x="130" y="24" fill="#444">13.1%</text>
    <rect x="100" y="30" width="60" height="60" fill="#d0a65e"/>
    <text x="130" y="82" fill="#444">≥ 0.20</text>
    <text x="250" y="24" fill="#444">3.25%</text>
    <rect x="220" y="60" width="60" height="25" fill="#e0c07a"/>
    <text x="250" y="82" fill="#444">≥ 0.30</text>
    <text x="370" y="24" fill="#444">0.64%</text>
    <rect x="340" y="72" width="60" height="10" fill="#c0392b"/>
    <text x="370" y="82" fill="#444">≥ 0.40</text>
  </g>
  <text x="60" y="122" fill="#777" font-size="11">Share of the 68,059 pairs exceeding each |bias| threshold (area ∝ share); only 63 pairs (0.09%) clear 0.50</text>
</svg>

---

## How bias shows itself

Two patterns stand out in the extreme tail. Neither names anyone — both are worth understanding.

**1. The "always wins together" pattern.** Of the 68,059 pairs, **400** are cases where a judge's average placing for a specific horse is exactly **0.000** — that judge *won* that horse every single time they were in the same class together. At the other end, **137** pairs sit at exactly **1.000**: the judge placed that horse last every time. Those two groups are 0.59% and 0.20% of all pairs. In this metric they are the strongest possible expression of an alignment — a judge's ordering of that horse that never once disagreed with the winner's circle, or with the back of it.

**2. Bias cuts both ways, and the far edge is the "worse" side.** Of the 100 largest absolute deviations, **58 point the worse direction** (the judge ranks the horse below its all-judge average) and **42 point the better one**. The single largest value in the whole dataset is **+0.737** — a judge placing one horse about three-quarters of the field below its all-judge average — against **−0.655** at the favourable end. Bias is not just "favoring a horse"; it can equally mean a judge who systematically marks one down.

> **Look, don't convict.** With 781 judges and 68,059 (judge, horse) pairs, tens of thousands of comparisons are screened at once, and the median pair in that extreme tail rests on only **6 appearances** (the range among the top 100 is 5–9). Even with zero real favoritism, some pairs will show large deviations by chance alone. Treat every row as a question worth a closer look — not as a statement about any judge or horse. A judge who places the same horse at the top of a class repeatedly may simply be reading the same quality the other judges also see.

---

## How much do judges differ in scoring level?

Separate from per-horse bias is raw scoring generosity. The database now holds **10,306,088 scored maneuver observations** across **43 disciplines**, with a global mean maneuver score of **0.329**. The question "do judges differ in level?" is real — but it has to be asked *inside* a discipline, because the scoring scale is not comparable between them:

| Discipline | Mean maneuver score | Maneuvers |
|---|---|---|
| Showmanship | 0.534 | 1,576,226 |
| Horsemanship | 0.446 | 375,738 |
| Trail | 0.378 | 2,658,662 |
| Ranch Trail | 0.329 | 1,242,924 |
| Hunt Seat Equitation | 0.314 | 229,267 |
| Ranch Riding | 0.245 | 2,533,788 |
| Western Riding | 0.236 | 593,319 |
| Ranch Pleasure | 0.189 | 104,118 |
| Reining | 0.009 | 538,206 |

A Reining judge averaging 0.009 is not being stingy — reining maneuvers are simply scored on a different scale from showmanship maneuvers. Comparing raw scores across disciplines is meaningless, so the chart below measures each judge *against their own discipline's mean*, over the **3,109 (judge, discipline) cells** with at least 200 scored maneuvers each (659 judges):

<svg viewBox="0 0 560 170" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Judge scoring level relative to own discipline mean, 3109 judge-discipline cells">
  <line x1="60" y1="120" x2="500" y2="120" stroke="#888" stroke-width="1"/>
  <line x1="196" y1="100" x2="196" y2="140" stroke="#999" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="196" y="154" text-anchor="middle" fill="#777" font-size="11">discipline mean (0)</text>
  <g stroke="#444" stroke-width="2">
    <line x1="70" y1="95" x2="150" y2="95"/>
    <line x1="150" y1="80" x2="222" y2="80" stroke-width="4"/>
    <line x1="222" y1="95" x2="430" y2="95"/>
    <line x1="70" y1="75" x2="70" y2="115"/>
    <line x1="150" y1="75" x2="150" y2="115"/>
    <line x1="222" y1="75" x2="222" y2="115"/>
    <line x1="430" y1="75" x2="430" y2="115"/>
  </g>
  <g fill="#555" font-size="11" text-anchor="middle">
    <text x="70"  y="56">p10 −0.334</text>
    <text x="150" y="56">Q1 −0.226</text>
    <text x="196" y="56">median −0.094</text>
    <text x="260" y="44">Q3 +0.042</text>
    <text x="430" y="56">p90 +0.176</text>
  </g>
  <text x="60" y="32" fill="#555" font-size="12">Judge mean maneuver score minus their discipline's mean, 3,109 judge×discipline cells</text>
</svg>

Key takeaways:

- **Most judges sit within about a quarter-point of their discipline.** Half the cells fall between **−0.226 and +0.042**, and **68.1%** of them sit below their discipline's mean — the mildly harsher side is the crowded one.
- **The extremes are mostly a units problem, not a judging problem.** The widest cell on the favourable side sits **+2.87** above its discipline mean while the harshest sits **−0.81** below. A +2.87 deviation on a scale whose discipline mean is 0.378 is not a judge being generous; it is a judge (or a results feed) recording something on a different basis. The robust summary above — median and quartiles — is the part worth trusting.
- **What it means for a class.** If a horse's score depends partly on *which* judge marks it, and it does, to the tune of a quarter-point for a typical judge, then comparing raw scores *across different judges' classes* is unreliable. This is why all the bias figures in this article normalise within each judge's field rather than comparing raw scores directly.

---

## What we can learn from this

1. **Favoritism is rare, not pervasive.** The typical (judge, horse) pair is essentially unbiased (mean |bias| 0.103), and the share of pairs in the tail is **stable as the dataset grows** — 13.1% above |bias| 0.20 both before and after an eightfold increase in data. That is what you'd expect if the extremes are properties of specific pairs rather than of judging in general.
2. **When it does show up, it's extreme and specific.** The signal lives in a thin tail — a few hundred pairs where a judge repeatedly wins (or repeatedly sinks) a particular horse, almost all resting on 5–9 meetings. These are the cases worth a closer look, and they're identifiable because they're so far from the pack.
3. **Scoring level is a real, separate effect — and it must be measured within a discipline.** Judges differ in level by roughly ±0.2 around their discipline's mean, which is enough to make raw cross-judge score comparisons apples-to-oranges. Within-judge normalisation is the honest way to measure *relative* performance.
4. **Bias is direction-neutral.** The largest deviation is a judge marking a horse *down* (+0.737), not up (the largest favourable deviation is −0.655). "Bias" in judging isn't only about favoritism — it can be the opposite.
5. **The metric had a real defect worth knowing about.** 4.3% of per-judge rows cannot be placed on a 0–1 scale at all, because the scrape captured only part of a class for that judge. Any analysis of judging that ignores the class's true size will produce deviations that look dramatic and mean nothing.

---

## What's not here

- **Trainer data is too sparse** for conclusions — only a small share of class-placing rows carry a trainer name — so no trainer analysis is reported.
- **Owner and exhibitor-level analyses** exist but are deliberately omitted to keep this article focused on the anonymized patterns rather than on individuals.

---

*This is one of a series of data articles built on my equine-data results database — a personal AQHA show-results explorer that analyzes every class in the dataset.*
