# Duct model audit

What the drawn model says about itself, and where it disagrees with the [register schedule](ducting-register-schedule.md). Currently **73 `Ducting:` objects and 25 registers**.

**Per-run sections, lengths and materials are not repeated here** — they live in [`ducting-parts-list.md`](ducting-parts-list.md), which is generated from the model on demand. This document carries only the findings that a table cannot: how the geometry was read, what the topology can and cannot tell us, and which sizing conclusions are contested.

---

## Connectivity

A 3D adjacency pass over all 73 duct objects and 25 registers at 3″ tolerance. **Every run joins something, no trunk or plenum dead-ends mid-run, and every register attaches to a duct** — the supply, SE, north and SW systems are all continuous as drawn.

**Read Sweet Home 3D's own rotated dimensions, not the raw ones.** A piece tilted by `pitch` or `roll` carries `widthInPlan` / `depthInPlan` / `heightInPlan` — the bounding box *after* that tilt — and its `elevation` is measured to the bottom of that box, not of the upright model. Twenty-four of the 73 duct objects are tilted, all of them horizontal runs drawn as pitched cylinders. Reconstructing the rotation from `width`/`depth`/`height` instead puts those runs **tens of inches off in elevation** while leaving the plan position right — so they read as badly broken chains that look perfectly joined on screen. Only the yaw (`angle`) still needs applying, to the in-plan footprint.

The SW return is the run that exposed this: trunks 3 and 4 overlap by 1″ in elevation (74–83″ and 82–91″), and a naive pass reported them 26″ apart. **Two rounds of model edits chased that phantom before the reader was suspected** — the owner's own observation that the pieces touched was correct throughout.

**The opposite mistake for the parts list.** In-plan dimensions are an axis-aligned envelope, so for anything tilted off a right angle they *overstate* the part — a rolled cylinder reported a 29″ diameter. Sections and lengths come from the raw `width`/`depth`/`height`, which are true at any rotation. Two questions, two correct answers, and using either one for the other's job produces confident nonsense.

## Topology cannot be inferred from geometry — only the return side works

Adjacency tells you two objects touch. It does not tell you they are *joined*, and in this model that distinction cannot be recovered:

- **Touching is too loose.** In the basement the branches run parallel along the joist bays and touch side by side. At 3″ tolerance the SE supply trunk comes out with **seven** neighbours and four sibling branches appear to tee into each other.
- **Intersecting is too tight.** Requiring real volume overlap disconnects the North return trunk from the return plenum — a joint that is certainly real, drawn as a butt rather than a penetration.

Joints here are a mix of butts and overlaps, so no single threshold separates a tee from a neighbour. **The return side survives anyway**, because its runs are sparse enough not to graze, and it walks into exactly the tree the design describes:

```
Return plenum
├── North return trunk → kitchen branch, both-main-bedrooms
│                        └── both-main-bedrooms → main bed, main floor kids
├── SE return trunk   → office, play room south      (the 2nd-floor riser)
└── SW return trunk   → SW return branch (living room / SW basement)
```

**The supply side needs its hierarchy declared rather than computed**, and it already is — the trunk tables in the register schedule are hand-authored and carry the reducing schedule an installer needs. Re-deriving them from geometry would confirm something already known at the cost of real modelling discipline.

**The parts list does not need any of this.** Run membership comes from the object *names* — stem plus ordinal — so per-run length, section, material and direction changes are all derivable without resolving a single junction. That is also why duplicate names are a correctness bug rather than untidiness: two segments sharing an ordinal sort arbitrarily and the bend count silently loses a turn. The generator now refuses to run when it finds one.

## The contested sizing

**The main-floor return path is the system's real bottleneck**, and it is not a grille problem. `Return branch for both main bedrooms` is a single **4x8 running 30 ft**, and three returns hang off it — Main Bed 227, Kids Room 64, and the Utility Room's 83 via the Kids Room tap. That is ~374 CFM through 32 in².

It is the existing duct through the inaccessible crawlspace, so it is not a sizing error to correct in the model — but **the pinch is only the buried section.** The basement portion is open and can be enlarged at least as far as the splitter, and optionally onward to the Kids Room. This also reframes the remedy: a transfer grille above the bedroom door relieves the bedroom alone and does nothing for the two rooms behind the same constriction.

**The Utility Room return shares the Kids Room branch**, which takes that branch from 64 CFM to 147. It is drawn at 8″, which runs 421 fpm and is fine; the 6″ the schedule originally specified would have run 747. A shared branch is sized for the sum, and once shared, the room name on it stops being the whole story.

**Two kitchen faces remain constrained by cabinetry** — the SE supply at 2″ of height running 806 fpm, and the return at 3x20 running 602. Both are construction decisions rather than duct decisions, which is why the model still carries them as drawn.

## Modelling caveats

Cross-section assumes the longest edge is the run direction; where a box is nearly cubic that assumption is weak. **No elbows, tees, takeoffs or transitions are modelled**, so run lengths are centre-line and indicative, and **total effective length is not derivable from this model**. That matters more than it sounds, because effective length is what a static-pressure argument turns on — and static pressure is what decides the one-unit-versus-two question.
