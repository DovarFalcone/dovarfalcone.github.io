---
layout: post
title: Does the Draw Order Decide Horse Show Placings?
subtitle: 751 real draw sheets, 28,882 drawn riders — the earlier version measured the wrong column, and the honest effect is small but not zero
category: Project
tags: [Project, AQHA, Data Analysis, Horse Show, Equine]
comments: true
---

# Does the Draw Order Decide Horse Show Placings?

Every exhibitor knows the feeling: you draw late in a big class and wonder if the judge has already made up their mind. I've now got enough results in the equine-data database to actually test that question properly — and, as of this cut, the **published draw sheets** themselves, rather than a column I'd been assuming was the draw.

Across **751 draw sheets and 28,882 drawn riders**, horses drawn later do place marginally better on average. The effect is small — about **2.7 percentile points** from the first third of the draw to the last — but on the corrected data it is **consistent and measurable**, and it is strongest in the biggest classes.

The pooled size-weighted Spearman rho between draw order and placing is **−0.047** (95% CI **−0.068 … −0.023**), with **54.4%** of draw sheets showing a negative association. Here's the honest picture.

*Based on 28,882 drawn riders and 9,015 recorded placings · analysis refreshed 16 October 2026.*

> **Updated 16 October 2026 — this analysis was measuring the wrong column, and the code that computed it had a real defect.** Two separate things were wrong with the earlier cuts of this page.
>
> The first: they used `class_placing.draw_no` as the draw order. It is not — in **88% of classes its maximum value exceeds the number of riders in the class**, because that field carries back-number-like values and composite ids, not a starting order. The database now ingests the **published draw sheets** (`class_draw` / `class_draw_rider`), where `draw_no` runs 1…N across the full field, so this cut is the first built on an actual draw.
>
> The second: the tercile chart was produced by code that divided **all three terciles by one shared total** instead of each tercile by its own rider count. Those buckets do not hold equal rider counts once classes of different sizes are pooled — on this corpus they hold **55,038 / 51,406 / 48,764** riders — so the last tercile was shrunk hardest. The defect did not merely rescale the chart; it manufactured a result. Run exactly as deployed, that chart reported a last-minus-first difference of **−0.0204** with a 95% interval of **−0.0218…−0.0190** — an apparently significant late-draw advantage. Run with each tercile divided by its own rider count, the same data gives **−0.0019**, interval **−0.0060…+0.0022**: a difference indistinguishable from zero. The pooling defect is fixed in the project's analysis code (in review as this update publishes), and the deployed method's own headline statistic on today's full corpus is rho **−0.0002** (95% CI **−0.0056…+0.0053**) — a number with no direction at all.
>
> That is the clearest sign the old column was measuring noise rather than drawing, and it is why this page's findings rest on the draw sheets instead. The earlier headline "the effect faded into noise" was about that column, not about draws.

---

## Per-sheet correlation distribution

