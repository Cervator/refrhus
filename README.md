# Refrhus — Sweet Home 3D house data

The house model, tracked **exploded** so git can diff the design — "PR your house" (branch a change, diff it, show a contractor, merge when built).

## Layout

- `sh3d-internals/` — the exploded `.sh3d` (which is a ZIP): `Home.xml` (walls / rooms / levels / furniture — the diffable truth), the serialized `Home`, `ContentDigests`, and numbered content entries (background images, 3D models). **Source of truth — commit changes here.**
- `Refrhus.sh3d` — the packed file you open in Sweet Home 3D. **Generated, gitignored.**
- `hvac/` — load calculations: the professional Manual J reports and every dated [Eldr](https://github.com/SiliconSaga/eldr) run, with an index explaining where the two disagree. See [`hvac/README.md`](hvac/README.md).
- `ducting-scheme.md` — **start here for the duct design**: the scheme as it stands, why it is shaped that way, and the case against a second air handler. `ducting-design.md` is the as-built seed and `ducting-plan.md` the earlier forward spec.
- Measurement records — `basement-joists.md`, `basement-structure.md`, `basement-measure-sheet.md`, `chimney-measure-sheet.md`, and `basement-post-details.html` (plan-view details of the six posts; also published as an artifact).
- `schematic-hitlist.md` — what still needs measuring or drawing, ranked by BTU impact.
- `eldr-sidecar.yaml` — the thermal assumptions Eldr reads alongside the geometry (assemblies, design conditions, infiltration). Live input, not an artifact, so it stays at the root.

## Pack / unpack

Scripts live in `realms/realm-siliconsaga/sweethome3d/`; run from the workspace root:

```bash
# rebuild the openable .sh3d from the exploded tree, then open it in SH3D
bash realms/realm-siliconsaga/sweethome3d/pack.sh   hoards/refrhus/sh3d-internals hoards/refrhus/Refrhus.sh3d

# after editing in SH3D, re-explode and commit the diff
bash realms/realm-siliconsaga/sweethome3d/unpack.sh hoards/refrhus/Refrhus.sh3d   hoards/refrhus/sh3d-internals
```

`Home.xml` is the meaningful diff target; the serialized `Home` is binary (tracked for now — may be dropped once we confirm SH3D reads `Home.xml` in priority, the `.sh3x` route).

## Pushing to a remote

Private repo recommended (it's your real house layout). `ws hoard init` left it remote-less:

```bash
gh repo create Cervator/refrhus --private --source=hoards/refrhus --remote=Cervator --push
```
