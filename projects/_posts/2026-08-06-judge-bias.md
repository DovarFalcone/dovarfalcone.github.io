---
layout: post
title: Do Judges Favor Certain Horses? 🧑‍⚖️
subtitle: What bias actually looks like across 8,145 (judge, horse) pairs — where it shows up, and what it can teach us
category: Project
tags: [Project, AQHA, Data Analysis, Horse Show, Judging, Equine]
comments: true
---

# Do Judges Favor Certain Horses?

Judges mostly agree with each other. But when you turn every judge's placings into a single comparable number per (judge, horse) pair — how much better or worse a judge ranks a horse than the horse's average across all judges — a few pairs deviate strongly from the pack.

This article is about **whether** that bias exists, **how it shows itself**, and **what we can learn from it** — so every figure below is anonymized. No judges, horses, or exhibitors are named; the focus is entirely on the patterns in the data.

Across **8,145 (judge, horse) pairs** (each appearing at least 5 times, drawn from **142 judges**), the largest bias is **0.675** in place-percentile units. That's a real signal worth a second look — but with this many comparisons screened at once, some large deviations are expected by chance alone. The goal here is to understand the shape of the phenomenon, not to single anyone out.

*Analysis refreshed 22 Sept 2026 · all figures from the Combined Judges roll-up.*

> **Updated 27 September 2026.** The first cut of this analysis (August 2026) covered 3,335 pairs from ~55 judges with a largest deviation of 0.57. Ingesting more shows took it to 8,145 pairs across 142 judges, and the pattern held: the typical pair is still essentially unbiased, the tail stayed proportional (11.4% of pairs above |bias| 0.20 then, **13.1%** now), and the spread between the most lenient and harshest judge widened from ~0.8 score points to **2.06**. The per-judge scoring-spread section is the part that changed most — read it before drawing conclusions about any individual.

---

## What the metric means

1. **Normalise within each judge's field.** For every individual judge's row, each horse's placing becomes `place_pct = (place − 1) / (n − 1)` against the field *that judge* ranked — 0.0 is a win, 1.0 is last. This makes judges with different class sizes comparable.
2. **Pair up judge and horse.** For each (judge, horse) pair with ≥ 5 appearances: `judge_avg` is the mean `place_pct` that judge gives the horse; `global_avg` is the horse's mean `place_pct` across all judges.
3. **bias = judge_avg − global_avg.** Negative bias means the judge ranks the horse *better* than its all-judge average; positive means worse. All values are in place-percentile units (0–1).

---

## Does bias exist? The shape of the distribution

The honest answer is: **only a little, and only in a thin tail.** The typical pair is nearly unbiased — the mean absolute bias is just **0.102**, half of all pairs sit below **0.08**, and **90%** fall below **0.224** place-percentile points. Bias of that size is noise-level.

It's the tail that matters:

| Threshold | Pairs exceeding it | Share of all 8,145 |
|---|---|---|
| \|bias\| ≥ 0.20 | 1,071 | 13.1% |
| \|bias\| ≥ 0.30 | 318 | 3.9% |
| \|bias\| ≥ 0.40 | 77 | 0.9% |
| \|bias\| ≥ 0.50 | 19 | 0.23% |

So roughly **one pair in four hundred** deviates by half the field's worth or more. Bias is not endemic; it's a rare, isolated signal hiding in a mostly-fair distribution, and that distribution's shape barely moves as the database grows. That is itself the most useful finding: **systematic favoritism is not the norm.**

<svg viewBox="0 0 560 130" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Share of pairs exceeding bias thresholds, 8145 pairs">
  <line x1="60" y1="95" x2="500" y2="95" stroke="#888" stroke-width="1"/>
  <g font-size="11" text-anchor="middle">
    <text x="130" y="24" fill="#444">13.1%</text>
    <rect x="100" y="30" width="60" height="60" fill="#d0a65e"/>
    <text x="130" y="82" fill="#444">≥ 0.20</text>
    <text x="250" y="24" fill="#444">3.9%</text>
    <rect x="220" y="60" width="60" height="30" fill="#e0c07a"/>
    <text x="250" y="82" fill="#444">≥ 0.30</text>
    <text x="370" y="24" fill="#444">0.9%</text>
    <rect x="340" y="75" width="60" height="15" fill="#c0392b"/>
    <text x="370" y="82" fill="#444">≥ 0.40</text>
  </g>
  <text x="60" y="122" fill="#777" font-size="11">Share of the 8,145 pairs exceeding each |bias| threshold (area ∝ share); only 19 pairs (0.23%) clear 0.50</text>
</svg>

---

## How bias shows itself

Two patterns stand out in the extreme tail. Neither names anyone — both are worth understanding.

**1. The "always wins together" pattern.** Of the 8,145 pairs, **89** are cases where a judge's average placing for a specific horse is exactly **0.000** — that judge *won* that horse every single time they were in the same class together, a record of 5–6 meetings. In rate terms that's about 1.1% of pairs — and it is the strongest possible expression of bias in this metric, because it means a judge's ordering of that horse never once disagreed with the winner's circle. If you were a judge, this is the profile you'd want to understand about yourself.

