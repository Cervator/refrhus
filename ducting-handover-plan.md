# Handover package — design plan

Written 2026-09-07, deliberately before a context compaction, so the next session can pick this up cold.

**Goal:** turn the duct design into something an HVAC company can be handed — a public GitHub Pages site with real navigation, backed by the measured model, carrying a parts list and renders. The company still favours a second air handler upstairs; this package is the argument against it, made in their own units.

**Decision made:** `Cervator/refrhus` goes **fully public**. Refr Hus becomes a public worked example of GDD applied to home improvement, and going public removes the GitHub Pages paid-tier question entirely (free plan publishes Pages from public repos; private-repo Pages needs Pro, and even then the *site* is public anyway).

---

## Where things stand

| | State |
|---|---|
| Model | Basement measurement-true; all three levels registered east–west; 71 `Ducting:` objects drawn |
| Loads | Eldr, heat-pump airflow (30°F rise), biased 2nd ×1.35 / basement ×0.70 |
| Schedule | `ducting-register-schedule.md` — per-register sizes, editable |
| Audit | `ducting-model-audit.md` — drawn objects vs schedule |
| Branch | `ducts/poc`, so the diff is the proposal |

Fixed since the audit: both plenums to 12×20, north return trunk widened to a stud bay (may have height to spare, deferred to install).

**Carried as doc-only metadata**, because there is no clean way to say it in the schematic: the main-bedroom return branch is 7.5×4 (91 CFM) against 227 needed. It is the existing duct through the inaccessible crawlspace, it is **not** a sizing error to correct, and the plan of record is a transfer grille above the bedroom door first, with a second return via the SE corner only if that proves insufficient. **Treat the docs as the home for design metadata the model cannot express.**

---

## Task 1 — Duct metadata convention

Ducts are *furniture*, and furniture names are editable directly in Sweet Home 3D. So use a **bracketed keyword in the name**, the same convention already established for tagging windows:

```
Ducting: SE supply trunk 3 [spiral]
Ducting: Return branch for main bed room 1 [oval]
Ducting: North supply trunk 4 [rect]
```

Vocabulary: `[rect]` · `[spiral]` · `[dwspiral]` (double-wall) · `[oval]` · `[flex]`

**Defaults, so most objects need no tag at all:** a box is `[rect]`, a cylinder is `[spiral]`. Only the exceptions get written down — squeeze a dimension and add `[oval]` where oval earns its place, `[dwspiral]` where a supply is exposed.

### When insulation is actually required

**Supply ducts sweat; returns do not.** A supply carries ~55°F air in cooling, and a basement at 75°F / 50% RH has a dew point right at 55°F — 60°F at 60% RH. So exposed basement supply runs condense *even in conditioned space*. Returns run near 75°F, above any indoor dew point, and never sweat.

| | Treatment |
|---|---|
| Supply, **exposed** (basement feature runs) | **`[dwspiral]`** — insulation inside the shell keeps the outer surface warm |
| Supply, concealed (joist bays, cabinet) | `[rect]` / `[spiral]` with external wrap |
| All returns | plain — no insulation needed for condensation |
| Returns in the knee-wall attic | plain; the blown insulation around them *is* the insulation |

Why names rather than `<property>` elements: properties need `tag.py`, which currently handles only walls and rooms, and furniture already has an editable name. The bracket is self-validating in the same way the assembly tags are — a token without a known keyword is just text.

**Do not** put material in the prose part of the name. The names already carry run identity, destination and sequence, and they are close to unwieldy.

## Task 2 — Compute the real hierarchy from geometry

The audit reads each object in isolation. What is missing is **connectivity**, and it is what the SE riser question turns on.

Approach: two objects are connected when their bounding boxes touch or overlap within a tolerance (the owner notes some only barely touch and some overlap). Build a graph, root it at each plenum, and walk outward. Then each segment's carried CFM is **the sum of the destination CFMs downstream of it** — which is the correct way to size a trunk, and something no amount of per-object inspection can produce.

Deliverables:
- A tree per system, plenum → trunk → branch → register
- Carried CFM at every segment
- **Required** size versus **drawn** size, flagged both ways

**Rotation will break a naive implementation.** Some segments are drawn at an angle — Sweet Home 3D stores an `angle` on each piece, and an axis-aligned bounding box around a rotated object is both too large and the wrong shape. Angled segments will read as disconnected, or as touching things they do not. Rotate each object's corners by its own angle before testing adjacency.

**The SE riser is the open question this answers.** Drawn 12×12 (763 CFM capacity), deliberately unsized. Scenarios, for scale:

| If it carries | CFM | Wants |
|---|---:|---|
| 2nd floor only (Office + Play Room) | 228 | 9″ |
| + Main-floor kids room | 292 | 10″ |
| + Main bed west | 405 | 11″ |

At 12×12 it holds 763, so unless it is carrying most of the south side it is oversized — and an oversized trunk runs slow, which is exactly what lets the near takeoff steal from the far one where this splits three ways at the top.

