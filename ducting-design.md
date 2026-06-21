# Refrhus HVAC / ducting redo — design seed

Seed doc for a fresh session to brainstorm → spec the **new ducting** arc. Harvested from the Trello card "Prepare basement corner wall for powerwall etc" (description + 50 measurement comments, now deleted — content distilled here) plus the warm 2026-06 modeling context. Read `HISTORY.md` (house ground truth) and `scanning-plan.md` (the scan path) first.

## Why this arc exists

HVAC was the original itch behind the whole git-native house effort: sketch a **new** duct layout and diff/PR it against the current ("PR your house"), instead of awkwardly tagging a ton of speculative boxes onto the as-built model. The first concrete deliverable is a **proof-of-concept new-duct layout on its own branch** (e.g. `ducts/poc` off `main`). Accuracy is NOT required for the PoC — the point is to prove the workflow (branch = proposal, diff = the change, merge when built) and rough out the scheme. The real HVAC contractor (DK Mechanical, Dkmechanical.llc@gmail.com — to receive an SH3D export alongside the plumber) refines from there.

Rough cost rule of thumb captured for sizing intuition: spiral duct ≈ diameter × 2 × length in dollars (6in × 2 × 5ft ≈ $60, ~$12/ft), from airhand.com — order-of-magnitude only.

## Current (as-built, approximate) basement ducting

The basement ducts are roughly modeled in `main` already; treat positions as ±. Measured reference points from the card (basement, north-to-south, joists 16in OC, ~26 joist positions from the west/left wall):

- HVAC unit: ~30in from the west wall, 36in across, 24in N–S; ~3in clearance to the water heater; ~108in to the east wall. Chimney 16×16in (24in toward the WH in the basement only), 93in from the south wall.
- Main blower trunk ("monster duct") off the unit: ~30in, then a 14in branch runs west and splits a bump to feed a bathroom vent.
- Main supply trunk into the carpeted (home-theater) half: 13in wide at the start → 9in after the living-room branch splits → 5in near the garage-side split.
- First ducts ~8ft south of the north wall: a 4in (kids-room blower) and a 5in (bedroom blower).
- An AC duct splits ~42in along to feed the **2nd floor** (≈12in, then ~10in for the 2nd-floor branch); double duct ~14in off the north beam feeds a kitchen/living-room vent combo.
- Beams/poles: the north (main) beam hangs ~5in below joists, the south beam ~10in; these constrain clear height for any new runs.

(Full joist-by-joist equipment map — old terminated office duct between joists 1–2, kids-room vent 2–3, sump-pump drain at 3, intake 7–8, supply 9–10, staircase mainbeams 11–16, living-room/front-door intake 17–18, kitchen-wall ducts 23–25 — lives in git history of the deleted Trello export if ever needed at that granularity.)

## The NEW ducting vision (from the card's final design note)

The proposed redo, to sketch on the branch:

- A **"ducting squid"** manifold in a **new false wall / closet just south of the chimney**. From it: four ducts east along the ceiling (two run N–S, two toward the wall) + three ducts south into the walls heading up to the **2nd-floor knee-wall attic for AC**.
- A basement **intake on the far side of the main beam** (near where the table/stairs go up), serving that side of the basement.
- From the chimney's other side: two ducts — one to the **upstairs bathroom**, one running behind the false wall / bookcases to the **north wall with a cold diffuser**.
- Home-theater (carpeted) side: keep the one existing upstairs vent + the living-room intake brought out the other side of the stairs; add one more duct toward the utility side with a ceiling diffuser.
- Target pattern for the basement itself: **~3 blowers + 2 intakes**, with cold diffusers up high and intakes positioned to circulate.

## The utility-corner build (adjacent, partly done / planned)

The card's primary subject — the SW utility corner being prepped for a Tesla Powerwall (PW2, 45in tall × 30in wide) on plywood over 2–3 studs, with fiber modems above, a long electrical/span panel (40in × 14in) to the left, and network gear on the right. The "lip board" geometry (8in cinderblock upper / 12in lower with a ~4in ledge) ties into the basement-ledge modeling item already noted in `HISTORY.md`. Ducts must route around this corner build. Lower priority than the duct scheme itself, but they share the same wall.

## Known unknowns / measurement gaps a scan would close

- **The orphan duct**: an old duct runs basement → 2nd floor and **dead-ends under flooring added later**. Its exact location is wanted to ~1in — a prime targeted-scan/measure objective (see `scanning-plan.md`). For the PoC it can be approximate.
- Basement internal accuracy generally (poles, beams, exact duct positions) is approximate and a scan-data candidate rather than more manual guessing.
- 2nd-floor attic routing depends on the (incomplete) 2nd-floor model — also scan-gated.

## What a fresh session should brainstorm → spec

1. **Scope of the PoC** — which subset to model first (likely the basement squid + the 3-up-to-attic AC runs, since that's the clearest win), and confirm "rough is fine."
2. **How to represent ducts in SH3D** — boxes/cylinders as furniture at per-run elevations within a level, vs. a convention worth standardizing (ties into the parked `sh3d-geometry` tooling). Ducts carry their own small elevation *within* a level; that's the one place height matters here.
3. **Branch/diff workflow** — confirm `ducts/poc` off `main`, current ducts stay in `main` as as-built, the branch shows the proposed scheme; merge when (if) built. This is the literal "PR your house" demo.
4. **What to hand the contractor** — an SH3D export + this scheme; what level of detail DK Mechanical actually needs.
5. **Sequencing vs scans** — what's worth sketching now vs. waiting on scan data (orphan duct, attic routing).

Suggested arc id: `refrhus-ducting`. Parent context: the `sweethome3d` arc.