**2. Bias cuts both ways.** The largest raw deviations are split between judges who rank a horse *much better* than its average (negative bias, down to **−0.600**) and those who rank it *much worse* (positive bias, up to **+0.675**). In fact the single largest value in the whole dataset is in the **worse** direction — a judge placing one horse about two-thirds of the field lower than its all-judge average. Bias is not just "favoring a horse"; it can equally mean a judge who systematically marks one down.

> **Look, don't convict.** With 142 judges × 8,145 (judge, horse) pairs, hundreds of comparisons are screened at once. Even with zero real favoritism, some pairs will show large deviations by chance alone. The strongest pairs here rest on only 5–7 appearances, so treat every row as a question worth a closer look — not as a statement about any judge or horse. A judge who places the same horse at the top of a class repeatedly may simply be reading the same quality the other judges also see.

---

## How much do judges differ in scoring level?

Separate from per-horse bias is raw scoring generosity. Judges vary in how high they score on average — the global mean maneuver score is **0.376** (1,896,539 scored maneuver observations behind it), and the 127 judges with enough maneuver-score rows spread widely around it:

<svg viewBox="0 0 560 160" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Distribution of judge scoring generosity relative to global mean, 127 judges">
  <line x1="60" y1="120" x2="500" y2="120" stroke="#888" stroke-width="1"/>
  <line x1="188" y1="100" x2="188" y2="140" stroke="#999" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="188" y="152" text-anchor="middle" fill="#777" font-size="11">global mean (0)</text>
  <g stroke="#444" stroke-width="2">
    <line x1="62" y1="95" x2="166" y2="95"/>
    <line x1="166" y1="80" x2="210" y2="80" stroke-width="4"/>
    <line x1="210" y1="95" x2="495" y2="95"/>
    <line x1="62" y1="75" x2="62" y2="115"/>
    <line x1="166" y1="75" x2="166" y2="115"/>
    <line x1="210" y1="75" x2="210" y2="115"/>
    <line x1="495" y1="75" x2="495" y2="115"/>
    <line x1="188" y1="70" x2="188" y2="90" stroke="#c0392b"/>
  </g>
  <g fill="#555" font-size="11" text-anchor="middle">
    <text x="62"  y="56">min −0.590</text>
    <text x="166" y="56">Q1 −0.093</text>
    <text x="188" y="56">median +0.010</text>
    <text x="210" y="44">Q3 +0.115</text>
    <text x="495" y="56">max +1.474</text>
  </g>
  <text x="60" y="34" fill="#555" font-size="12">Judge mean maneuver score minus global mean, 127 judges (anonymized)</text>
</svg>

This is a box-whisker of how far each judge's average maneuver score sits from the global mean. Key takeaways:

- **The median judge is essentially at the global mean** (+0.010), and half of all judges sit within about **−0.09 to +0.12** of it. Most judges score at a similar level — 61 below the mean, 66 above.
- **The extremes are the story, and they got longer.** The most lenient judge scores **+1.474** above the global mean while the harshest sits **−0.590** below it — a spread of **2.06** score points between the two ends of the judging panel, and the top end is a long way out on its own (the next most lenient judges sit near +1.4 and +0.6).
- **A handful of outliers, not a spectrum.** With more judges in the pool the middle barely moved; the tails stretched. That asymmetry — two or three very high-scoring judges against a longer, gentler harsher side — is the shape to keep an eye on.

> **What this means for a class:** if a horse's score depends partly on *which* judge marks it — and it does, to the tune of up to ~1.5 points for the most extreme judges — then comparing raw scores *across different judges' classes* is unreliable. This is why all the bias figures in this article normalise within each judge's field rather than comparing raw scores directly.

---

## What we can learn from this

1. **Favoritism is rare, not pervasive.** The typical (judge, horse) pair is essentially unbiased (mean |bias| 0.102), and the share of pairs in the tail barely moved as the dataset grew from 3,335 pairs to 8,145 — 11.4% to 13.1% above |bias| 0.20, 3.6% to 3.9% above 0.30. Bias rates are stable as more results come in, which is what you'd expect if the extremes are properties of specific pairs rather than of judging in general.
2. **When it does show up, it's extreme and specific.** The signal lives in a thin tail — a handful of pairs where a judge repeatedly wins (or repeatedly sinks) a particular horse. These are the cases worth a closer look, and they're identifiable because they're so far from the pack.
3. **Scoring level is a real, separate effect that widened with more data.** Judges differ in overall generosity by up to ~2 points at the extremes, so raw cross-judge score comparisons are apples-to-oranges. Within-judge normalisation is the honest way to measure *relative* performance.
4. **Bias is direction-neutral.** The largest deviation is a judge marking a horse *down* (+0.675), not up (the largest favorable deviation is −0.600). "Bias" in judging isn't only about favoritism — it can be the opposite.

---

## What's not here

- **Trainer data is too sparse** for conclusions — only 7.8% of class-placing rows carry a trainer name — so no trainer analysis is reported.
- **Owner and exhibitor-level analyses** exist (the exhibitor version of this metric spans 8,847 pairs) but are deliberately omitted to keep this article focused on the anonymized patterns rather than on individuals.

---

*This is one of a series of data articles built on my equine-data results database — a personal AQHA show-results explorer that analyzes every class in the dataset.*