**Shape it wide and shallow, not square.** Three takeoffs need face width more than they need area, and square is the worst shape for the job:

| If it carries | Rectangular | Equiv | Capacity | fpm |
|---|---|---:|---:|---:|
| ~292 | **6×16** | 10.4″ | 400 | 350 |
| ~405 | **8×16** | 12.2″ | 628 | 456 |

16″ of face gives three takeoffs room to be spaced rather than crowded; 6–8″ of depth keeps the riser from eating the cabinet space the return needs alongside it. Velocity runs low at these sizes, so **damper all three takeoffs** — at 350–450 fpm that is how the split gets balanced, not an optional refinement.

**Return riser: 9×9.** It collects the two upstairs returns — Office 113 plus Play Room 168 at the generous sizing, 228 by mass balance. 9×9 gives 9.84″ equivalent and 357 CFM capacity, running 405 fpm at 228 and 499 at 281, both inside the 400–600 window returns want. 8×8 would be 8.75″ and slightly under. Square is fine here because it collects rather than branches.

## Task 3 — Parts list

Derivable from the objects once Task 2 lands. Per run: material, cross-section, total length, and a count of direction changes (inferable from segment-to-segment angle) even though elbows are not modelled.

Report as: schedule of runs, then a materials summary — linear feet by size and material, register and grille counts, damper counts. **Connectors are explicitly out of scope** and the document should say so, since a parts list that silently omits fittings reads as complete when it is not.

## Task 4 — Renders

Sweet Home 3D exports the 3D view to OBJ natively. Worth having: the air handler and plenum area, each trunk system, and the second-floor riser through the utility cabinet. Alternative: photograph the plan view per level with the duct layer visible.

## Task 5 — The site

GitHub Pages from `Cervator/refrhus`, public. Side navigation across the existing documents plus the generated parts list and renders. The existing docs are already written to be read cold, so the work is navigation and presentation, not rewriting.

Suggested order: the scheme primer as the landing page, then the argument against a second unit, the register schedule, the model audit, the parts list, the measurement records, and the renders.

---

## Task 6 — CI: run Eldr on every push, diff the loads on every PR

The idea that completes "PR your house". `ducting-plan.md` §1 already says as-built anchors live on `main` and proposals live on a branch **so the diff is the proposal** — but today that diff is geometric. Running the engine in CI makes it *quantitative*: change a room, and the load change shows up in the pull request.

**On push to `main`:** regenerate the report and publish it to Pages, so the site is never stale relative to the model.

**On a pull request:** run Eldr against both the PR head and `main`, then comment the difference. `--json` already emits the whole analysis as structured data, so the diff is a dict comparison rather than text scraping:

```
## Eldr — load change vs main

| Component  |   main |     PR |    Δ |
|------------|-------:|-------:|-----:|
| ceiling    |  1,555 |  2,340 | +785 |
| **total**  | 39,439 | 40,224 | +785 |

Design airflow 1,217 → 1,241 CFM · Manual S 3.3 → 3.4 tons (recommendation unchanged)
```

**Eldr's warnings become CI checks**, which may be the more valuable half. A pull request that draws a room badly and introduces a new schematic gap, an unbound `spaces:` key or a borrowed U-value would surface it in the comment instead of being discovered three sessions later. That is regression testing for a house.

Practicalities:

- **The engine has to be reachable.** `SiliconSaga/eldr` is a separate repo, and a public `refrhus` pulling a private `eldr` means a token with private-repo read sitting in a public repo's secrets. Cleanest resolution: **make `eldr` public too.** It is an engine with no house data in it, and the whole exercise is a public worked example.
- **Eldr has no packaging metadata** — a known limitation from the level-stack work. CI checks it out and sets `PYTHONPATH` rather than pip-installing. Worth fixing eventually; not a blocker.
- **Runs against `sh3d-internals/Home.xml` directly**, which is the tracked artefact. The packed `.sh3d` is gitignored and irrelevant to CI.
- Dependencies are only `pyyaml` and `defusedxml`.

## What to fix before handover

1. **Size the SE riser** from Task 2's answer.
2. **Add material tags** so the parts list can be generated.
3. **Consider flat oval** on the nine 4″-deep runs the audit lists.

## What to be upfront about in the package

**Total effective length is not derivable from this model.** No elbows, tees or takeoffs are drawn, and Eldr's Manual D uses a flat 1.5× fitting factor rather than true equivalent lengths. Real fittings on a three-storey run add 50–150 ft of equivalent length.

This matters more than any other caveat, because **the second-unit argument will be decided on static pressure**. Going in with an acknowledged gap is far stronger than being caught with an optimistic number — and it invites the contractor to supply the fitting counts, which is work they are better placed to do anyway.

Two other honest notes already written into the documents and worth keeping visible: the second-floor loads are deliberately conservative (ceiling area modelled at 984 ft² against the professionals' 1,547), and the biases applied to the airflow are stated rather than buried.
