---
layout: post
title: Do Judges Favor Certain Horses? 🧑‍⚖️
subtitle: What bias actually looks like across 3,335 (judge, horse) pairs — where it shows up, and what it can teach us
category: Project
tags: [Project, AQHA, Data Analysis, Horse Show, Judging, Equine]
comments: true
---

# Do Judges Favor Certain Horses?

Judges mostly agree with each other. But when you turn every judge's placings into a single comparable number per (judge, horse) pair — how much better or worse a judge ranks a horse than the horse's average across all judges — a few pairs deviate strongly from the pack.

This article is about **whether** that bias exists, **how it shows itself**, and **what we can learn from it** — so every figure below is anonymized. No judges, horses, or exhibitors are named; the focus is entirely on the patterns in the data.

Across **3,335 (judge, horse) pairs** (each appearing at least 5 times, drawn from ~55 judges), the largest bias is **0.57** in place-percentile units. That's a real signal worth a second look — but with this many comparisons screened at once, some large deviations are expected by chance alone. The goal here is to understand the shape of the phenomenon, not to single anyone out.

*Analysis refreshed Aug 2026 · all figures from the Combined Judges roll-up.*

---

## What the metric means

1. **Normalise within each judge's field.** For every individual judge's row, each horse's placing becomes `place_pct = (place − 1) / (n − 1)` against the field *that judge* ranked — 0.0 is a win, 1.0 is last. This makes judges with different class sizes comparable.
2. **Pair up judge and horse.** For each (judge, horse) pair with ≥ 5 appearances: `judge_avg` is the mean `place_pct` that judge gives the horse; `global_avg` is the horse's mean `place_pct` across all judges.
3. **bias = judge_avg − global_avg.** Negative bias means the judge ranks the horse *better* than its all-judge average; positive means worse. All values are in place-percentile units (0–1).

---

## Does bias exist? The shape of the distribution

The honest answer is: **only a little, and only in a thin tail.** The typical pair is nearly unbiased — the mean absolute bias is just **0.10**, and **90%** of pairs fall below **0.21** place-percentile points. Bias of that size is noise-level.

It's the tail that matters:

| Threshold | Pairs exceeding it | Share of all 3,335 |
|---|---|---|
| \|bias\| ≥ 0.20 | 379 | 11% |
| \|bias\| ≥ 0.30 | 119 | 3.6% |
| \|bias\| ≥ 0.40 | 25 | 0.7% |
| \|bias\| ≥ 0.50 | 4 | 0.1% |

So roughly **one pair in a hundred** deviates by half the field's worth or more — and a handful exceed that. Bias is not endemic; it's a rare, isolated signal hiding in a mostly-fair distribution. That is itself the most useful finding: **systematic favoritism is not the norm.**

<svg viewBox="0 0 560 120" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Share of pairs exceeding bias thresholds">
  <line x1="60" y1="95" x2="500" y2="95" stroke="#888" stroke-width="1"/>
  <g font-size="11" text-anchor="middle">
    <text x="130" y="24" fill="#444">11%</text>
    <rect x="100" y="30" width="60" height="60" fill="#d0a65e"/>
    <text x="130" y="82" fill="#444">≥ 0.20</text>
    <text x="250" y="24" fill="#444">3.6%</text>
    <rect x="220" y="56" width="60" height="34" fill="#e0c07a"/>
    <text x="250" y="82" fill="#444">≥ 0.30</text>
    <text x="370" y="24" fill="#444">0.7%</text>
    <rect x="340" y="76" width="60" height="14" fill="#c0392b"/>
    <text x="370" y="82" fill="#444">≥ 0.40</text>
  </g>
  <text x="60" y="112" fill="#777" font-size="11">Share of the 3,335 pairs exceeding each |bias| threshold (area ∝ share)</text>
</svg>

---

## How bias shows itself

Two patterns stand out in the extreme tail. Neither names anyone — both are worth understanding.

**1. The "always wins together" pattern.** Of the 3,335 pairs, **18** are cases where a judge's average placing for a specific horse is exactly **0.000** — that judge *won* that horse every single time they were in the same class together, a record of 5–6 meetings. Statistically, repeatedly winning the same horse is the strongest possible expression of bias in this metric, and it appears far more often than chance would predict. If you were a judge, this is the profile you'd want to understand about yourself.

