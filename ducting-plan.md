# Refrhus ducting — working design plan

Living design/spec doc for the new-HVAC arc (`refrhus-ducting`). This is the **forward-looking plan**; the harvested as-built reference stays in [`ducting-design.md`](ducting-design.md) (Trello seed) and [`HISTORY.md`](HISTORY.md) (construction ground truth). Source cards now recovered on disk: `descent-into-chaos.json` (original, 50 measurement comments) and `minioverhaul.json` (the minimal-reuse approach). Floor-plan images: `OriginalFloorPlan.png`, `OriginalPlanHVAC.png` (garage-unit v1), `LargerFloorplanMudroomHvacV2.png` (reuse v2).

Status: brainstorm → spec in progress. The **joist-anchoring pass (§4) is placed roughly** (2026-07-08, `joist-01…25` left→right) and awaits owner re-measurement; the new-duct scheme itself is not yet committed to the model.

---

## 1. How we collaborate on this (the method that actually works)

The hard-won lesson: **ad-hoc spatial schematics and topology diagrams don't survive agent translation** — maps come out wrong, even E/W gets flipped, and Mermaid is great for software architecture but not physical house layout. So:

- **The SH3D model is the collaboration medium**, not prose and not drawn images. It's already spatially correct (walls, rooms, levels at real coordinates), the agent can edit coordinates precisely and diff them, and the human can *see* it and judge spatially. That's the literal "PR your house" loop.
- **Division of labor by strength.** Human supplies spatial truth (measurements, "this register is ~here in this room, nearest joist N"); agent places it precisely in `Home.xml`, keeps naming/elevations consistent, and produces the diff. **The agent never invents positions — it only places, normalizes, and connects what the human specifies.**
- **Anchors before ducts; durability over old-vs-new.** Vent/register *locations* and structural anchors (joists, beams, posts, the unit spot, the conduit hole) are durable and get pinned accurately first, on `main`. The leaky old *duct runs* are disposable and get designed fresh on a branch. Split work by what persists, not by what's existing.
- **Branch/diff workflow.** As-built anchors live in `main`; the proposed new scheme is sketched on `ducts/poc` so the diff *is* the proposal. Merge if/when built. Hand DK Mechanical (Dkmechanical.llc@gmail.com) an SH3D export + this plan; accuracy for the PoC is "rough is fine," the point is to prove the workflow.

Terminology fixed here: a floor/wall **supply** opening is a **register**; a **return** opening is a **grille**.

---

## 2. The chosen scheme: single heat pump under the stairs

Decided direction after walking through the evolution (garage-unit v1 → full-reuse v2 → relocate-under-stairs → brief two-unit flirtation):

