---
layout: post
title: Do Judges Favor Certain Horses?
subtitle: Mostly no. Across 68,059 judge and horse pairings, strong bias shows up in about one in a thousand.
category: Project
tags: [Project, AQHA, Data Analysis, Horse Show, Judging, Equine]
comments: true
---

Judges mostly agree with each other. I wanted to know whether some judges place specific horses consistently better or worse than everyone else does, so I compared each judge's placings for a horse with how that horse placed under all judges.

I looked at 68,059 judge and horse pairings from 781 judges, counting only pairs that met at least 5 times. Most pairs show almost no difference. A small number show a big one, and the largest is 0.737 on a 0 to 1 scale, about three-quarters of the class. With this many pairs, some big gaps will happen by chance, so this post is about how often bias shows up and what it looks like, not about any one judge. Nothing here names a judge, horse, or exhibitor.

*Numbers refreshed October 16, 2026, from the Combined Judges results in my database.*

> **Updated October 16, 2026.** This page used to report 8,145 pairs from 142 judges. The database now holds about eight times as much judging detail, and rerunning the numbers turned up a bug. When I only had a few rows for a judge in a class, the math that turns a placing into a 0 to 1 score used too small a number, which pushed some scores past 1 and made the extremes look bigger than they were. Everything below uses the corrected math. The main finding didn't change. The scoring-level section is also rebuilt to compare judges within the same discipline instead of across all of them.

---

## How I measure bias

1. **Score each placing.** For every judge's card, each horse's placing becomes a score from 0 to 1 within that judge's field. A win is 0 and last is 1. That lets me compare classes of different sizes.
2. **Pair each judge with each horse.** For every judge and horse that met at least 5 times, I average the scores that judge gave the horse, then average the scores the horse got from all judges.
3. **Subtract.** Bias is the judge's average minus the all-judge average. A negative number means the judge placed the horse better than the other judges did. A positive number means worse.

One fix matters here. My scraper usually captures only the top 15 placings per class, even in a class of 200. A judge might have ten captured rows in a class where their lowest recorded placing is 52nd. If I scored that against the ten rows I happened to have, the result would land way off the 0 to 1 scale. So I score against the class's own placing count from the Combined Judges results, and I throw out any row whose placing is outside that range. That drops 43,968 of 1,018,114 judge rows (4.32%), the ones where the scrape cut off partway through a class. It's why the extremes here are smaller than in earlier versions of this page.

---

## How often does bias show up?

Not often. The average pair is off by 0.103. Half of all pairs are off by less than 0.082, and 90% by less than 0.220. A gap that size is normal noise between judges.

The bigger gaps are rare:

| Gap of at least | Pairs | Share of all 68,059 |
|---|---|---|
| 0.20 | 8,931 | 13.1% |
| 0.30 | 2,209 | 3.25% |
| 0.40 | 433 | 0.64% |
| 0.50 | 63 | 0.09% |

About one pair in a thousand is off by half the class or more. That share has also held steady as the data grew. When this page covered 8,145 pairs, 13.1% had a gap of 0.20 or more. At 68,059 pairs, it's still 13.1%. If judges were broadly playing favorites, I'd expect that number to move. It hasn't.

<svg viewBox="0 0 560 140" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Share of pairs with a bias gap above each threshold">
  <line x1="60" y1="100" x2="500" y2="100" stroke="#9aa3ae" stroke-width="1"/>
  <g font-size="11" text-anchor="middle">
    <rect x="100" y="34" width="60" height="66" fill="#d0a65e"/>
    <text x="130" y="26" fill="#c9ced6">13.1%</text>
    <text x="130" y="116" fill="#9aa3ae">0.20+</text>
    <rect x="220" y="84" width="60" height="16" fill="#d0a65e"/>
    <text x="250" y="76" fill="#c9ced6">3.25%</text>
    <text x="250" y="116" fill="#9aa3ae">0.30+</text>
    <rect x="340" y="97" width="60" height="3" fill="#c0392b"/>
    <text x="370" y="89" fill="#c9ced6">0.64%</text>
    <text x="370" y="116" fill="#9aa3ae">0.40+</text>
  </g>
  <text x="60" y="134" fill="#9aa3ae" font-size="11">Share of the 68,059 pairs at or above each gap. Only 63 pairs (0.09%) reach 0.50.</text>
</svg>

---

## What the extreme cases look like

Two patterns show up at the far end.

**Same result every time.** In 400 pairs, the judge won that horse every single time they met. In 137 pairs, the judge placed that horse last every time. That's 0.59% and 0.20% of all pairs. It's the strongest version of bias this measure can show, and it's still under 1% of pairs.

