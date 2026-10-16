---
layout: post
title: Where Pattern Classes Are Won and Lost
subtitle: The maneuvers that separate the top three from the rest of the class, and the penalties that cost the most
category: Project
tags: [Project, AQHA, Data Analysis, Horse Show, Equine]
comments: true
---

A pattern class comes down to a handful of maneuvers. I wanted to know which ones separate the top three from everyone else, and which ones cost riders the class through penalties.

I compared maneuver scores in 12 disciplines that score each maneuver, across 619 combinations of discipline and maneuver with at least 20 scored riders each. The biggest gap between the top three and the rest of the class is "180, B, 540" in Showmanship. The top three average +1.52 points on it and everyone else averages −0.39, a gap of 1.91 points.

*Based on 191,605 placings and 1,896,539 scores. Numbers refreshed September 22, 2026.*

> **Updated September 27, 2026.** The August version ran on 424 maneuvers and 1,080,007 scores. Adding more shows grew that to 619 and 1,896,539. The "where classes are won" results held up: the same Showmanship maneuver still leads with the same 1.91-point gap, and Showmanship and Horsemanship still fill the top of the list. The penalty section changed. It now shows the top 8 per discipline with at least 30 riders each, instead of one list across all disciplines with at least 200, and the biggest average penalties turned out to be on Showmanship's technical maneuvers, not Trail.

---

## Where pattern classes are won

For each rider and maneuver, I averaged the scores from all of that rider's judges. Then I compared the average for riders who placed 1st through 3rd with the average for everyone else. A positive gap means the top three outscored the rest of the class on that maneuver. These are the ten biggest gaps. Maneuver names are written the way they appear on the scoresheet.

| Maneuver | Discipline | Top 3 average | Rest of class | Gap | Riders |
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

Showmanship and Horsemanship take most of the list, and the biggest gaps are on turns like the 540s and 180s. That's the technical work where the top riders pull away from the class.

---

## Where classes are lost

For penalties I looked at two things per maneuver: the share of riders who got at least one penalty, and how many points those riders lost on average. A rider counts as penalized if any of their judges gave a penalty. These are the highest penalty rates, all from Trail:

| Maneuver | Discipline | Penalized | Riders | Rate | Average points lost |
|---|---|---|---|---|---|
| W, SP L, W | Trail | 31 | 36 | **86%** | 1.70 |
| Jog, Stop | Trail | 28 | 33 | 85% | 0.69 |
| WALK BOX/POLES | Trail | 35 | 41 | 85% | 0.86 |
| J, JOs, S | Trail | 24 | 30 | 80% | 1.05 |
| JO | Trail | 38 | 50 | 76% | 0.58 |
| Chng, LL L | Trail | 23 | 31 | 74% | 1.11 |
| W | Trail | 145 | 210 | 69% | 0.97 |

<svg viewBox="0 0 560 170" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Penalty rate by maneuver">
  <line x1="150" y1="16" x2="150" y2="132" stroke="#9aa3ae" stroke-width="1"/>
  <g font-size="11">
    <text x="140" y="39" text-anchor="end" fill="#c9ced6">W, SP L, W</text>
    <rect x="150" y="26" width="154" height="18" fill="#d0a65e"/>
    <text x="310" y="39" fill="#c9ced6">86%</text>
    <text x="140" y="65" text-anchor="end" fill="#c9ced6">Jog, Stop</text>
    <rect x="150" y="52" width="152" height="18" fill="#d0a65e"/>
    <text x="308" y="65" fill="#c9ced6">85%</text>
    <text x="140" y="91" text-anchor="end" fill="#c9ced6">WALK BOX/POLES</text>
    <rect x="150" y="78" width="152" height="18" fill="#d0a65e"/>
    <text x="308" y="91" fill="#c9ced6">85%</text>
    <text x="140" y="117" text-anchor="end" fill="#c9ced6">180, B, 540</text>
    <rect x="150" y="104" width="65" height="18" fill="#6a9e78"/>
    <text x="221" y="117" fill="#c9ced6">36%, average 6.94 points lost</text>
  </g>
  <text x="150" y="150" fill="#9aa3ae" font-size="11">Share of riders penalized (tan = Trail, green = Showmanship)</text>
</svg>

Trail has the most penalties. On some Trail maneuvers almost nine in ten riders get one, though those numbers come from small groups of 30 to 41 riders. The penalties that cost the most are in Showmanship. Only 36% of riders get penalized on "180, B, 540", but those who do lose 6.94 points on average, the largest average penalty in the data. The next biggest are also Showmanship and Horsemanship technical maneuvers:

| Maneuver | Discipline | Rate | Average points lost | Riders |
|---|---|---|---|---|
| 180, B, 540 | Showmanship | 36% | **6.94** | 102 |
| RL | Horsemanship | 7% | 5.91 | 340 |
| 450 | Showmanship | 32% | 5.47 | 203 |
| 1 3/4 | Showmanship | 41% | 4.87 | 51 |
| XJ, S | Horsemanship | 15% | 4.86 | 151 |
| 270, T | Showmanship | 25% | 4.77 | 386 |

The Showmanship turns that separate the winners are also where a mistake costs the most. Trail penalties are common but small. Pattern-class penalties are less common and much bigger.

---

## How I did it

1. **One score per rider.** The scoresheet data has a row for every exhibitor, judge, and maneuver, so I averaged each rider's score for a maneuver across their judges before comparing anything.
2. **Top three against the rest.** Placings come from the Combined Judges results for the same class. Riders who placed 1st through 3rd are the top group, and everyone else is the rest of the class. The gap is the top-three average minus the rest-of-class average.
3. **Which maneuvers count.** Each discipline and maneuver combination needs at least 20 scored riders for the gap table and 30 for the penalty tables. Today 619 qualify for gaps (up from 424 in August) and 544 for penalties.
4. **Penalties.** A rider counts as penalized when any judge's penalty isn't zero. The points lost are averaged across that rider's judges, then across penalized riders only.

**Before you quote any of this:**

- **Scores aren't adjusted between classes.** Judges, pattern difficulty, and scoring scales differ, so comparing gap sizes or penalties between disciplines isn't apples to apples.
- **Penalty rate and penalty size are different things.** Trail leads the rate table on small groups. Showmanship leads the size table. A 36% rate with 6.94 points lost costs a rider far more than an 86% rate with 1.70 points lost, so read both columns.
- **A negative gap isn't an error.** If the top three score below the rest of the class on a maneuver, that maneuver is usually separating the class by difficulty, not skill.
- **This shows patterns, not causes.** Which riders enter which classes and how judges mark both shape these numbers. Treat the tables as a map of where to look, not proof of what wins.

---

*This is one of a series of posts built on my equine-data results database, a personal AQHA show-results explorer that analyzes every class I've collected.*
