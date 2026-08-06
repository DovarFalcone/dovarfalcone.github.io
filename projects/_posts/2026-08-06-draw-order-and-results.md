---
layout: post
title: Does the Draw Order Decide Horse Show Placings? 🐴
subtitle: Analyzing 934 classes of AQHA results — later draws place slightly better, but the effect is tiny
category: Project
tags: [Project, AQHA, Data Analysis, Horse Show, Equine]
comments: true
---

# Does the Draw Order Decide Horse Show Placings?

Every exhibitor knows the feeling: you draw late in a big class and wonder if the judge has already made up their mind. I've now got enough results in the equine-data database to actually test that question properly.

Across **934 classes and 86,281 placings**, horses drawn later place marginally better on average — but the effect is small, and class-to-class variation swamps it. Draw order is, at most, a tie-breaker, not a deciding factor.

The pooled weighted Spearman rho between draw order and placing is **−0.019** (95% CI −0.036…−0.004), and only **52.9%** of classes show any negative association at all. Here's the honest picture.

*Based on 86,281 placings · analysis refreshed Aug 2026.*

---

## Per-class correlation distribution

For each class with at least 10 riders I computed the rank correlation (Spearman's rho) between draw order and placing. Negative rho means later draws placed better; positive means earlier draws did. The histogram below is the real spread across all 934 classes — not just the pooled average:

<svg viewBox="0 0 560 230" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Histogram of Spearman rho per class, 934 classes">
  <line x1="12" y1="196" x2="548" y2="196" stroke="#888" stroke-width="1"/>
  <line x1="214" y1="16" x2="214" y2="196" stroke="#999" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="214" y="212" text-anchor="middle" fill="#777" font-size="12">0</text>
  <g fill="#6a9e78">
    <rect x="16"  y="164" width="44" height="32"  rx="2"/>
    <rect x="82"  y="129" width="44" height="67"  rx="2"/>
    <rect x="148" y="26"  width="44" height="170" rx="2"/>
    <rect x="214" y="95"  width="44" height="101" rx="2"/>
  </g>
  <g fill="#d0a65e">
    <rect x="280" y="93"  width="44" height="103" rx="2"/>
    <rect x="346" y="60"  width="44" height="136" rx="2"/>
    <rect x="412" y="132" width="44" height="64"  rx="2"/>
    <rect x="478" y="170" width="44" height="26"  rx="2"/>
  </g>
  <g fill="#777" font-size="11" text-anchor="middle">
    <text x="38"  y="178">43</text>
    <text x="104" y="143">89</text>
    <text x="170" y="40">227</text>
    <text x="236" y="109">135</text>
    <text x="302" y="107">138</text>
    <text x="368" y="74">182</text>
    <text x="434" y="146">85</text>
    <text x="500" y="184">35</text>
  </g>
  <g fill="#777" font-size="10" text-anchor="middle">
    <text x="38"  y="224">&lt;−0.5</text>
    <text x="104" y="224">−0.4</text>
    <text x="170" y="224">−0.2</text>
    <text x="236" y="224">−0.05</text>
    <text x="302" y="224">0.05</text>
    <text x="368" y="224">0.2</text>
    <text x="434" y="224">0.4</text>
    <text x="500" y="224">&gt;0.5</text>
  </g>
  <text x="12" y="10" fill="#555" font-size="12">Spearman rho per class (934 classes, n ≥ 10)</text>
</svg>

Green bins are classes where later draws placed better (negative rho); tan bins are the reverse. The mass sits just left of zero — **median rho −0.028**, and **52.9%** of classes are negative — but the full range (from roughly −0.8 to +0.8) shows how much classes disagree. One pooled number hides a lot of spread, and this histogram is the honest picture.

---

## Draw terciles

Within each class I split riders into three equal groups by draw rank and averaged their place percentile (0.0 = win, 1.0 = last; lower is better). Pooled across all classes:

<svg viewBox="0 0 420 190" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Mean place percentile by draw third">
  <line x1="40" y1="160" x2="400" y2="160" stroke="#888" stroke-width="1"/>
  <g fill="#6a9e78">
    <rect x="70"  y="116" width="60" height="44"  rx="2"/>
    <rect x="180" y="123" width="60" height="37"  rx="2"/>
    <rect x="290" y="128" width="60" height="32"  rx="2"/>
  </g>
  <g fill="#444" font-size="12" text-anchor="middle">
    <text x="100" y="108">0.176</text>
    <text x="210" y="115">0.165</text>
    <text x="320" y="120">0.156</text>
  </g>
  <g fill="#555" font-size="11" text-anchor="middle">
    <text x="100" y="178">1st third</text>
    <text x="210" y="178">2nd third</text>
    <text x="320" y="178">3rd third</text>
    <text x="100" y="191">early draws</text>
    <text x="210" y="191">(middle)</text>
    <text x="320" y="191">late draws</text>
  </g>
  <text x="40" y="12" fill="#555" font-size="12">Mean place percentile by draw third (pooled; lower = better)</text>
</svg>

Later draws average **−0.019** percentile points better than early draws across the whole range — the interval below is the bootstrap 95% CI on that difference:

<svg viewBox="0 0 420 48" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Last vs first tercile difference with 95% confidence interval">
  <line x1="20" y1="24" x2="400" y2="24" stroke="#999" stroke-width="1"/>
  <line x1="60" y1="24" x2="360" y2="24" stroke="#d0a65e" stroke-width="6" stroke-linecap="round"/>
  <circle cx="210" cy="24" r="5" fill="#c0392b"/>
  <text x="60"  y="42" text-anchor="middle" fill="#777" font-size="11">−0.024</text>
  <text x="210" y="42" text-anchor="middle" fill="#444" font-size="11">−0.019</text>
  <text x="360" y="42" text-anchor="middle" fill="#777" font-size="11">−0.015</text>
  <text x="20" y="14" fill="#777" font-size="11">95% CI on last-vs-first difference</text>
</svg>

The whole interval sits below zero, so the effect is real — but it is **−0.019 percentile points across the entire draw range**. That's far smaller than typical class-to-class variation.

---

## Does going first matter?

The most striking single number on this page is actually about the **first** draw, not the last. Among the 355 classes of 10+ riders where the first-drawn rider posted a numeric result, first-goers won **9.3%** of their classes — against **6.4%** expected if the draw carried no advantage (the mean of 1/n across the same classes). That's a **1.45×** win rate.

| Class size | First-goers | Won | Expected | Ratio |
|---|---|---|---|---|
| 5–9 riders | 285 | 17.5% | 15.2% | 1.15× |
| 10+ riders | 355 | 9.3% | 6.4% | **1.45×** |

The effect survives larger fields but bigger classes dilute it. Going first also shifts the average placing slightly better: first-goers sit **−0.048** percentile points from the rest of the field (95% CI −0.081…−0.014) — an interval entirely on the better side of zero, though far smaller than the win-rate gap.

**Caveats.** There's only one first-goer per class, so this compares classes against each other, not riders within a class. A higher-than-odds win rate is associative, not causal — the draw is a schedule artifact, and classes that draw first may differ in other ways.

---

## By discipline

Pooled weighted rho per discipline. Bars left of zero = later draws placed better in that discipline; right = earlier draws did. `n` is the number of classes behind each figure — disciplines with small n are noisy.

<svg viewBox="0 0 560 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Weighted mean rho per discipline">
  <line x1="280" y1="16" x2="280" y2="252" stroke="#999" stroke-width="1"/>
  <text x="280" y="268" text-anchor="middle" fill="#777" font-size="11">0</text>
  <g font-size="11">
    <text x="268" y="40" text-anchor="end" fill="#555">Reining</text>
    <rect x="262" y="30" width="18" height="16" fill="#6a9e78"/>
    <text x="284" y="43" fill="#444">−0.065 · n=64</text>
    <text x="268" y="66" text-anchor="end" fill="#555">Ranch Trail</text>
    <rect x="264" y="56" width="16" height="16" fill="#6a9e78"/>
    <text x="284" y="69" fill="#444">−0.050 · n=50</text>
    <text x="268" y="92" text-anchor="end" fill="#555">Halter</text>
    <rect x="264" y="82" width="16" height="16" fill="#6a9e78"/>
    <text x="284" y="95" fill="#444">−0.046 · n=64</text>
    <text x="268" y="118" text-anchor="end" fill="#555">Trail</text>
    <rect x="264" y="108" width="16" height="16" fill="#6a9e78"/>
    <text x="284" y="121" fill="#444">−0.043 · n=113</text>
    <text x="268" y="144" text-anchor="end" fill="#555">Western Riding</text>
    <rect x="258" y="134" width="22" height="16" fill="#6a9e78"/>
    <text x="284" y="147" fill="#444">−0.078 · n=50</text>
    <text x="268" y="170" text-anchor="end" fill="#555">Horsemanship</text>
    <rect x="280" y="160" width="16" height="16" fill="#d0a65e"/>
    <text x="300" y="173" fill="#444">+0.037 · n=74</text>
    <text x="268" y="196" text-anchor="end" fill="#555">Showmanship</text>
    <rect x="280" y="186" width="16" height="16" fill="#d0a65e"/>
    <text x="300" y="199" fill="#444">+0.030 · n=74</text>
    <text x="268" y="222" text-anchor="end" fill="#555">Hunter U/S</text>
    <rect x="280" y="212" width="16" height="16" fill="#d0a65e"/>
    <text x="300" y="225" fill="#444">+0.043 · n=72</text>
  </g>
</svg>

**Horsemanship, Showmanship and Hunter Under Saddle** are the notable exceptions — later draws didn't help there at all (in fact slightly the reverse). The strongest negative signals (Reining, Ranch Trail, Halter, Western Riding) are consistent with a modest late-draw edge in pattern/rail classes.

---

## Methodology & caveats

**How it's measured:**
1. **Within-class percentile normalisation** — raw places are meaningless across classes of different sizes (6th of 8 is not 6th of 60), so each rider's outcome is `place_pct = (place − 1) / (n − 1)`; draws are normalised the same way.
2. **Spearman's rho per class** — rank correlation between draw order and placing for every class with ≥ 10 riders (average ranks for ties; DQ and non-numeric rows excluded).
3. **Pooled weighted mean + bootstrap CI** — class rhos pooled as a size-weighted mean; 95% interval from a 2,000-iteration bootstrap resampling classes with replacement (fixed seed, reproducible).
4. **Draw terciles** — riders split into three equal groups by draw rank within each class.

**Read before quoting:**
- **Draw semantics vary by class type.** In some classes the draw is a random start order; in others it's a scheduled slot, and scratches/re-entries can shift it afterward. One pooled number averages over all of these.
- **DQ rows are excluded** — only rows with a numeric place and a draw number enter the analysis, using the Combined Judges roll-up placing.
- **The effect is small:** about 2 percentile points across the whole draw range — far smaller than typical class-to-class variation.
- **Per-class variation is the interesting part** — the pooled mean hides a lot of spread, and the histogram above is the honest picture.

---

*This is one of a series of data articles built on my equine-data results database — a personal AQHA show-results explorer that analyzes every class in the dataset.*
