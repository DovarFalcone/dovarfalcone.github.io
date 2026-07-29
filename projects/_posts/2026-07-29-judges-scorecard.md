---
layout: post
title: Judges Scorecard 🐴
subtitle: A mobile-first, offline-capable scorecard for AQHA horse-show judges
category: Project
gh-repo: DovarFalcone/judges-scorecard
gh-badge: [star, fork, follow]
tags: [Project, AQHA, Judging, Scorecard, Mobile, TypeScript, React, Capacitor]
comments: true
---

# Judges Scorecard 🐴

A mobile-first, offline-capable scorecard for **AQHA horse-show judges**. Create classes, drop in exhibitors by back number, score each maneuver on the universal AQHA −1.5 → +1.5 scale, and apply **class-type-specific penalties** (Reining, Ranch Riding, Trail, Ranch Trail, Western Riding, etc.) — all backed by a real 2026 AQHA rulebook you can search from inside the app. Placings are computed automatically once scoring is done.

![Judges Scorecard screenshot]({{ site.url }}/projects/assets/images/judges-scorecard-icon.svg)

## Features

- **Quick Class creation** — name + class type + ⚡ Quick Card (specify number of maneuvers). No pattern needed to start.
- **Class-type penalty profiles** — penalty buttons adapt to the class:
  - Reining → `0.5 / 1 / 2 / 5` + a ±0.5 stepper (out-of-lead accumulates per ¼ circle)
  - Ranch Riding → `1 / 3 / 5 / 10` (10 = unnatural appearance)
  - Trail / Ranch Trail → `0.5 / 1 / 3 / 5`
  - Western Riding, Western Pleasure, Showmanship, Equitation, Horsemanship → `1 / 3 / 5`
  - Generic (fallback) → `0.5 / 1 / 3 / 5 / 10`
- **Maneuver scoring** on the AQHA base-70 scale (−1.5 … +1.5 per maneuver).
- **Exhibitor entry by back number**, with a ✎ rename for the rider name.
- **Auto placings / leaderboard** — ranked by total score with top-3 highlighted.
- **In-app rulebook** — full-text search of the 2026 AQHA rulebook, filterable by class, lazy-loaded so it never slows startup.
- **Offline persistence** via SQLite (Capacitor on mobile, IndexedDB-less local store on web).

## Installation

```bash
git clone https://github.com/DovarFalcone/judges-scorecard.git
cd judges-scorecard
npm install
npm run dev      # http://localhost:5173
```

### Production build

```bash
npm run build    # tsc -b && vite build  -> dist/
npm run preview  # serve the build locally
```

### Mobile (iOS / Android)

```bash
npm run build
npx cap add ios        # or: npx cap add android
npx cap sync           # copies dist/ into the native project (webDir: 'dist')
npx cap open ios       # open in Xcode / Android Studio
```

> Requires the Capacitor CLI and the native toolchains. `capacitor.config.ts` already targets `webDir: 'dist'`.

## Updating the rulebook

The searchable rulebook (`public/rulebook.json`) is generated from the 2026 AQHA rulebook text by a script:

```bash
# drop the rulebook text at scripts/aqha_2026_rulebook.txt, then:
python3 scripts/build_rulebook.py
```

This reparses the source into category-filtered, searchable entries. Re-run whenever the rulebook changes.

## Project layout

```
src/
  components/        UI (ClassModal, PatternModal, ScoreInput, InputModal,
                     PlacingsPage, RulebookView, ...)
  data/
    penaltyProfiles.ts   class-type penalty profiles (grounded in SHW rules)
  store/
    useScoreStore.ts     Zustand store + actions
  services/
    DatabaseService.ts   SQLite persistence
public/
  rulebook.json          generated, searchable 2026 AQHA rulebook
scripts/
  build_rulebook.py      rulebook text -> rulebook.json
  aqha_2026_rulebook.txt source text
```

## Making updates

The app is a static SPA with no backend, so deploys are just a rebuild + restart on the server.

Typical loop:
1. Edit code locally and test with `npm run dev` (instant HMR — no deploy needed for testing).
2. Commit + push to the private repo for history.
3. Deploy with one command:
   ```bash
   ./deploy.sh
   ```
   This builds locally (fails fast if anything breaks), syncs the source to the server (`10.0.0.26`), and rebuilds + restarts the container. Cloudflare picks up the new build automatically — no tunnel restart needed.

`deploy.sh` requires SSH access to the server (key at `~/.ssh/hermes_to_100026`). Adjust `SERVER` / `SSH_KEY` in the script if your setup differs.

## Tech notes

- **Base score** defaults to 70 (AQHA standard) and is auto-filled from the class type.
- **Class type** is set at class creation and inherited from the pattern when one is reused.
- The rulebook view fetches `rulebook.json` on first open only.

## Live Demo & Source Code

- **Live Demo**: https://scorecards.maradara.com
- **Source Code**: https://github.com/DovarFalcone/judges-scorecard

---