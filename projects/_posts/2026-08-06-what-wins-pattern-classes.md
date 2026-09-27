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

Across **619 (discipline, maneuver) buckets** with at least 20 scored riders (12 disciplines with per-maneuver scores), the single largest gap between placers 1–3 and the field is still **"180, B, 540" in Showmanship**: the top three average **+1.52** points on it while the rest of the field averages **−0.39** — a **+1.91-point spread** where the winners cleanly outscore everyone else.

The tables below show every discipline's strongest maneuvers in both directions, plus the penalty rates that decide where classes are actually lost.

*Based on 191,605 placings · 1,896,539 scores · analysis refreshed 22 Sept 2026.*

> **Updated 27 September 2026.** The August cut ran on 424 buckets and 1,080,007 scores; ingesting more shows grew it to 619 buckets and 1,896,539 scores. The "where classes are won" story was stable — the same Showmanship spin/rollback maneuver still leads with the same 1.91-point gap, and Showmanship + Horsemanship still dominate the top. The "where classes are lost" section is the one that moved: the penalty tables are now reported top-8 per discipline at n ≥ 30 instead of one global n ≥ 200 list, and the biggest *average deductions* turned out to belong to Showmanship's technical maneuvers, not Trail's flatwork.

---

## Where pattern classes are won

