---
layout: post
title: A Reversed CPU Fan Cost My Server 4°C 🌡️
subtitle: A 72-hour temperature chart, one wrong hunch about airflow, and the numbers that settled it
category: Project
tags: [Homelab, Unraid, Grafana, InfluxDB, Telegraf, Cooling, Data Analysis]
comments: true
thumbnail-img: /projects/assets/images/unraid-cpu-fan-reflip.png
---

# A Reversed CPU Fan Cost My Server 4°C

My home server — an Unraid box running an Intel i5-13400 under a low-profile Thermalright AXP120-X67 cooler — reports everything: Telegraf ships CPU, sensor and disk telemetry into InfluxDB, and I watch it in Grafana. So when the machine started running warmer, the interesting question wasn't *whether* it was warming up. It was *why*, and whether the data could settle it.

It could. The answer cost me 4 °C, and the fix was one screwdriver turn.

## The observation

I pulled the last 72 hours of CPU core temperatures into a single chart. One thing stood out immediately: a clean step up to a new, **persistent** baseline on Monday afternoon.

![Unraid CPU core temperatures over 72 hours](/projects/assets/images/unraid-cpu-72h.png){: .mx-auto.d-block :}

Before that moment, the package sat around **42 °C**. After it, **46 °C** — and it never came back down. Something physical changed at that timestamp, and I had a strong suspicion what: shortly before, I had flipped the cooler's fan so it blew **away** from the fin stack instead of **into** it. My reasoning was that pulling heat off the cooler would help it escape. That reasoning was wrong, and the chart was about to prove it.

## The trap: comparing raw CPU temperature

The obvious analysis — "the CPU is 4 °C hotter now" — proves almost nothing, because absolute CPU temperature moves with two things that have nothing to do with your cooler: **how busy the CPU is**, and **how warm the room is**.

To isolate the cooler I switched to a different metric: **CPU temperature minus room temperature**, at matched load. The room sensor is a separate Raspberry Pi in the same room, so it's an independent measurement, and the CPU load is logged alongside.

That changes the story completely.

| Variable | Before (Sun → Mon 13:45) | After (Wed 02:00 → 09:00) | Change |
|---|---|---|---|
| CPU package | 42.0 °C | 44.9 °C | +2.9 °C |
| Room temperature | 24.2 °C | 23.0 °C | −1.1 °C |
| **CPU − room (cooling delta)** | **17.8 °C** | **21.9 °C** | **+4.1 °C** |
| CPU load | 1.9 % | 2.1 % | flat |

Read the middle rows together and the conclusion is unavoidable. The room got **colder** by more than a degree, the load didn't change, and the CPU still ran **hotter**. The gap between the CPU and the room — the part the cooler is responsible for — grew by **4 °C**: a ~23 % increase in thermal resistance, while essentially idle.

![CPU temperature, room temperature, and the cooling delta](/projects/assets/images/unraid-cpu-cooling-delta.png){: .mx-auto.d-block :}

Two things kept this from being a story about a bad sensor. First, the step appears independently in the board's own PECI reading of the CPU, which rose 3.3 °C at the same minute — a different sensor, the same verdict. Second, a scheduled parity check ran later that Monday and pushed the package to 48 °C, which is the busiest the box got — but the elevated baseline *stayed* elevated for a day and a half after the check finished. Workload explains a bump during a job. It does not explain a new normal that outlives it.

For context: at 48 °C peak this was never a danger — these chips throttle around 100 °C. It was a *cooling* problem, not a *thermal emergency*.

## Why blowing away from the fins is worse

A heatsink isn't a flat plate with air waved at it. It's a stack of narrow channels. For fins to shed heat efficiently, air has to be driven **through** those channels at speed, scrubbing the fin surfaces — which is exactly what a fan blowing *into* the stack does: it pressurizes the top and forces air down through every gap.

Reverse the fan and you ask it to do the harder job of **pulling** air through that same restrictive stack. Axial fans are not symmetric — they move measurably less air when sucking against a dense fin stack than when pushing into it. Two more penalties come along for free: the fan now draws its intake from the sides of the cooler, where the air has already been warmed by the fins and the board, and the downward wash of air that also cooled the VRM, RAM and socket area is gone.

Net effect: less air through the fins, warmer air going in, and a few degrees lost. Nothing gained.

## The fix

I put the fan back to blowing into the fins. Within about fifteen minutes, at the same load and the same room temperature:

| Variable | Before flip-back | After (~13 min) | Change |
|---|---|---|---|
| CPU package | 44.6 °C | 38.7 °C | **−5.9 °C** |
| CPU − room (cooling delta) | 21.8 °C | 16.2 °C | **−5.6 °C** |
| CPU load | 2.2 % | 2.2 % | flat |

![Before and after re-flipping the CPU fan](/projects/assets/images/unraid-cpu-fan-reflip.png){: .mx-auto.d-block :}

That doesn't just undo the regression — the machine now idles *below* the baseline it had before I ever touched the fan, most likely because the reseat improved how the fan mates with the fin stack.

## What I took from it

- **Monitor the delta, not the absolute number.** CPU temperature minus ambient, at matched load, isolates the cooling system from the workload and the weather. It's what turned a vague "feels warmer" into +4.1 °C with a timestamp on it.
- **A persistent step means something physical changed.** When a temperature chart steps up and *stays* up, suspect hardware and airflow — dust, thermal paste, a reseated cooler, a fan direction — not a mysterious background process.
- **Cheap telemetry is worth it.** Catching this, confirming it against a second sensor, and verifying the repair took one morning and required no guessing. The whole investigation is three charts and two tables.

And the most mundane lesson: **fans push better than they pull.** Low-profile top-down coolers are designed around the fan blowing air into the fins — the arrow stamped on the fan frame is not decorative.

---

*Kit: Unraid server (Intel i5-13400) with a [Thermalright AXP120-X67](https://www.amazon.com/dp/B09TGSCHYV) low-profile cooler; Raspberry Pi room-temperature sensor; Telegraf → InfluxDB → Grafana for the telemetry.*
