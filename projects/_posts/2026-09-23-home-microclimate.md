---
layout: post
title: A Month Inside My Home's Microclimate (and 5 Days in a Camper)
subtitle: 32 days of minutely readings from two Raspberry Pis — a house that holds inside 8.5 °F, a daily cycle that barely exists, and a surprise about which gap in the data was the biggest
category: Project
tags: [Monitoring, Raspberry Pi, Data, Homelab, Sensors, Climate]
comments: true
thumbnail-img: /projects/assets/images/micro-03-heatmap.png
---

# A Month Inside My Home's Microclimate (and 5 Days in a Camper)

A Raspberry Pi Zero in my house has been reporting ambient temperature and humidity every minute for a month. It's a tiny thing — a $15 board and a cheap DHT22 sensor — but it never stops, so it produces the kind of record you can't get by checking a thermostat twice a day.

Then, without meaning to, I ran an experiment. The Pi came with me in a camper to Raleigh, North Carolina for five days in early September. It kept recording the whole time. That gives the same sensor, the same wiring, the same calibration, in two completely different environments — and it turns out the camper days are the most interesting part of the data.

So here's a month: **27 days in the house, 5 days on the road, 37,000+ readings.**

## The month at a glance

![Daily temperature range in the house, with the camper days shown in yellow](/projects/assets/images/micro-01-band.png){: .mx-auto.d-block :}

*The blue band is the house's daily min–max, with the mean as a line. The yellow dotted line is the raw sensor output on the five days it was in a camper instead.*

The first thing that jumps out is how little the house moves. Over 27 days it stayed between **67.8 °F and 76.3 °F** — a total span of **8.5 °F** across a month where the weather outside was doing its own thing entirely.

The second thing is the gap where the camper is. Those five days are plotted raw, minute by minute, because a daily average would hide what's actually going on: the readings swing much harder, as you'd expect from a small box with no real climate control in the September sun.

| | Readings | Min | Mean | Max | Range |
|---|---|---|---|---|---|
| House (27 days) | 31,429 | 67.8 °F | 72.4 °F | 76.3 °F | **8.5 °F** |
| Camper (5 days) | 5,773 | 66.7 °F | 73.3 °F | 79.9 °F | **13.1 °F** |

Here's the part I didn't expect: **the camper wasn't hotter on average.** Its mean was 73.3 °F against the house's 72.4 °F — less than one degree apart. What changed wasn't the average temperature, it was the *stability*.

## The house barely has a day

Most temperature data has an obvious rhythm: cool before dawn, warm in the afternoon. Mine doesn't, and that's the finding.

![Average temperature by hour of day, house versus camper](/projects/assets/images/micro-02-rhythm.png){: .mx-auto.d-block :}

Averaged across all 27 house days, the difference between the coolest hour of the day (07:00, 71.6 °F) and the warmest (12:00, 73.8 °F) is **2.2 °F**. The overnight-to-daytime difference is even smaller: **1.4 °F** between the sleep window and the working day. The shaded band shows the 10th–90th percentile for each hour — on a typical day, the house sits in a window barely two degrees wide.

The camper, same sensor, shows a **6.2 °F** swing across the day — nearly three times as much — with a morning trough and an afternoon peak that actually look like a daily cycle.

Two explanations are plausible and I can't separate them from this data alone: the house is conditioned, so something is actively flattening the curve, and the camper is a small, mostly sealed box in the sun. Either way, the practical upshot is that **my indoor climate is driven by weather, not by time of day.** The warmest day of the month (September 19, mean 73.3 °F) and the coolest (September 7, mean 69.6 °F) are five degrees apart, while every single day looks nearly identical hour to hour.

## Every minute of the month

![Heatmap of temperature by day and hour](/projects/assets/images/micro-03-heatmap.png){: .mx-auto.d-block :}

This is the chart I'd frame if I had to pick one. Each row is a day, each column an hour, and colour is temperature. The house rows are almost featureless — that's the point. You can see the whole month drift slightly warmer through mid-September and then cool off, but there are no dramatic bands, no hot afternoons, no cold nights.

The five dashed rows — September 2 through 6 — are the camper, and you can read the difference directly: colour that changes as you move right across the row, warm evenings, and a couple of genuinely hot afternoons peaking at **79.9 °F**.

I've kept those rows visible on purpose. They're real measurements from a real device, they just aren't measurements of my house, and a chart that quietly dropped them would be lying about what the sensor saw.

## Two climate knobs, moving independently

Temperature isn't the whole story. The same sensor reports relative humidity, and it behaves completely differently.

![Daily temperature range and humidity range over the month](/projects/assets/images/micro-04-knobs.png){: .mx-auto.d-block :}

Humidity wandered between **40 % and 68 %** over the month — a much wider relative swing than temperature — without any obvious pattern. And when I compared it minute by minute against temperature across all 31,000+ house readings, the correlation is essentially **zero (r ≈ 0.03)**.

That's worth pausing on, because outdoors, temperature and relative humidity are famously inversely correlated: warmer air can hold more water, so relative humidity drops when temperature rises. Indoors, that relationship has vanished. Something in the space is managing moisture independently of temperature — the two metrics are just… separate knobs. If I'd only looked at temperature I'd have assumed a calm, stable climate; the humidity data says the indoor environment is far more variable than the temperature line suggests.

## The biggest gap in the data was between my own two sensors

Finally, I have a second Raspberry Pi with the same DHT22 setup reporting from elsewhere in the house, so the two can be compared directly on the same minutes.

![Daily mean temperature from two sensors in the same house](/projects/assets/images/micro-05-crosscheck.png){: .mx-auto.d-block :}

Over 26,700 aligned minute-pairs they differ by **4.9 °F on average** — and on the extreme end they're **10.3 °F** apart. That's larger than the house's own 2.2 °F daily swing, larger than the differences between many of the days, and not far off the entire 8.5 °F month.

Think about what that means. The indoor climate doesn't have a temperature; it has a *distribution*. Where you stand matters — a south-facing room, a second floor, or a spot near a vent can easily read 5 °F differently from another spot in the same building, and that's bigger than whether it's 7 in the morning or noon. I don't know exactly where the divergence comes from in my case — placement, height, airflow, sun exposure are all in play — but the scale of it is the real lesson: **a single sensor is a sample, not a truth.** This is also a reminder that my "house temperature" numbers above are really "the temperature *at the sensor*", and the second device is doing exactly its job by disagreeing.

## What a month of this is worth

None of this required anything exotic: a couple of cheap Pis, a DHT22 each, a small time-series database, and a dashboard I rarely look at. The value isn't the monitoring in real time — it's that a month later I can answer questions I didn't ask at the time:

- Is the house actually stable? Yes — 8.5 °F over a month, and barely a daily rhythm.
- Does HVAC-style conditioning show up in the data? It looks that way, though an air conditioner is only hearsay from here.
- What does "comfortable" mean numerically? 67.8–76.3 °F at the sensor, 40–68 % humidity, with the caveat that a second sensor 5 °F away is telling a different story.

And the accidental experiment: the 5 days in the camper turned out to be the most informative five days on record, not because the environment was extreme, but because the *same instrument* made the comparison explicit.

The sensor is still running. Next winter's data should be interesting.

---

*All readings are minute-precision from a Raspberry Pi Zero (DHT22 ambient sensor, 32-day window ending September 23, 2026). The five camper days (September 2–6, Raleigh, NC) are excluded from every house statistic and kept visible in the charts where noted. Humidity and temperature values are raw sensor output — a cheap sensor, honest about its tolerances.*
