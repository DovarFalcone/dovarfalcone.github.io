---
layout: post
title: Do Judges Favor Certain Horses? 🧑‍⚖️
subtitle: A look at 55 judges and 3,335 (judge, horse) pairs — the extremes are candidates for a closer look, not verdicts
category: Project
tags: [Project, AQHA, Data Analysis, Horse Show, Judging, Equine]
comments: true
---

# Do Judges Favor Certain Horses?

Judges mostly agree with each other. But when you turn every judge's placings into a single comparable number per (judge, horse) pair — how much better or worse a judge ranks a horse than the horse's average across all judges — a few pairs deviate strongly from the pack.

Across **55 judges and 3,335 (judge, horse) pairs** (each pair appearing at least 5 times), the largest bias is **0.57** in place-percentile units. That's a real signal worth a second look — but with this many comparisons screened at once, some large deviations are expected by chance alone. Treat every row here as **a question worth a closer look, not a statement about any judge or horse**.

*Analysis refreshed Aug 2026 · all figures from the Combined Judges roll-up.*

---

## What the metric means

1. **Normalise within each judge's field.** For every individual judge's row, each horse's placing becomes `place_pct = (place − 1) / (n − 1)` against the field *that judge* ranked — 0.0 is a win, 1.0 is last. This makes judges with different class sizes comparable.
2. **Pair up judge and horse.** For each (judge, horse) pair with ≥ 5 appearances: `judge_avg` is the mean `place_pct` that judge gives the horse; `global_avg` is the horse's mean `place_pct` across all judges.
3. **bias = judge_avg − global_avg.** Negative bias means the judge ranks the horse *better* than its all-judge average; positive means worse. All values are in place-percentile units (0–1).
4. **Sorted by |bias|** — the tables below show the largest deviations, both directions.

> **Look, don't convict.** With 55 judges × 3,335 pairs, hundreds of comparisons are screened at once. Even with zero real favoritism, some pairs will show large deviations by chance alone. The strongest pairs here rest on only 5–9 appearances.

---

## Horses a judge ranks better than the pack

*Negative bias — the judge's mean place percentile for this horse is lower (better) than the horse's all-judge mean. Top by |bias|.*

| Judge | Horse | n | Bias | Judge avg | Global avg |
|---|---|---|---|---|---|
| BAKER; RICK | THE COOKIE CLUB | 6 | **+0.566** | 0.973 | 0.407 |
| BAKER; ELIZABETH M | XTRA WIMPYS CATALYST | 6 | +0.562 | 0.885 | 0.323 |
| SARGENT; BENNIE T | CERTAINLY BEST BAR | 6 | −0.561 | 0.000 | 0.561 |
| Devitt; April | MADE FOR SLEEP | 6 | −0.554 | 0.200 | 0.754 |
| FULLERTON; CLINT J | SHOOTIN THE BREEZE | 9 | −0.546 | 0.019 | 0.564 |
| SMITH; JASON | I GOTT YOU BABE | 6 | −0.530 | 0.000 | 0.530 |
| WILLIS; TRACY L | SHOOTIN THE BREEZE | 6 | −0.504 | 0.061 | 0.564 |
| MCGAULY; CHELE | SHOOTIN THE BREEZE | 9 | −0.480 | 0.084 | 0.564 |

A few things jump out:
- **SHOOTIN THE BREEZE** appears three times in this list — different judges all rank it well below its global average, which is itself a noteworthy pattern (strong horse, or a horse that consistently places well under these judges).
- Several negative-bias pairs have a judge avg of **0.000** — that judge *always* won the horse. With n=6 that's a striking record, and exactly the kind of thing that's interesting to look at more closely.
- The largest raw value is actually **positive** (+0.566, Baker→The Cookie Club): that judge placed the horse a full **0.57 of the field's worth** worse than the horse's average — a big outlier in the *worse* direction.

---

## Judge leniency on maneuver scores

Judges also differ in how generously they score. The figure below is each judge's mean maneuver score versus the global mean of **0.396** (higher scores are better in this sport's scoring, so above the line = more lenient). Judges with the largest differences, shown with n ≥ 1,000:

| Judge | n | Mean score | Diff vs global |
|---|---|---|---|
| Ross; Dean | 1,126 | 0.855 | **+0.459** |
| Grose IV; Theodore W | 3,648 | 0.753 | +0.357 |
| Kunkle; Jennifer L | 2,447 | 0.702 | +0.306 |
| SMITH; JASON | 15,232 | 0.110 | −0.286 |
| Poplin; Bub | 5,863 | 0.122 | −0.274 |
| Luse; Van | 4,579 | 0.065 | −0.331 |

<svg viewBox="0 0 560 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Judge mean maneuver score vs global mean">
  <line x1="90" y1="20" x2="90" y2="160" stroke="#999" stroke-width="1"/>
  <text x="90" y="176" text-anchor="middle" fill="#777" font-size="11">0</text>
  <text x="90" y="16" text-anchor="middle" fill="#777" font-size="11">global mean</text>
  <g font-size="11">
    <text x="80" y="44" text-anchor="end" fill="#555">Ross; Dean</text>
    <rect x="90"  y="32" width="196" height="18" fill="#6a9e78"/>
    <text x="292" y="46" fill="#444">+0.459</text>
    <text x="80" y="70" text-anchor="end" fill="#555">Grose IV</text>
    <rect x="90"  y="58" width="152" height="18" fill="#6a9e78"/>
    <text x="248" y="72" fill="#444">+0.357</text>
    <text x="80" y="96" text-anchor="end" fill="#555">Kunkle; Jennifer</text>
    <rect x="90"  y="84" width="130" height="18" fill="#6a9e78"/>
    <text x="226" y="98" fill="#444">+0.306</text>
    <text x="80" y="122" text-anchor="end" fill="#555">SMITH; JASON</text>
    <rect x="90"  y="110" width="122" height="18" fill="#d0a65e"/>
    <text x="84" y="124" fill="#444">−0.286</text>
    <text x="80" y="148" text-anchor="end" fill="#555">Poplin; Bub</text>
    <rect x="90"  y="136" width="117" height="18" fill="#d0a65e"/>
    <text x="84" y="150" fill="#444">−0.274</text>
  </g>
</svg>

Judges with means **above** the global line (green, positive diff) are **more lenient** — they award higher scores than the field average; judges **below** it (tan, negative) are **harsher**. Sample sizes vary widely (from ~1,100 to ~15,000), so the biggest-n judges are the most trustworthy comparisons. Judge leniency is about *scoring level*, which is separate from the per-horse bias tables above.

---

## What's not here

- **Trainer data is too sparse** for conclusions — only 7.8% of class-placing rows carry a trainer name — so no trainer table is reported.
- **Owner data** is available but was left out to keep this focused; the metric is identical if it's ever wanted.

---

*This is one of a series of data articles built on my equine-data results database — a personal AQHA show-results explorer that analyzes every class in the dataset.*