**2. Bias cuts both ways.** The largest raw deviations are split between judges who rank a horse *much better* than its average (negative bias) and those who rank it *much worse* (positive bias). In fact the single largest value in the whole dataset is in the **worse** direction — one pair deviating a full **0.57** of the field's worth below the horse's normal placing. Bias is not just "favoring a horse"; it can equally mean a judge who systematically marks one down.

> **Look, don't convict.** Even with zero real favoritism, some pairs will show large deviations by chance alone. The strongest pairs rest on only 5–9 appearances, and a judge who places the same horse at the top of a class repeatedly may simply be reading the same quality the other judges also see. The patterns above are directions to investigate, not verdicts on anyone.

---

## How much do judges differ in scoring level?

Separate from per-horse bias is raw scoring generosity. Judges vary in how high they score on average — the global mean maneuver score is **0.396**, and individual judges spread around it. Across the judges in the dataset:

<svg viewBox="0 0 560 160" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Distribution of judge scoring generosity relative to global mean">
  <line x1="60" y1="120" x2="500" y2="120" stroke="#888" stroke-width="1"/>
  <line x1="255" y1="100" x2="255" y2="140" stroke="#999" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="255" y="152" text-anchor="middle" fill="#777" font-size="11">global mean (0)</text>
  <g stroke="#444" stroke-width="2">
    <line x1="93" y1="95" x2="201" y2="95"/>
    <line x1="201" y1="80" x2="313" y2="80" stroke-width="4"/>
    <line x1="313" y1="95" x2="479" y2="95"/>
    <line x1="93" y1="75" x2="93" y2="115"/>
    <line x1="201" y1="75" x2="201" y2="115"/>
    <line x1="313" y1="75" x2="313" y2="115"/>
    <line x1="479" y1="75" x2="479" y2="115"/>
    <line x1="245" y1="70" x2="245" y2="90" stroke="#c0392b"/>
  </g>
  <g fill="#555" font-size="11" text-anchor="middle">
    <text x="93"  y="56">min −0.331</text>
    <text x="201" y="56">Q1 −0.111</text>
    <text x="245" y="56">median −0.020</text>
    <text x="313" y="56">Q3 +0.119</text>
    <text x="479" y="56">max +0.459</text>
  </g>
  <text x="60" y="34" fill="#555" font-size="12">Distribution of judge mean score minus global mean (box-whisker, anonymized)</text>
</svg>

This is a box-whisker of how far each judge's average maneuver score sits from the global mean. Key takeaways:

- **The median judge is essentially at the global mean** (−0.020), and half of all judges sit within about **−0.11 to +0.12** of it. Most judges score at a similar level.
- **The extremes are the story.** The most lenient judge scores **+0.459** above the global mean while the harshest sits **−0.331** below it — a spread of nearly **0.8** score points between the two ends of the judging panel.
- There are more judges below the mean (harsher) than above it, but the single biggest swing is on the lenient side.

> **What this means for a class:** if a horse's score depends partly on *which* judge marks it — and it does, to the tune of up to ~0.5 points for the most extreme judges — then comparing raw scores *across different judges' classes* is unreliable. This is why all the bias figures in this article normalise within each judge's field rather than comparing raw scores directly.

---

## What we can learn from this

1. **Favoritism is rare, not pervasive.** The typical (judge, horse) pair is essentially unbiased. Any suggestion that judging is broadly biased is not supported by the data.
2. **When it does show up, it's extreme and specific.** The signal lives in a thin tail — a handful of pairs where a judge repeatedly wins (or repeatedly sinks) a particular horse. These are the cases worth a closer look, and they're identifiable because they're so far from the pack.
3. **Scoring level is a real, separate effect.** Judges differ in overall generosity by up to ~0.5 points, so raw cross-judge score comparisons are apples-to-oranges. Within-judge normalisation is the honest way to measure *relative* performance.
4. **Bias is direction-neutral.** The largest deviation is a judge marking a horse *down*, not up. "Bias" in judging isn't only about favoritism — it can be the opposite.

---

## What's not here

- **Trainer data is too sparse** for conclusions — only 7.8% of class-placing rows carry a trainer name — so no trainer analysis is reported.
- **Owner and exhibitor-level analyses** exist but are deliberately omitted to keep this article focused on the anonymized patterns rather than on individuals.

---

*This is one of a series of data articles built on my equine-data results database — a personal AQHA show-results explorer that analyzes every class in the dataset.*