- **One heat pump air handler, relocated under the stairs** (ample floor behind the bar — the tight ~33in dimension is only the narrow lip up to the bar counter; there's full-height floor space behind it). Relocating out of the SW utility corner also **frees that corner for the Powerwall build**, which was the original corner-prep goal.
- **Two-unit option (basement + garage/crawlspace) dropped as YAGNI.** Rationale: doubles equipment + maintenance for a workflow demo, and the crawlspace is unsealed/unconditioned (daylight visible from outside, ~3–4ft tall) — a poor home for equipment without air-sealing, condensate, and electrical work first. Revisit only if zoning/comfort proves inadequate.
- **Reuse reality:** the existing duct *runs* are leaky and old — **assume all-new ducting**, reusing register *locations* where they still serve. Two genuine duct-reuse candidates survive: (a) the **orphan duct** on the east-room side running basement → 2nd floor, and (b) the **"dinky" duct by the stairs** that did nothing — possibly revivable.

### Upstairs strategy (the crux — minimizing long runs)

Getting air to the 2nd floor without enormous runs is the whole challenge. Plan:

- **East upstairs room (big bedroom):** reuse the **orphan duct → floor register in the NE corner** (a blower). Then a small set of risers up the **maintenance wall between the front door and the primary bedroom** (see §5) — putting a **return/grille near the door** for that room, plus a **blower pushed down the extended (gabled) end**.
- **West upstairs room:** nearly trivial by comparison — short run, one blower.

**Open item — duct count in the door↔bedroom chase.** Earlier framing was "two ducts up between the front door and the bedroom" (a door-side intake + a gable blower). Latest thinking says **three**. Pin this before sizing the wall cavity in §5 — the depth/width budget depends on it. Likely candidates for the third: a dedicated return, a second supply branch, or a stub for the west room / future need.

### Basement itself

Earlier "squid" target was ~3 blowers + 2 intakes with high cold diffusers and circulating intakes. With the unit now under the stairs (central-ish to the carpeted half), basement runs are short. Detail TBD against the joist grid (§4) — this is where the lost "newest sketch" (exact basement register points + duct counts, including E–W runs along the main beams where you duck your head anyway) gets regenerated directly in the model rather than on paper.

---

## 3. Model facts confirmed (basement)

Extracted from `Home.xml` and cross-checked against the cards — the model is trustworthy for walls:

| Element | Model position (cm) | Thickness | Card cross-check |
|---|---|---|---|
| Exterior wall A | X = 699.04 | 8in | cinder block ✓ |
| Exterior wall B | X = 1722.02 | 8in | cinder block ✓ |
| Interior E–W span | **402.8in** | — | within the 394–414in range you measured ✓ |
| Center / staircase wall | X = 1268.43 | 5in | interior stud wall ✓ |
| North / South walls | Y = 615.07 / 1308.02 | 8in | N–S span 272.8in ≈ 22'8″ ✓ |

The carpeted/bar/stairs half is the one containing the bar counter (x≈1149) and staircase (x≈1216), just inside the center wall; the utility/HVAC half is the other side. (Cardinal labels are deliberately not asserted here — anchoring is done against named walls and furniture, not N/E/S/W, to avoid the repeated E/W-swap mistake.)

---

## 4. Pass 1 — joist + structure anchoring (CONFIRMED 2026-07-08, placed roughly)

Starting skeleton in the `basement-main-transition` layer (before this pass):

- **12 joists** as thin brown `texturableBox` boxes (model `19/texturableBox.obj`), 2in wide × 271in deep (full N–S), at a near-perfect **16in OC** grid from x≈1705 to x≈1268. The final gap is 12in (matches "11 is last normal one, 12in from there to the mainbeam staircase").
- **3 rough placeholders** near the far wall (x≈780/820/861) — "aim points," to be redone.
- 402.8in ÷ 16 ≈ **26 joists** total → ~14 to add across the stair/bar half (incl. the irregular staircase-mainbeam zone).

### The three confirms — answered (2026-07-08)

- **(A) Direction — LEFT→RIGHT.** Number **joist-01 at the west (lowest-x) end, counting east to the highest number** (opposite the earlier x≈1705-first proposal). In the default SH3D plan view, left = smaller x = the stair/bar half; right = larger x = the utility/HVAC half where the 12 existing joists sit.
- **(B) Stair/bar half — lay nominal 16in OC roughly right NOW; owner re-measures.** The card's measurements "roughly match including across the stairs/bar span," so a clean grid is close enough to anchor against; the **staircase-mainbeam zone and the west-wall end bay are the explicit re-measure targets**. No re-walk needed before placing.
- **(C) Beams/posts — already in the model (4 of them); locate + report, don't re-place.** The owner already put 4 beam/post elements on the schematic; their exact positions are in question. The agent **finds them and reports coordinates** so the owner can re-measure them anchored against the now-confirmed joist numbers. (Card ground truth: North Pole + South Pole, ~3.5in dia; North beam hangs ~4–5in below joists, South beam ~9.5–10in; "beam from north wall to North Pole ~86in.")

### What was placed (this pass)

A clean **16in-OC (40.64 cm) grid, anchored at the existing east joist x≈1705.44 and stepping west**, regenerated as named boxes **`joist-01` (west) … `joist-25` (east)** — 25 joists on the clean grid (the card's "≈26" is within re-measure noise; add a 26th at the west wall if a re-measure wants it). The staircase-mainbeam sits between **joist-14 (x≈1258)** and **joist-15 (x≈1299)**; **joist-13…15 + joist-01/02** (west end) are flagged approximate. Element style preserved (brown `19/texturableBox.obj`, 5.08 × 688.34 × 20.32 cm, y≈962.02, transition level). Script: `components/langr/sh3d-scripts/place_joists.py` (regenerates the grid deterministically; re-runnable).

**Still open (Pass 2):** owner re-measures joists in SH3D against the real basement; then re-measures the 4 beams/posts against confirmed joist numbers; then the conduit-hole **shared datum** (§5a) before the `ducts/poc` scheme.

---

## 5. The maintenance wall (front door ↔ primary bedroom) — design review

The wall the upstairs-east risers pass through, and the trickiest build. Constraints from physical exploration:

- Currently **one stud space deep**, with room for **exactly one more stud space inside the bedroom**, thanks to the doubled/offset wall quirk created when the bedroom was extended south.
- Broke in from the bedroom side: saw **2–3 studs** and an **old conduit hole through to the basement**.
- Must carry **~3 vertical ducts** basement → 2nd floor, stay **sturdy when removed/reinstalled**, leave room for the actual ducts, and **read as intentional built-ins from the front door** (shelving, coat hanging, pretty framing, hidden fasteners). Originates from the minioverhaul card's "removable wall piece that looks like built-in framing — unscrew it for future maintenance instead of over-provisioning ducts up front."

### 5a. Use the conduit hole as the datum

The old conduit hole is the gift here: it's a **single point that pierces both the basement and the wall cavity**, so it registers the two coordinate frames against each other — the same shared-anchor trick as the joists. Plan: mark it in the model on both the basement ceiling and the wall, measure the 2–3 observed studs *relative to it*, and reference every riser to it. That converts "I can't tell where the studs are vs. where ducts come up" into exact offsets from one known hole.

### 5b. Fit 3 ducts in a shallow doubled wall — go rectangular, not round

Depth budget ≈ two stud bays back-to-back (~7in, a bit more counting the gap between the two wall planes). Width in a bay ≈ 14.5in clear (16in OC − 1.5in stud). Three **round** 5–6in ducts side-by-side (~15–18in) won't fit one bay cleanly and fight the studs.

**Recommendation: residential "wall-stack" rectangular duct** (e.g. 3.25in × 10in or 3.25in × 12in), purpose-made to run vertically *between* studs in a 2×4 wall. Three wall-stacks distribute across adjacent bays with the shallow (3.25in) dimension fitting the wall depth — solving "shallow cavity + 3 ducts" directly. Oval duct is a fallback with similar shallow-fit benefits. Round only if the count drops or a bay can be widened using the doubled-wall depth (staggering ducts front/back).

Stud-vs-duct conflicts: prefer running each duct **within a bay** (no stud notching). If a riser must cross a stud, treat the wall as the **non-load-bearing partition it most likely is** (verify — the south-extension quirk muddies this) and bore/notch within code, or frame a small header. Confirm the 3-duct count (§2 open item) before finalizing bay assignments.

### 5c. Removable panel — sturdy yet demountable

Three structural strategies, best-to-worst for this job:

1. **Self-supporting cabinet/torsion-box face (recommended).** Build the built-in as a rigid, self-bracing box (face-framed or torsion-box back) so it doesn't rack when lifted off the wall. Attach to studs with a handful of concealed screws. Rigidity = sturdiness; few perimeter screws = removability. Standard cabinetmaker approach to "looks built-in, comes off in one piece."
2. **French-cleat-hung face over permanent backing.** A permanent ledger/cleat strip screwed to the studs; the decorative face hangs in shear on the cleat + a couple of hidden screws at the base. Lifts straight off. Clean, very strong, slightly more depth.
3. **Hinged access door(s) for routine + removable for major.** Concealed European hinges let a section swing open for quick access while the whole unit still unscrews for big work. Adds clearance/fiddliness around the ducts; use only if frequent access is expected.

A combo of 1 + 2 (rigid box hung on a cleat) is the sweet spot.

### 5d. Hidden fasteners + the seam trick

- **Hide screws** inside shelf interiors (behind a removable shelf), behind/under the coat rail, behind a toe-kick/kickplate, in dadoes capped by trim, via pocket screws from the inside, or keyhole hangers + magnetic catches for the truly invisible bits.
- **Put the removable seams on natural trim lines.** Design the face as board-and-batten or stile-and-rail paneling so the panel edges fall on a batten/rail joint — the demountable seam reads as intentional millwork, not an access hatch. This is the single biggest "looks right from the front door" move.

### 5e. Built-ins program (front-door face)

An entry **drop zone**: coat hooks/rail, a bench (the duct chase can hide behind or below the seat back), slim cubbies/shelving, picture-frame or board-and-batten molding to carry the seams. The card's **triangular shelves above/below the adjacent stairs** are a related, separate built-in that can share the visual language. Keep the duct access panel(s) within the paneling grid so the whole wall looks composed.

### 5f. Open items for the maintenance wall

- Lock the **duct count (2 vs 3)** and assign each to a stud bay.
- Confirm the wall is **non-load-bearing** before any stud notching.
- Decide **wall-stack vs oval vs round** once count + bay widths are known.
- Measure the **2–3 studs and conduit hole** relative to the datum, then model them.
- Whether to model this wall now (1st-floor + bedroom + the chase up to 2nd floor) as part of the PoC, or after the basement anchoring + scheme are settled.

---

## 6. Next steps

1. Answer §4 (A/B/C) → agent lays the authoritative joist grid + beams; you eyeball in SH3D.
2. With joists authoritative, you report basement registers/ducts by nearest-joist; agent places them; we build the `ducts/poc` branch scheme from §2.
3. Pin the §2/§5 duct-count open item; then model the maintenance-wall chase + the upstairs reuse (orphan riser, door↔bedroom chase, gable blower).
4. Export for DK Mechanical when the scheme is legible enough to discuss.
