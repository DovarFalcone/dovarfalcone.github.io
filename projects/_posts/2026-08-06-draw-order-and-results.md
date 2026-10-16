---
layout: post
title: Does the Draw Order Decide Horse Show Placings?
subtitle: A little. Late draws do slightly better, and mostly in the biggest classes.
category: Project
tags: [Project, AQHA, Data Analysis, Horse Show, Equine]
comments: true
---

Anyone who has shown a horse knows the feeling of drawing late in a big class and wondering if the judge already has the class pinned. I have enough results in my equine-data database now to check, and as of this update I have the published draw sheets themselves, so I can use the real starting order.

The short answer: horses drawn late place a little better on average. Over 751 draw sheets and 28,882 drawn riders, the last third of the draw finished about 2.7 points better (on a 100-point scale, explained below) than the first third. That's roughly half a placing in a 20-horse class. It's small, but it shows up the same way in every test I ran, and it's strongest in the biggest classes.

*Based on 28,882 drawn riders and 9,015 recorded placings. Numbers refreshed October 16, 2026.*

> **Updated October 16, 2026.** The earlier versions of this page got two things wrong.
>
> First, I was using the wrong column as the draw. The `draw_no` field on the results table isn't a starting order. In 88% of classes its highest value was bigger than the number of riders in the class, because it holds back numbers and other IDs. The database now pulls in the published draw sheets, where the draw runs from 1 to the size of the field, so this is the first version built on an actual draw.
>
> Second, the code behind the old "draw thirds" chart divided all three groups by one shared total instead of each group by its own rider count. The groups weren't the same size (55,038, 51,406, and 48,764 riders), so the late group got shrunk the most. That bug created a late-draw advantage that wasn't there: run as deployed, it showed a difference of −0.0204 (95% CI −0.0218 to −0.0190), which looked significant. Fixed, the same data shows −0.0019 (−0.0060 to +0.0022), which is no difference at all. The fix is in the project's analysis code, and the old column's overall correlation on today's data is −0.0002 (−0.0056 to +0.0053), which has no direction either. The old column was measuring noise, and the earlier headline that "the effect faded into noise" was about that column, not about the draw.

---

## How I measure a placing

Raw placings don't compare well across classes. Fifth out of 6 and fifth out of 60 are very different rides. So I turn every placing into a score from 0 to 1 based on the class's full field size: a win is 0, last place is 1, and the middle of the class is 0.5. Lower is better. When I say "2.7 points" above, I mean 0.027 on that scale.

---

## Class by class

For each draw sheet with at least 5 recorded placings (662 of them), I checked whether later draws tended to place better or worse. That gives one number per class between −1 and +1. Below zero means later draws placed better. Above zero means earlier draws did.

<svg viewBox="0 0 560 230" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Histogram of draw-order correlation per draw sheet, 662 sheets">
  <line x1="12" y1="196" x2="548" y2="196" stroke="#9aa3ae" stroke-width="1"/>
  <line x1="280" y1="16" x2="280" y2="196" stroke="#9aa3ae" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="280" y="212" text-anchor="middle" fill="#9aa3ae" font-size="12">0</text>
  <rect x="46" y="146" width="72" height="50" rx="2" fill="#6a9e78"/>
  <text x="82" y="140" fill="#c9ced6" font-size="11" text-anchor="middle">79</text>
  <rect x="130" y="116" width="72" height="80" rx="2" fill="#6a9e78"/>
  <text x="166" y="110" fill="#c9ced6" font-size="11" text-anchor="middle">125</text>
  <rect x="214" y="96" width="72" height="100" rx="2" fill="#6a9e78"/>
  <text x="250" y="90" fill="#c9ced6" font-size="11" text-anchor="middle">156</text>
  <rect x="298" y="93" width="72" height="103" rx="2" fill="#d0a65e"/>
  <text x="334" y="87" fill="#c9ced6" font-size="11" text-anchor="middle">160</text>
  <rect x="382" y="138" width="72" height="58" rx="2" fill="#d0a65e"/>
  <text x="418" y="132" fill="#c9ced6" font-size="11" text-anchor="middle">91</text>
  <rect x="466" y="163" width="72" height="33" rx="2" fill="#d0a65e"/>
  <text x="502" y="157" fill="#c9ced6" font-size="11" text-anchor="middle">51</text>
  <g fill="#9aa3ae" font-size="10" text-anchor="middle">
    <text x="82" y="224">−0.8</text>
    <text x="166" y="224">−0.4</text>
    <text x="250" y="224">−0.1</text>
    <text x="334" y="224">0.1</text>
    <text x="418" y="224">0.3</text>
    <text x="502" y="224">0.6</text>
  </g>
  <text x="12" y="10" fill="#c9ced6" font-size="12">Number of classes by draw-order correlation (662 classes)</text>
</svg>

Green bars are classes where later draws placed better, tan bars the reverse. A little more than half (54.4%) land on the green side, and the middle value is −0.047, so the lean toward late draws is slight. The spread is wide. One in ten classes sits at −0.43 or lower, and one in ten at +0.36 or higher. Plenty of classes go strongly the other way, which a single average would hide.

---

## Early, middle, and late draws

Next I split every class into thirds by draw position and averaged the placing score for each third. Each third is averaged over its own riders, which is the part the old code got wrong.

