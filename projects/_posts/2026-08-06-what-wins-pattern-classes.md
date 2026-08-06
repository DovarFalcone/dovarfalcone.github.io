---
layout: post
title: Where Pattern Classes Are Won — and Where They're Lost 📋
subtitle: The maneuvers that separate placers 1–3 from the field, and the penalties that actually lose classes
category: Project
tags: [Project, AQHA, Data Analysis, Horse Show, Equine]
comments: true
---

# Where Pattern Classes Are Won — and Where They're Lost

Every pattern class comes down to a handful of maneuvers. Which ones actually separate the top three from the field — and which ones quietly cost riders the class through penalties?

Across **424 (discipline, maneuver) buckets** with at least 20 scored riders, the single largest gap between placers 1–3 and the field is **"180, B, 540" in Showmanship**: the top three average **+1.52** points on it while the rest of the field averages **−0.39** — a **+1.91-point spread** where the winners cleanly outscore everyone else.

The tables below show every discipline's strongest maneuvers in both directions, plus the penalty rates that decide where classes are actually lost.

*Based on 86,281 placings · 1,080,007 scores · analysis refreshed Aug 2026.*

---

## Where pattern classes are won

For every scored rider (one show-class-exhibitor-maneuver observation; the score is the mean across that rider's judges), here's the maneuver score of placers 1–3 vs everyone else. Positive gaps mean the top three outscore the field on that maneuver; negative gaps mean they score *below* it. Top by |gap|:

| Maneuver | Discipline | Top 3 avg | Field avg | Diff | n |
|---|---|---|---|---|---|
| 180, B, 540 | Showmanship | 1.52 | −0.39 | **+1.91** | 102 |
| S, 540L, B, 540R | Horsemanship | 1.27 | −0.25 | +1.52 | 116 |
| 135, W | Showmanship | 1.67 | 0.28 | +1.38 | 102 |
| RL, HG, RL | Hunt Seat Equitation | 1.29 | 0.02 | +1.27 | 172 |
| LL | Horsemanship | 1.50 | 0.29 | +1.21 | 99 |
| RL | Horsemanship | 1.30 | 0.22 | +1.08 | 291 |
| S, B, 90 L | Horsemanship | 0.94 | −0.14 | +1.08 | 87 |
| 360 | Showmanship | 1.03 | −0.03 | +1.07 | 66 |
| 2 PT, Sit T | Hunt Seat Equitation | 1.33 | 0.27 | +1.06 | 172 |
| RL | Hunt Seat Equitation | 1.30 | 0.25 | +1.05 | 138 |

The pattern is striking: **Showmanship and Horsemanship** dominate the top of the list, and the biggest gaps are all on **turning maneuvers** (540s, 360s, 180s) — the technical, pattern-heavy work where the top riders pull ahead. `n` is the number of scored riders behind the bucket (placers 1–3 plus field).

---

## Where classes are lost

Penalty rates per (discipline, maneuver) — the share of riders who drew at least one penalty, and the mean penalty size among those who did. A rider is penalized when any of its judges' penalties is nonzero. Shown for buckets with n ≥ 200:

| Maneuver | Discipline | Penalized | Total | Rate | Avg penalty |
|---|---|---|---|---|---|
| Jog | Trail | 217 | 335 | **65%** | 0.42 |
| JOG POLES | Trail | 260 | 443 | 59% | 0.47 |
| RL, LOs | Trail | 124 | 231 | 54% | 0.42 |
| LL Logs | Ranch Trail | 194 | 396 | 49% | **2.32** |
| JOG | Trail | 105 | 216 | 49% | 0.70 |
| W, 360, W | Trail | 360 | 738 | 49% | 1.08 |
| WOs | Trail | 529 | 1,074 | 49% | 0.90 |
| J, JOs | Trail | 525 | 1,150 | 46% | 0.51 |

**Trail dominates the penalty story.** Over half of riders penalize on the basic Jog and JOG POLES — the most common maneuvers in the sport's most penalty-heavy discipline. The largest average penalty (**2.32** on Ranch Trail's LL Logs) is nearly double the next biggest, which is exactly the kind of maneuver that can sink a class in one stride.

<svg viewBox="0 0 560 170" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Penalty rate by maneuver">
  <line x1="150" y1="16" x2="150" y2="132" stroke="#999" stroke-width="1"/>
  <g font-size="11">
    <text x="140" y="36" text-anchor="end" fill="#555">Jog</text>
    <rect x="150" y="26" width="120" height="18" fill="#d0a65e"/>
    <text x="276" y="40" fill="#444">65%</text>
    <text x="140" y="62" text-anchor="end" fill="#555">JOG POLES</text>
    <rect x="150" y="52" width="109" height="18" fill="#d0a65e"/>
    <text x="265" y="66" fill="#444">59%</text>
    <text x="140" y="88" text-anchor="end" fill="#555">RL, LOs</text>
    <rect x="150" y="78" width="100" height="18" fill="#d0a65e"/>
    <text x="256" y="92" fill="#444">54%</text>
    <text x="140" y="114" text-anchor="end" fill="#555">LL Logs</text>
    <rect x="150" y="104" width="91" height="18" fill="#6a9e78"/>
    <text x="247" y="118" fill="#444">49% · avg 2.32</text>
  </g>
  <text x="150" y="150" fill="#777" font-size="11">% of riders penalized (tan = Trail, green = Ranch Trail)</text>
</svg>

---

## Methodology & caveats

**How it's measured:**
1. **Rider-level observations.** Scoresheet rows are duplicated per (exhibitor, judge, maneuver), so each rider's maneuver score is the mean across that rider's judges before anything is compared.
2. **Top vs field.** The rider's place comes from the Combined Judges roll-up for the same class; placers 1–3 are the "top" group and everyone else is the field. The gap is `avg_top − avg_field`.
3. **Buckets.** (discipline, maneuver) pairs are joined through a deduped discipline map. A bucket is reported only with ≥ 20 scored riders — 30 for the penalty table.
4. **Penalties.** A rider counts as penalized when any judge's penalty is nonzero; the magnitude is the mean |penalty| across the rider's judges, averaged over penalized riders only.

**Read before quoting:**
- **Scores are not normalised across classes.** A 7.0 in one class is not the same 7.0 in another — judges, difficulty and scoring scales differ. Comparing gap sizes *across* disciplines is comparing different scales.
- **Negative gaps are relative-judging artifacts, not errors.** When the top three score below the field on a maneuver, it usually means that maneuver separates the field by difficulty rather than skill — the comparison is within the same bucket.
- **Associative, not causal.** Which riders enter which classes, and how judges mark, both shape these gaps. These tables are a map of where to look, not proof of what wins.

---

*This is one of a series of data articles built on my equine-data results database — a personal AQHA show-results explorer that analyzes every class in the dataset.*
