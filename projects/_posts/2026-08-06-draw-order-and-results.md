---
layout: post
title: Does the Draw Order Decide Horse Show Placings? 🐴
subtitle: 1,748 classes of AQHA results — with twice the data, the pooled draw effect has faded into noise, but the first-draw advantage is still there
category: Project
tags: [Project, AQHA, Data Analysis, Horse Show, Equine]
comments: true
---

# Does the Draw Order Decide Horse Show Placings?

Every exhibitor knows the feeling: you draw late in a big class and wonder if the judge has already made up their mind. I've now got enough results in the equine-data database to actually test that question properly.

Across **1,748 classes and 191,605 placings**, horses drawn later place marginally better on average — but the pooled effect is now small enough that it can't be separated from zero. Class-to-class variation swamps it. Draw order is, at most, a tie-breaker, not a deciding factor.

The pooled weighted Spearman rho between draw order and placing is **−0.005** (95% CI −0.018…+0.007), and only **50.3%** of classes show any negative association at all. Here's the honest picture.

*Based on 191,605 placings · analysis refreshed 27 Sept 2026.*

> **Updated 27 September 2026.** This post was first published in August 2026 on 934 classes and 86,281 placings, where the pooled rho was −0.019 with an interval entirely below zero. The dataset has since more than doubled, and **the headline got weaker, not stronger**: mean rho drifted from −0.019 to −0.005 and the confidence interval now straddles zero, while the median class rho went from −0.028 to −0.004. The first-draw win-rate edge also eased from 1.45× to 1.25×. The last-vs-first draw tercile contrast is the one number that held its ground (−0.019 → −0.018, interval still below zero). Numbers below are the current ones; the August figures are noted where they differ.

---

## Per-class correlation distribution