**Bias goes both ways, and the bigger gaps are against the horse.** Of the 100 largest gaps, 58 are a judge placing a horse worse than other judges did, and 42 are better. The single largest gap is +0.737, a judge placing a horse about three-quarters of the class lower than its average. The largest gap in the horse's favor is −0.655. So bias in this data is just as likely to be a judge marking a horse down as a judge favoring one.

> **This is a reason to look closer, not proof of anything.** With 781 judges and 68,059 pairs, some big gaps will show up by chance even if no judge favors anyone. The typical pair in the top 100 met only 6 times, and none more than 9. A judge who keeps placing the same horse first may be seeing the same quality the other judges see.

---

## Do some judges score higher than others?

Separate from bias toward a horse is whether some judges just score higher or lower overall. The database has 10,306,088 scored maneuvers across 43 disciplines, with an average maneuver score of 0.329. Disciplines don't use the same scale, so I compare judges only within their own discipline:

| Discipline | Average maneuver score | Maneuvers |
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

A Reining judge averaging 0.009 isn't stingy. Reining is scored on a different scale than Showmanship. The chart below compares each judge to their own discipline's average, using the 3,109 judge and discipline combinations with at least 200 scored maneuvers each (659 judges).

<svg viewBox="0 0 560 180" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Judge scoring level compared to their discipline average, 3,109 judge and discipline combinations">
  <line x1="335" y1="60" x2="335" y2="135" stroke="#9aa3ae" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="335" y="150" text-anchor="middle" fill="#9aa3ae" font-size="11">discipline average (0)</text>
  <g stroke="#c9ced6" stroke-width="2">
    <line x1="114" y1="95" x2="185" y2="95"/>
    <line x1="362" y1="95" x2="451" y2="95"/>
    <line x1="114" y1="85" x2="114" y2="105"/>
    <line x1="451" y1="85" x2="451" y2="105"/>
    <line x1="272" y1="78" x2="272" y2="112" stroke-width="3"/>
  </g>
  <rect x="185" y="78" width="177" height="34" fill="#6a9e78" fill-opacity="0.35" stroke="#6a9e78" stroke-width="2"/>
  <g fill="#c9ced6" font-size="11" text-anchor="middle">
    <text x="114" y="70">−0.334</text>
    <text x="185" y="70">−0.226</text>
    <text x="272" y="70">−0.094</text>
    <text x="362" y="70">+0.042</text>
    <text x="451" y="70">+0.176</text>
  </g>
  <g fill="#9aa3ae" font-size="10" text-anchor="middle">
    <text x="114" y="56">10th pct</text>
    <text x="185" y="56">25th</text>
    <text x="272" y="56">middle</text>
    <text x="362" y="56">75th</text>
    <text x="451" y="56">90th pct</text>
  </g>
  <text x="20" y="24" fill="#c9ced6" font-size="12">Judge average minus discipline average, 3,109 judge and discipline combinations</text>
  <text x="20" y="172" fill="#9aa3ae" font-size="11">The box holds the middle half of judges. The line inside it is the middle judge.</text>
</svg>

- **Most judges stay close to their discipline.** The middle half fall between −0.226 and +0.042. And 68.1% score below their discipline's average, so slightly tougher than average is the more common side.
- **The extremes look like data problems.** The highest combination sits 2.87 above its discipline's average and the lowest sits 0.81 below. A 2.87 jump in a discipline that averages under 0.4 points to a judge or a results feed recording scores on a different basis, not a generous judge. The middle of the chart is the part I trust.
- **It does change how you read scores.** A typical judge can be about a quarter point off their discipline's average, so comparing raw scores between different judges' classes doesn't work well. That's why the bias numbers above score each placing within the judge's own field.

---

## What I took from this

1. **Favoritism is rare.** The typical pair is about even (average gap 0.103), and the share of pairs with a big gap stayed at 13.1% while the data grew eightfold. That's what I'd expect if big gaps belong to specific pairs and not to judging in general.
2. **When it shows up, it's specific.** The big gaps are a few hundred pairs where a judge keeps winning or sinking one horse, almost all based on 5 to 9 meetings. They stand out because they're so far from everyone else.
3. **Scoring level is its own effect.** Judges run about 0.2 above or below their discipline's average, which is enough to make raw score comparisons between judges unreliable.
4. **Bias runs in both directions.** The largest gap is a judge marking a horse down (+0.737), and the largest gap in a horse's favor is −0.655.
5. **The data needed fixing first.** 4.3% of judge rows can't be scored on a 0 to 1 scale at all, because the scrape only captured part of the class for that judge. Ignoring the class's real size produces gaps that look dramatic and mean nothing.

---

## What's not here

- **Trainers.** Only a small share of results list a trainer, which isn't enough to say anything.
- **Owners and exhibitors.** I have these numbers but left them out to keep this post about patterns, not people.

---

*This is one of a series of posts built on my equine-data results database, a personal AQHA show-results explorer that analyzes every class I've collected.*
