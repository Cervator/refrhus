# Refrhus — Sweet Home 3D house data

The house model, tracked **exploded** so git can diff the design — "PR your house" (branch a change, diff it, show a contractor, merge when built).

**Public.** The rendered site at [`index.md`](index.md) is the contractor-facing version of what is here.

## Layout

- `sh3d-internals/` — the exploded `.sh3d` (which is a ZIP): `Home.xml` (walls / rooms / levels / furniture — the diffable truth), `ContentDigests`, and numbered content entries (background images, 3D models). **Source of truth — commit changes here.**
- `Refrhus.sh3d` — the packed file you open in Sweet Home 3D. **Generated, gitignored.**
- `hvac/` — load calculations: the professional Manual J reports and every dated [Eldr](https://github.com/SiliconSaga/eldr) run, with an index explaining where the two disagree. See [`hvac/README.md`](hvac/README.md).
- `eldr-sidecar.yaml` — the thermal assumptions Eldr reads alongside the geometry (assemblies, design conditions, infiltration). Live input, not an artifact, so it stays at the root.
- `tools/` — generators. `partslist.py` rebuilds `ducting-parts-list.md` from the model.

### The duct design

| | |
|---|---|
| [`ducting-scheme.md`](ducting-scheme.md) | **Start here.** The scheme, why it is shaped that way, the case against a second air handler, and the build details |
| [`ducting-register-schedule.md`](ducting-register-schedule.md) | Per-register airflow, duct size and face size. Hand-edited |
| [`ducting-parts-list.md`](ducting-parts-list.md) | **Generated** — run `tools/partslist.py`, do not edit |
| [`ducting-handover-plan.md`](ducting-handover-plan.md) | Modelling conventions and what remains open |
| [`ducting-model-audit.md`](ducting-model-audit.md) | What is drawn, checked against the schedule |

### The house

[`HISTORY.md`](HISTORY.md) is construction ground truth — read it before moving a wall. Measurement records are `basement-joists.md`, `basement-structure.md`, `basement-measure-sheet.md`, `chimney-measure-sheet.md`, and `basement-post-details.html`. [`schematic-hitlist.md`](schematic-hitlist.md) ranks what still needs measuring by BTU impact. [`scanning-plan.md`](scanning-plan.md) is a parked evaluation of 3D scanning as a way to close the remaining gaps.

## Pack / unpack

Scripts live in `realms/realm-siliconsaga/sweethome3d/`; run from the workspace root:

```bash
# rebuild the openable .sh3d from the exploded tree, then open it in SH3D
bash realms/realm-siliconsaga/sweethome3d/pack.sh   hoards/refrhus/sh3d-internals hoards/refrhus/Refrhus.sh3d

# after editing in SH3D, re-explode and commit the diff
bash realms/realm-siliconsaga/sweethome3d/unpack.sh hoards/refrhus/Refrhus.sh3d   hoards/refrhus/sh3d-internals
```

`Home.xml` is the meaningful diff target. **A no-op open→save→unpack must diff to nothing** — `normalize.sh` enforces that by stripping volatile view state. If no-op saves start churning, a new view-state surface appeared: extend `normalize.sh` rather than hand-editing `Home.xml`.