For each draw sheet with at least 5 recorded placings I computed the rank correlation (Spearman's rho) between draw position and place percentile, where the percentile is normalised against the sheet's **own field size** — not against the number of placings recorded, which is capped at 15 by the scrape.

<svg viewBox="0 0 560 230" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Spearman rho per draw sheet histogram, 662 sheets">
  <line x1="12" y1="196" x2="548" y2="196" stroke="#888" stroke-width="1"/>
  <line x1="280" y1="16" x2="280" y2="196" stroke="#999" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="280" y="212" text-anchor="middle" fill="#777" font-size="12">0</text>
  <rect x="46" y="196" width="72" height="0" rx="2" fill="#6a9e78"/>
  <rect x="130" y="116" width="72" height="80" rx="2" fill="#6a9e78"/>
  <text x="166" y="110" fill="#777" font-size="11" text-anchor="middle">125</text>
  <rect x="214" y="96" width="72" height="100" rx="2" fill="#6a9e78"/>
  <text x="250" y="90" fill="#777" font-size="11" text-anchor="middle">156</text>
  <rect x="298" y="93" width="72" height="103" rx="2" fill="#d0a65e"/>
  <text x="334" y="87" fill="#777" font-size="11" text-anchor="middle">160</text>
  <rect x="382" y="138" width="72" height="58" rx="2" fill="#d0a65e"/>
  <text x="418" y="132" fill="#777" font-size="11" text-anchor="middle">91</text>
  <rect x="466" y="163" width="72" height="33" rx="2" fill="#d0a65e"/>
  <text x="502" y="157" fill="#777" font-size="11" text-anchor="middle">51</text>
  <rect x="46" y="145" width="72" height="20" rx="2" fill="#6a9e78"/>
  <text x="82" y="139" fill="#777" font-size="11" text-anchor="middle">79</text>
  <g fill="#777" font-size="10" text-anchor="middle">
    <text x="82" y="224">−0.8</text>
    <text x="166" y="224">−0.4</text>
    <text x="250" y="224">−0.1</text>
    <text x="334" y="224">0.1</text>
    <text x="418" y="224">0.3</text>
    <text x="502" y="224">0.6</text>
  </g>
  <text x="12" y="10" fill="#555" font-size="12">Spearman rho per draw sheet (662 sheets, ≥ 5 recorded placings)</text>
</svg>

Green bins are sheets where later draws placed better (negative rho); tan bins are the reverse. The mass sits left of zero — **median rho −0.047**, **54.4%** of sheets negative — but the spread is enormous: the 10th percentile is **−0.43** and the 90th is **+0.36**, so plenty of sheets run strongly the other way. One pooled number hides all of that, and this histogram is the honest picture.

---

## Draw terciles

Within each draw sheet I split the field into three equal groups by draw position and averaged their place percentile (0.0 = win, 1.0 = last; lower is better). Each tercile is pooled as its own total place percentile divided by its **own rider count** — the groups are equal *within* a sheet, but not once sheets of different sizes are combined, which is exactly the normalisation the old code got wrong. Pooled across all sheets:

<svg viewBox="0 0 420 190" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Mean place percentile by draw third">
  <line x1="40" y1="160" x2="400" y2="160" stroke="#888" stroke-width="1"/>
  <rect x="70" y="50" width="60" height="110" rx="2" fill="#6a9e78"/>
  <text x="100" y="42" fill="#444" font-size="12" text-anchor="middle">0.250</text>
  <rect x="180" y="56" width="60" height="104" rx="2" fill="#6a9e78"/>
  <text x="210" y="48" fill="#444" font-size="12" text-anchor="middle">0.237</text>
  <rect x="290" y="62" width="60" height="98" rx="2" fill="#6a9e78"/>
  <text x="320" y="54" fill="#444" font-size="12" text-anchor="middle">0.223</text>
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

The gradient is monotone: **0.250 → 0.237 → 0.223**, a last-minus-first difference of **−0.027** percentile points. On the scale of a 20-horse class that is roughly **half a placing** — real, consistent, and far smaller than the noise between two runs of the same class.

---

## The strongest test: does drawing late make you more likely to place at all?

Every measure above uses only riders who *received a placing*, which the scrape caps at 15 per class — so in a 224-horse barrel race, 209 riders are invisible to it. The draw sheets cover the **whole field**, so they let me ask a cleaner question: among everyone who drew, what share recorded a placing? That answer cannot be distorted by the 15-row ceiling.

| Field size | First third | Middle third | Last third | Spread |
|---|---|---|---|---|
| All sheets (≥ 10) | 30.87% | 30.92% | 31.62% | +0.75 pt |
| More than 15 | 27.59% | 28.19% | 28.96% | +1.36 pt |
| 50 or more | 17.62% | 17.84% | **19.53%** | **+1.91 pt** |

In small classes the draw makes no difference to whether you place. In the largest classes — the ones where the draw actually matters to an exhibitor — the last third places **1.9 percentage points** more often than the first third, on a base rate of 18%. That is a **10% relative** improvement, and it is the same direction as the correlation and the tercile gradient, from three independent measurements.

---

## Does going first matter?

The first draw is its own story. Among the **330 sheets** where the first-drawn rider recorded a placing, first-goers won **41 classes — 12.4%** — against **9.2%** expected if the draw carried no advantage (the mean of 1 divided by the number of placings recorded in those same sheets, which is the right benchmark, since a rider who places is competing against the other placed riders, not the whole field). That's a **1.35×** win rate, rising to **1.48×** in fields of more than 15.

| Group | Sheets | First-goers won | Expected | Ratio |
|---|---|---|---|---|
| All sheets | 330 | 12.4% | 9.2% | 1.35× |
| Fields > 15 riders | 219 | 11.4% | 7.7% | **1.48×** |

**Caveats.** There is only one first-goer per sheet, so this compares sheets against each other, not riders within a sheet, and 330 sheets is a modest sample. A higher-than-odds win rate is associative, not causal: the draw is a schedule artefact, and what draws first may differ in other ways — a trainer with two entries may pick the slot, and scratches can move the first position.

---

## By discipline

Pooled size-weighted rho per discipline, for every discipline with at least 15 draw sheets. Negative = later draws placed better; positive = earlier draws did.

| Discipline | Draw sheets | Weighted rho |
|---|---|---|
| Western Riding | 36 | −0.112 |
| Reining | 72 | −0.081 |
| Ranch Riding | 83 | −0.078 |
| Roping | 23 | −0.071 |
| Ranch Trail | 47 | −0.062 |
| Western Pleasure | 23 | −0.048 |
| Hunt Seat Equitation | 19 | −0.047 |
| Showmanship | 25 | −0.040 |
| Barrels | 25 | −0.035 |
| Working Hunter | 27 | −0.035 |
| Halter | 55 | −0.014 |
| Pole Bending | 27 | −0.011 |
| Trail | 96 | −0.009 |
| Horsemanship | 27 | +0.012 |
| Hunter Under Saddle | 27 | **+0.095** |

The late-draw edge is concentrated in the disciplines judged on **accumulated manoeuvre scores** — Western Riding, Reining, Ranch Riding, Ranch Trail — where a judge scoring fifteen riders in sequence is plausibly drifting as the class goes on. It is absent, and even reversed, in **Hunter Under Saddle and Horsemanship**, the two classes judged as a single go-round on overall impression. Barrels and Pole Bending sit near zero, which matters because those are the classes with the deepest fields: whatever is happening in the pattern classes is not a general "later is better" law.

---

## Methodology & caveats

**How it's measured:**

1. **The draw is the published draw sheet** — `class_draw_rider.draw_no`, which runs 1…field size across the entire field, joined to results on back number. This is the fix that made the rest possible; the earlier version's `class_placing.draw_no` is not a draw order.
2. **Within-sheet percentile normalisation** — raw places are meaningless across sheets of different sizes, so each placed rider's outcome is `place_pct = (place − 1) / (field − 1)`, using the sheet's true field size.
3. **Spearman's rho per sheet** — rank correlation between draw position and place percentile, average ranks for ties, for every sheet with ≥ 5 recorded placings.
4. **Pooled weighted mean + bootstrap CI** — sheet rhos pooled as a size-weighted mean; 95% interval from a 2,000-iteration bootstrap resampling sheets with replacement (fixed seed, reproducible).
5. **P(placed) by quarter-of-field** — the whole-field test, using every drawn rider, which the 15-placing cap cannot distort.
6. **First-goer test** — only sheets where the first-drawn rider recorded a placing; the benchmark is the mean of 1/(placings recorded) over those sheets.

**Filters applied to the 2,789 ingested draw sheets** (751 survive): a class name resolvable via the schedule, a field of at least 10, a rider list covering at least 95% of the declared field, no draw number beyond the field size, and at least one recorded placing. Each of those rejects a sheet where the draw range can't be trusted, and together they are why this cut covers a third of the ingested sheets rather than all of them.

**Read before quoting:**

- **Draw semantics vary.** In some classes the draw is a random start order; in others it is a scheduled slot, and scratches and re-entries can shift it afterwards. One pooled number averages over all of these.
- **The effect is small.** About 2.7 percentile points across the whole draw range, and 1.9 points of extra chance of placing in the deepest classes. It is not the difference between a ribbon and a drive home empty.
- **Only 751 sheets are captured**, and they skew to shows that publish draws — Congress and the championship shows. Small shows are barely represented.
- **Per-sheet variation is the interesting part.** Most sheets show little, but 12% sit at −0.4 or lower and 8% at +0.4 or higher. Whatever is going on is a property of particular classes, not of horse shows in general.

---

*This is one of a series of data articles built on my equine-data results database — a personal AQHA show-results explorer that analyzes every class in the dataset.*