<svg viewBox="0 0 420 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Average placing score by draw third">
  <line x1="40" y1="160" x2="400" y2="160" stroke="#9aa3ae" stroke-width="1"/>
  <rect x="70" y="50" width="60" height="110" rx="2" fill="#6a9e78"/>
  <text x="100" y="42" fill="#c9ced6" font-size="12" text-anchor="middle">0.250</text>
  <rect x="180" y="56" width="60" height="104" rx="2" fill="#6a9e78"/>
  <text x="210" y="48" fill="#c9ced6" font-size="12" text-anchor="middle">0.237</text>
  <rect x="290" y="62" width="60" height="98" rx="2" fill="#6a9e78"/>
  <text x="320" y="54" fill="#c9ced6" font-size="12" text-anchor="middle">0.223</text>
  <g fill="#9aa3ae" font-size="11" text-anchor="middle">
    <text x="100" y="178">Early third</text>
    <text x="210" y="178">Middle third</text>
    <text x="320" y="178">Late third</text>
  </g>
  <text x="40" y="14" fill="#c9ced6" font-size="12">Average placing score by draw third (lower is better)</text>
</svg>

It steps down evenly from 0.250 to 0.237 to 0.223. The late third beats the early third by 0.027, the half a placing in a 20-horse class I mentioned at the top. That's real, and it's much smaller than the difference between two runs of the same class.

---

## Are late draws more likely to place at all?

Everything above only looks at riders who got a placing, and my scraper only captures up to 15 placings per class. In a 224-horse barrel race, that leaves 209 riders out. The draw sheets list the whole field, so I can ask a cleaner question: out of everyone who drew, what share placed? The 15-placing limit can't skew that answer.

| Field size | Early third | Middle third | Late third | Late minus early |
|---|---|---|---|---|
| All classes with 10+ riders | 30.87% | 30.92% | 31.62% | +0.75 pt |
| More than 15 riders | 27.59% | 28.19% | 28.96% | +1.36 pt |
| 50 or more riders | 17.62% | 17.84% | **19.53%** | **+1.91 pt** |

In small classes the draw makes no difference to whether you place. In the biggest classes, the late third placed 1.9 percentage points more often than the early third, on a base rate of about 18%. That's about 10% more placings for the late group. This is the third separate test pointing the same direction.

---

## Does going first matter?

The first draw gets its own look. In the 330 classes where the first rider placed, that rider won 41 times, or 12.4%. If the draw didn't matter, I'd expect 9.2%. That expected rate is the average of 1 divided by the number of placings recorded in those classes, because a rider who places is up against the other placed riders, not the whole field. So first-goers won about 1.35 times as often as chance, and 1.48 times in fields over 15.

| Group | Classes | First-goer won | Expected | Ratio |
|---|---|---|---|---|
| All classes | 330 | 12.4% | 9.2% | 1.35× |
| More than 15 riders | 219 | 11.4% | 7.7% | **1.48×** |

There's only one first-goer per class, and 330 classes is a modest sample. It also doesn't prove the draw caused the win. Drawing first isn't always random. A trainer with two entries may pick the slot, and scratches can move someone into the first spot.

---

## By discipline

Here's the same class-by-class number averaged per discipline, for every discipline with at least 15 draw sheets. Below zero means later draws placed better.

| Discipline | Draw sheets | Draw-order score |
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

The late-draw edge is biggest in Western Riding, Reining, Ranch Riding, and Ranch Trail, where the judge scores each maneuver. My guess is a judge marking a long class in order drifts as it goes, but that's a guess. Trail is also scored maneuver by maneuver and sits near zero, so I wouldn't call it a rule. Hunter Under Saddle goes the other way, with early draws doing better. Barrels and Pole Bending, which have some of the deepest fields, sit near zero, so this isn't a general "later is better" effect.

---

## How I did it

1. **The draw.** The draw comes from the published draw sheet, which numbers the whole field from 1 to N. I matched it to results by back number.
2. **The placing score.** Each placed rider gets `(place − 1) / (field − 1)`, using the class's real field size, so 0 is a win and 1 is last.
3. **Class by class.** For each draw sheet with at least 5 recorded placings, I calculated a Spearman rank correlation between draw position and placing score, with ties given their average rank.
4. **Pooling.** I combined the classes with an average weighted by class size, then got a 95% confidence interval by resampling the classes 2,000 times with a fixed seed so it's repeatable. The pooled correlation is −0.047 (95% CI −0.068 to −0.023).
5. **Share placed.** The "more likely to place at all" table uses every drawn rider, so the 15-placing limit can't affect it.
6. **First-goers.** Only classes where the first rider placed count, and the expected win rate is the average of 1 divided by the number of placings recorded.

I pulled in 2,789 draw sheets and kept 751. A sheet stayed in if its class name matched the show schedule, it had at least 10 riders, its rider list covered at least 95% of the declared field, no draw number was bigger than the field, and at least one rider placed. Each filter drops a sheet where I can't trust the draw, which is why only about a third made it.

**Before you quote any of this:**

- **The draw doesn't mean the same thing everywhere.** In some classes it's a random start order. In others it's a scheduled slot, and scratches and re-entries can shift it after the fact. One average covers all of them.
- **The effect is small.** About 2.7 points across the whole draw, and 1.9 points more chance of placing in the biggest classes. It won't decide whether you go home with a ribbon.
- **Only 751 draw sheets are in the data**, and they lean toward shows that publish draws, like Congress and the championship shows. Small shows barely show up.
- **The class-to-class spread is the interesting part.** Most classes show little, but 12% sit at −0.4 or lower and 8% at +0.4 or higher. Whatever is going on belongs to particular classes, not horse shows in general.

---

*This is one of a series of posts built on my equine-data results database, a personal AQHA show-results explorer that analyzes every class I've collected.*