For each class with at least 10 riders I computed the rank correlation (Spearman's rho) between draw order and placing. Negative rho means later draws placed better; positive means earlier draws did. The histogram below is the real spread across all 1,748 classes — not just the pooled average:

<svg viewBox="0 0 560 230" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Spearman rho per class histogram, 1748 classes">
  <line x1="12" y1="196" x2="548" y2="196" stroke="#888" stroke-width="1"/>
  <line x1="276" y1="16" x2="276" y2="196" stroke="#999" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="276" y="212" text-anchor="middle" fill="#777" font-size="12">0</text>
  <rect x="16" y="196" width="24" height="0" rx="2" fill="#6a9e78"/>
  <rect x="42" y="195" width="24" height="1" rx="2" fill="#6a9e78"/>
  <rect x="68" y="191" width="24" height="5" rx="2" fill="#6a9e78"/>
  <rect x="94" y="181" width="24" height="15" rx="2" fill="#6a9e78"/>
  <rect x="120" y="170" width="24" height="26" rx="2" fill="#6a9e78"/>
  <text x="132" y="164" fill="#777" font-size="11" text-anchor="middle">39</text>
  <rect x="146" y="155" width="24" height="41" rx="2" fill="#6a9e78"/>
  <text x="158" y="149" fill="#777" font-size="11" text-anchor="middle">62</text>
  <rect x="172" y="119" width="24" height="77" rx="2" fill="#6a9e78"/>
  <text x="184" y="113" fill="#777" font-size="11" text-anchor="middle">115</text>
  <rect x="198" y="74" width="24" height="122" rx="2" fill="#6a9e78"/>
  <text x="210" y="68" fill="#777" font-size="11" text-anchor="middle">183</text>
  <rect x="224" y="53" width="24" height="143" rx="2" fill="#6a9e78"/>
  <text x="236" y="47" fill="#777" font-size="11" text-anchor="middle">213</text>
  <rect x="250" y="29" width="24" height="167" rx="2" fill="#6a9e78"/>
  <text x="262" y="23" fill="#777" font-size="11" text-anchor="middle">250</text>
  <rect x="276" y="26" width="24" height="170" rx="2" fill="#d0a65e"/>
  <text x="288" y="20" fill="#777" font-size="11" text-anchor="middle">254</text>
  <rect x="302" y="67" width="24" height="129" rx="2" fill="#d0a65e"/>
  <text x="314" y="61" fill="#777" font-size="11" text-anchor="middle">193</text>
  <rect x="328" y="82" width="24" height="114" rx="2" fill="#d0a65e"/>
  <text x="340" y="76" fill="#777" font-size="11" text-anchor="middle">171</text>
  <rect x="354" y="122" width="24" height="74" rx="2" fill="#d0a65e"/>
  <text x="366" y="116" fill="#777" font-size="11" text-anchor="middle">110</text>
  <rect x="380" y="156" width="24" height="40" rx="2" fill="#d0a65e"/>
  <text x="392" y="150" fill="#777" font-size="11" text-anchor="middle">60</text>
  <rect x="406" y="169" width="24" height="27" rx="2" fill="#d0a65e"/>
  <text x="418" y="163" fill="#777" font-size="11" text-anchor="middle">41</text>
  <rect x="432" y="181" width="24" height="15" rx="2" fill="#d0a65e"/>
  <rect x="458" y="189" width="24" height="7" rx="2" fill="#d0a65e"/>
  <rect x="484" y="196" width="24" height="0" rx="2" fill="#d0a65e"/>
  <rect x="510" y="196" width="24" height="0" rx="2" fill="#d0a65e"/>
  <g fill="#777" font-size="10" text-anchor="middle">
    <text x="38" y="224">−1.0</text>
    <text x="104" y="224">−0.4</text>
    <text x="170" y="224">−0.2</text>
    <text x="276" y="224">0</text>
    <text x="382" y="224">0.2</text>
    <text x="448" y="224">0.4</text>
    <text x="514" y="224">1.0</text>
  </g>
  <text x="12" y="10" fill="#555" font-size="12">Spearman rho per class (1,748 classes, n ≥ 10)</text>
</svg>

Green bins are classes where later draws placed better (negative rho); tan bins are the reverse. The distribution is a bell sitting almost exactly on zero — the tallest single bin is actually the **first positive** one (254 classes between 0.0 and +0.1) against 250 classes in the −0.1…0.0 bin beside it. **Median rho −0.004**, **50.3%** of classes negative, and the full range still runs from −0.80 to +0.80. One pooled number hides all of that spread, and this histogram is the honest picture.

---

## Draw terciles

Within each class I split riders into three equal groups by draw rank and averaged their place percentile (0.0 = win, 1.0 = last; lower is better). Pooled across all classes:

<svg viewBox="0 0 420 190" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Mean place percentile by draw third">
  <line x1="40" y1="160" x2="400" y2="160" stroke="#888" stroke-width="1"/>
  <rect x="70" y="49" width="60" height="111" rx="2" fill="#6a9e78"/>
  <text x="100" y="41" fill="#444" font-size="12" text-anchor="middle">0.175</text>
  <rect x="180" y="56" width="60" height="104" rx="2" fill="#6a9e78"/>
  <text x="210" y="48" fill="#444" font-size="12" text-anchor="middle">0.165</text>
  <rect x="290" y="60" width="60" height="100" rx="2" fill="#6a9e78"/>
  <text x="320" y="52" fill="#444" font-size="12" text-anchor="middle">0.158</text>
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

Later draws average **−0.018** percentile points better than early draws across the whole range — the interval below is the bootstrap 95% CI on that difference:

<svg viewBox="0 0 420 48" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Last vs first tercile difference with 95 percent confidence interval">
  <line x1="20" y1="24" x2="400" y2="24" stroke="#999" stroke-width="1"/>
  <line x1="60" y1="24" x2="360" y2="24" stroke="#d0a65e" stroke-width="6" stroke-linecap="round"/>
  <circle cx="189" cy="24" r="5" fill="#c0392b"/>
  <text x="60" y="42" text-anchor="middle" fill="#777" font-size="11">−0.021</text>
  <text x="189" y="42" text-anchor="middle" fill="#444" font-size="11">−0.018</text>
  <text x="360" y="42" text-anchor="middle" fill="#777" font-size="11">−0.014</text>
  <text x="20" y="14" fill="#777" font-size="11">95% CI on last-vs-first difference</text></svg>

The whole interval sits below zero, so this contrast is real — but it is **−0.018 percentile points across the entire draw range**, and it is the *only* pooled measurement here that still clears zero. That's far smaller than typical class-to-class variation, and it is not the same statement as "drawing late helps".

---

## Does going first matter?

The most striking single number on this page is actually about the **first** draw, not the last. Among the 718 classes of 10+ riders where the first-drawn rider posted a numeric result (1,239 more classes are excluded because their first draw scratched or never placed), first-goers won **8.5%** of their classes — against **6.8%** expected if the draw carried no advantage (the mean of 1/n across the same classes). That's a **1.25×** win rate.

| Class size | First-goers | Won | Expected | Ratio |
|---|---|---|---|---|
| all classes (n ≥ 5) | 1,334 | 12.2% | 10.7% | 1.14× |
| 10+ riders | 719 | 8.5% | 6.8% | **1.25×** |

The direction survives larger fields but the gap has narrowed since the August cut (1.45× on 355 classes then, 1.25× on 719 now) — exactly what you'd expect if part of the earlier number was the small sample being flattering.

Broken out by discipline, the first-draw edge is concentrated in the western pattern and hunter classes:

| Discipline | Classes | First-goers won | Expected | Ratio |
|---|---|---|---|---|
| Showmanship | 122 | 23.0% | 9.5% | 2.42× |
| Hunter Hack | 20 | 25.0% | 13.0% | 1.92× |
| Roping | 28 | 14.3% | 9.3% | 1.54× |
| Hunter Under Saddle | 51 | 17.6% | 11.9% | 1.48× |
| Western Riding | 66 | 15.2% | 10.7% | 1.42× |
| Working Hunter | 35 | 14.3% | 10.7% | 1.34× |

The average placing is a quieter story: first-goers sit **−0.035** percentile points from the rest of the field (95% CI −0.058…−0.012) — an interval entirely on the better side of zero, though far smaller than the win-rate gap.

**Caveats.** There's only one first-goer per class, so this compares classes against each other, not riders within a class. The disciplines above have modest n's and no correction for multiple comparisons across ~20 disciplines — with draws like these, one or two will look strong by chance. A higher-than-odds win rate is associative, not causal: the draw is a schedule artifact, and classes that draw first may differ in other ways.

---

## By discipline

Pooled weighted rho per discipline for every discipline with at least 10 classes. Negative = later draws placed better; positive = earlier draws did.

| Discipline | Classes | Weighted rho |
|---|---|---|
| Trail | 214 | −0.041 |
| Western Pleasure | 174 | −0.025 |
| Hunter Under Saddle | 165 | +0.019 |
| Horsemanship | 144 | +0.008 |
| Showmanship | 143 | +0.038 |
| Ranch Riding | 141 | −0.007 |
| Ranch Trail | 107 | −0.029 |
| Halter | 103 | +0.030 |
| Hunt Seat Equitation | 101 | +0.020 |
| Reining | 88 | −0.051 |
| Western Riding | 70 | −0.043 |
| Ranch Rail | 34 | −0.003 |
| Roping | 33 | −0.083 |
| Working Hunter | 31 | −0.012 |
| Longe Line | 21 | +0.127 |
| Hunter Hack | 20 | +0.087 |
| Working Cow Horse | 18 | +0.034 |
| Conformation | 13 | −0.077 |
| Pole Bending | 12 | +0.111 |
| Barrels | 12 | +0.094 |
| Barrel Racing | 12 | +0.121 |
| Western Rail | 11 | +0.006 |
| Working Western Rail | 11 | +0.045 |
| Cutting | 10 | −0.103 |

The old three-discipline story got messier with more data. **Horsemanship and Showmanship** — the two clear "later draws don't help" exceptions in the August cut — have converged on zero (+0.008 and +0.038, both barely off it), and **Hunter Under Saddle** flipped sign but stayed small (+0.019 vs −0.043 before). What survives is a split by *class type*: the largest negative figures now sit in cattle and speed-adjacent work (**Cutting −0.103, Roping −0.083, Reining −0.051, Western Riding −0.043, Trail −0.041**), while the positive ones are the timed speed events and Longe Line (**Barrel Racing +0.121, Pole Bending +0.111, Barrels +0.094, Longe Line +0.127**) — where going later means a chewed-up arena or a warmer clock, so the sign flips the other way.

---

## Methodology & caveats

**How it's measured:**
1. **Within-class percentile normalisation** — raw places are meaningless across classes of different sizes (6th of 8 is not 6th of 60), so each rider's outcome is `place_pct = (place − 1) / (n − 1)`; draws are normalised the same way.
2. **Spearman's rho per class** — rank correlation between draw order and placing for every class with ≥ 10 riders (average ranks for ties; DQ and non-numeric rows excluded). 1,748 classes qualify today, up from 934 in August.
3. **Pooled weighted mean + bootstrap CI** — class rhos pooled as a size-weighted mean; 95% interval from a 2,000-iteration bootstrap resampling classes with replacement (fixed seed, reproducible).
4. **Draw terciles** — riders split into three equal groups by draw rank within each class.
5. **First-goer test** — only classes where the first-drawn rider posted a numeric result count; the benchmark is the mean of 1/n over the same classes, i.e. the win probability the draw alone would predict.

**Read before quoting:**
- **Draw semantics vary by class type.** In some classes the draw is a random start order; in others it's a scheduled slot, and scratches/re-entries can shift it afterward. One pooled number averages over all of these.
- **DQ rows are excluded** — only rows with a numeric place and a draw number enter the analysis, using the Combined Judges roll-up placing.
- **The pooled effect is no longer distinguishable from zero** (−0.005, CI −0.018…+0.007). Only the last-vs-first tercile contrast still clears zero, at about 1.8 percentile points — far smaller than typical class-to-class variation.
- **Doubling the data weakened the signal, and that's the useful lesson** — an effect that shrank toward zero as n grew was mostly small-sample optimism. Treat single-cut anomalies in your own results with the same suspicion.
- **Per-class variation is the interesting part** — the pooled mean hides a lot of spread, and the histogram above is the honest picture.

---

*This is one of a series of data articles built on my equine-data results database — a personal AQHA show-results explorer that analyzes every class in the dataset.*