For every scored rider (one show-class-exhibitor-maneuver observation; the score is the mean across that rider's judges), here's the maneuver score of placers 1–3 vs everyone else. Positive gaps mean the top three outscore the field on that maneuver; negative gaps mean they score *below* it. Top by |gap|:

| Maneuver | Discipline | Top 3 avg | Field avg | Diff | n |
|---|---|---|---|---|---|
| 180, B, 540 | Showmanship | 1.52 | −0.39 | **+1.91** | 102 |
| S, 540L, B, 540R | Horsemanship | 1.27 | −0.25 | +1.52 | 116 |
| 135, W | Showmanship | 1.67 | 0.28 | +1.38 | 102 |
| RL, HG, RL | Hunt Seat Equitation | 1.29 | 0.02 | +1.27 | 172 |
| S, B, 90 L | Horsemanship | 0.94 | −0.14 | +1.08 | 87 |
| RL | Horsemanship | 1.33 | 0.27 | +1.07 | 322 |
| 2 PT, Sit T | Hunt Seat Equitation | 1.33 | 0.27 | +1.06 | 172 |
| RL | Hunt Seat Equitation | 1.30 | 0.25 | +1.05 | 138 |
| 450 | Showmanship | 1.12 | 0.10 | +1.03 | 203 |
| XJ, S | Horsemanship | 0.73 | −0.30 | +1.03 | 151 |

The pattern is striking and stable: **Showmanship and Horsemanship** dominate the top of the list, and the biggest gaps are all on **turning maneuvers** (540s, 360s, 180s) — the technical, pattern-heavy work where the top riders pull ahead. `n` is the number of scored riders behind the bucket (placers 1–3 plus field).

---

## Where classes are lost

Penalty rates per (discipline, maneuver) — the share of riders who drew at least one penalty, and the mean penalty size among those who did. A rider is penalized when any of its judges' penalties is nonzero. The tables below are the top buckets per discipline (reported at n ≥ 30):

| Maneuver | Discipline | Penalized | Total | Rate | Avg penalty |
|---|---|---|---|---|---|
| W, SP L, W | Trail | 31 | 36 | **86%** | 1.70 |
| Jog, Stop | Trail | 28 | 33 | 85% | 0.69 |
| WALK BOX/POLES | Trail | 35 | 41 | 85% | 0.86 |
| J, JOs, S | Trail | 24 | 30 | 80% | 1.05 |
| JO | Trail | 38 | 50 | 76% | 0.58 |
| Chng, LL L | Trail | 23 | 31 | 74% | 1.11 |
| W | Trail | 145 | 210 | 69% | 0.97 |

<svg viewBox="0 0 560 170" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Penalty rate by maneuver, top buckets">
  <line x1="150" y1="16" x2="150" y2="132" stroke="#999" stroke-width="1"/>
  <g font-size="11">
    <text x="140" y="36" text-anchor="end" fill="#555">W, SP L, W</text>
    <rect x="150" y="26" width="154" height="18" fill="#d0a65e"/>
    <text x="310" y="40" fill="#444">86%</text>
    <text x="140" y="62" text-anchor="end" fill="#555">Jog, Stop</text>
    <rect x="150" y="52" width="152" height="18" fill="#d0a65e"/>
    <text x="308" y="66" fill="#444">85%</text>
    <text x="140" y="88" text-anchor="end" fill="#555">WALK BOX/POLES</text>
    <rect x="150" y="78" width="152" height="18" fill="#d0a65e"/>
    <text x="308" y="92" fill="#444">85%</text>
    <text x="140" y="114" text-anchor="end" fill="#555">180, B, 540</text>
    <rect x="150" y="104" width="65" height="18" fill="#6a9e78"/>
    <text x="221" y="118" fill="#444">36% · avg −6.94</text>
  </g>
  <text x="150" y="150" fill="#777" font-size="11">% of riders penalized (tan = Trail, green = Showmanship)</text>
</svg>

**Trail still owns the *prevalence* story** — nearly nine in ten riders draw a penalty on some Trail maneuvers (W, SP L, W at 86%, Jog, Stop at 85%, WALK BOX/POLES at 85%), though the buckets involved are small (n = 30–41). Showmanship's 180, B, 540 is the big *cost* story — only 36% of riders draw a penalty there, but the mean deduction is **−6.94 points**, the largest average in the whole dataset. The next-biggest average deductions are also Showmanship/Horsemanship technical maneuvers:

| Maneuver | Discipline | Rate | Avg penalty | n |
|---|---|---|---|---|
| 180, B, 540 | Showmanship | 36% | **−6.94** | 102 |
| RL | Horsemanship | 7% | −5.91 | 340 |
| 450 | Showmanship | 32% | −5.47 | 203 |
| 1 3/4 | Showmanship | 41% | −4.87 | 51 |
| XJ, S | Horsemanship | 15% | −4.86 | 151 |
| 270, T | Showmanship | 25% | −4.77 | 386 |

That's the flip side of the "where classes are won" table: the maneuvers that separate the winners — Showmanship's spins and rollbacks — are exactly where a mistake is most expensive. The sport's *highest* penalty rates are Trail obstacles; its *largest* single-ride deductions are pattern-class mistakes.

---

## Methodology & caveats

**How it's measured:**
1. **Rider-level observations.** Scoresheet rows are duplicated per (exhibitor, judge, maneuver), so each rider's maneuver score is the mean across that rider's judges before anything is compared.
2. **Top vs field.** The rider's place comes from the Combined Judges roll-up for the same class; placers 1–3 are the "top" group and everyone else is the field. The gap is `avg_top − avg_field`.
3. **Buckets.** (discipline, maneuver) pairs are joined through a deduped discipline map. A bucket is reported only with ≥ 20 scored riders — 30 for the penalty table. 619 gap buckets and 544 penalty buckets qualify today (up from 424 in August).
4. **Penalties.** A rider counts as penalized when any judge's penalty is nonzero; the magnitude is the mean |penalty| across the rider's judges, averaged over penalized riders only.

**Read before quoting:**
- **Scores are not normalised across classes.** A 7.0 in one class is not the same 7.0 in another — judges, difficulty and scoring scales differ. Comparing gap sizes *across* disciplines is comparing different scales; comparing average *penalties* across disciplines is likewise apples-to-oranges.
- **Penalty rates and average penalty are different signals.** Trail heads the rate table on small-n buckets; Showmanship heads the magnitude table. A 36% rate with a −6.94 average (Showmanship) costs far more per class than an 86% rate with −1.70 (Trail) — read both columns.
- **Negative gaps are relative-judging artifacts, not errors.** When the top three score below the field on a maneuver, it usually means that maneuver separates the field by difficulty rather than skill — the comparison is within the same bucket.
- **Associative, not causal.** Which riders enter which classes, and how judges mark, both shape these gaps. These tables are a map of where to look, not proof of what wins.

---

*This is one of a series of data articles built on my equine-data results database — a personal AQHA show-results explorer that analyzes every class in the dataset.*