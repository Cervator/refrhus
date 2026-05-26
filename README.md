# Refrhus — Sweet Home 3D house data

The house model, tracked **exploded** so git can diff the design — "PR your house" (branch a change, diff it, show a contractor, merge when built).

## Layout

- `sh3d-internals/` — the exploded `.sh3d` (which is a ZIP): `Home.xml` (walls / rooms / levels / furniture — the diffable truth), the serialized `Home`, `ContentDigests`, and numbered content entries (background images, 3D models). **Source of truth — commit changes here.**
- `Refrhus.sh3d` — the packed file you open in Sweet Home 3D. **Generated, gitignored.**

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
