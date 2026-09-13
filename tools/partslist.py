#!/usr/bin/env python3
"""Generate the duct parts list from the model.

Run membership comes from the object names — stem plus ordinal — never from
geometry, so this needs no junction resolution. Round vs rectangular comes from
the catalogue id rather than from guessing at near-square sections.

Usage: partslist.py [Home.xml] [out.md]   (defaults are relative to this file)
"""
import math
import os
import re
import sys
from collections import defaultdict

import defusedxml.ElementTree as DET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOME = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "sh3d-internals", "Home.xml")
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(ROOT, "ducting-parts-list.md")
IN = lambda cm: cm / 2.54

DEFAULT_MATERIAL = {"round": "dwspiral", "rect": "rect"}

root = DET.parse(HOME).getroot()
levels = {l.get("id"): l.get("name") for l in root.findall("level")}

ducts, regs = [], []
for f in root.iter("pieceOfFurniture"):
    nm = f.get("name") or ""
    low = nm.lower()
    is_reg = low.startswith("register:")
    if not is_reg and "duct" not in low:
        continue
    full = nm.split(":", 1)[-1].strip()
    m = re.search(r"\[(\w+)\]", full)
    tag = m.group(1) if m else None
    bare = re.sub(r"\s*\[\w+\]\s*", " ", full).strip()
    # RAW dimensions, not the in-plan box. The in-plan values are an axis-aligned
    # envelope — correct for adjacency, but for anything tilted off a right angle
    # they overstate the section (a 12in cylinder rolled 15deg reports 15in wide).
    # width/depth/height are the true part sizes whatever the rotation.
    dims = sorted((IN(float(f.get("width"))),
                   IN(float(f.get("depth"))),
                   IN(float(f.get("height")))))
    shape = "round" if "Cylinder" in (f.get("catalogId") or "") else "rect"
    lvl = levels.get(f.get("level"), "?")
    # Only an explicit FUTURE prefix counts. The `description` field carries
    # "Future possibility" on plenums and trunks that are plainly core scope,
    # and a lowercase "future" appears mid-name in runs that serve a future
    # space alongside a live one.
    future = bare.startswith("FUTURE")
    if is_reg:
        regs.append(dict(name=bare, level=lvl, face=(dims[1], dims[2]),
                         style="circular" if tag == "circular" else "louvred",
                         side="return" if "return" in bare.lower() else "supply",
                         future=future))
    else:
        # Longest dimension is the run direction; the other two are the section.
        ducts.append(dict(name=bare, stem=re.sub(r"\s+\d+$", "", bare), level=lvl,
                          shape=shape, length=dims[2], section=(dims[0], dims[1]),
                          material=tag or DEFAULT_MATERIAL[shape],
                          axis=None, future=future,
                          ordinal=int(re.search(r"(\d+)$", bare).group(1))
                          if re.search(r"(\d+)$", bare) else 1))

# Which axis each segment runs along, so direction changes can be counted.
def axis_of(f):
    w = IN(float(f.get("widthInPlan") or f.get("width")))
    dp = IN(float(f.get("depthInPlan") or f.get("depth")))
    h = IN(float(f.get("heightInPlan") or f.get("height")))
    ang = float(f.get("angle") or 0)
    cs, sn = abs(math.cos(ang)), abs(math.sin(ang))
    ex, ey = w * cs + dp * sn, w * sn + dp * cs
    return max((("x", ex), ("y", ey), ("z", h)), key=lambda t: t[1])[0]


by_name = {}
for f in root.iter("pieceOfFurniture"):
    nm = f.get("name") or ""
    if "duct" not in nm.lower() or nm.lower().startswith("register:"):
        continue
    bare = re.sub(r"\s*\[\w+\]\s*", " ", nm.split(":", 1)[-1].strip()).strip()
    by_name.setdefault(bare, []).append(axis_of(f))
for d in ducts:
    d["axis"] = by_name.get(d["name"], ["?"])[0]

runs = defaultdict(list)
for d in ducts:
    runs[d["stem"]].append(d)

rows = []
for stem, members in runs.items():
    members.sort(key=lambda d: d["ordinal"])
    total = sum(m["length"] for m in members)
    bends = sum(1 for a, b in zip(members, members[1:]) if a["axis"] != b["axis"])
    secs, mats, lvls = [], [], []
    for m in members:
        s = (f'{m["section"][1]:.0f}″ ø' if m["shape"] == "round"
             else f'{m["section"][0]:.0f}x{m["section"][1]:.0f}')
        if s not in secs:
            secs.append(s)
        if m["material"] not in mats:
            mats.append(m["material"])
        if m["level"] not in lvls:
            lvls.append(m["level"])
    rows.append(dict(stem=stem, n=len(members), total=total, bends=bends,
                     secs=secs, mats=mats, lvls=lvls,
                     side="return" if "return" in stem.lower() else "supply",
                     future=all(m["future"] for m in members)))

# Linear feet by section + material, future excluded from the buy.
tally = defaultdict(float)
for d in ducts:
    if d["future"]:
        continue
    s = (f'{d["section"][1]:.0f}″ ø' if d["shape"] == "round"
         else f'{d["section"][0]:.0f}x{d["section"][1]:.0f}')
    tally[(s, d["material"])] += d["length"]

L = []
w = L.append
w("# Duct parts list")
w("")
w("**Generated from the model.** Every figure below is read from the drawn objects — "
  "run membership from the object names, lengths and sections from the geometry, "
  "register faces from the frame objects. Regenerate it rather than editing it.")
w("")
w("**Fittings are not in this list.** No elbows, tees, takeoffs, boots, transitions or "
  "hangers are modelled, and the bend counts below are inferred from segment-to-segment "
  "direction changes rather than drawn. A parts list that silently omitted fittings would "
  "read as complete when it is not — **treat this as the straight-duct schedule and the "
  "fitting count as the contractor's to supply.** That is work they are better placed to "
  "do anyway, and asking for it is how the effective-length question gets answered.")
w("")
w("Lengths are centre-line and **do not deduct for fittings**, so they run long at every "
  "junction. Runs marked *future* are drawn but out of scope, and are excluded from the "
  "material totals.")
w("")

for side in ("supply", "return"):
    w(f"## {side.title()} runs")
    w("")
    w("| Run | Levels | Segs | Section | Material | Length | Bends |")
    w("|---|---|:-:|:-:|:-:|---:|:-:|")
    for r in sorted(rows, key=lambda r: (r["future"], r["stem"])):
        if r["side"] != side:
            continue
        fut = " *(future)*" if r["future"] else ""
        w(f'| {r["stem"]}{fut} | {", ".join(r["lvls"])} | {r["n"]} | '
          f'{" / ".join(r["secs"])} | {" / ".join(r["mats"])} | '
          f'{r["total"] / 12:.1f} ft | {r["bends"]} |')
    w("")

w("## Registers and grilles")
w("")
w("| Register | Level | Face | Style |")
w("|---|---|:-:|:-:|")
for r in sorted(regs, key=lambda r: (r["future"], r["side"], r["name"])):
    fut = " *(future)*" if r["future"] else ""
    w(f'| {r["name"]}{fut} | {r["level"]} | {r["face"][0]:.0f}x{r["face"][1]:.0f} | {r["style"]} |')
w("")

w("## Materials summary")
w("")
w("Future runs excluded. Round sizes are **airway** — confirm whether a supplier quotes "
  "inner or outer diameter on double-wall before ordering, because getting it backwards "
  "costs two inches of diameter on every round run at once.")
w("")
w("| Section | Material | Linear feet |")
w("|---|---|---:|")
for (s, mat), ln in sorted(tally.items(), key=lambda kv: -kv[1]):
    w(f"| {s} | {mat} | {ln / 12:.1f} |")
w(f'| **Total** | | **{sum(tally.values()) / 12:.1f}** |')
w("")

live_regs = [r for r in regs if not r["future"]]
branches = [r for r in rows if "branch" in r["stem"].lower() and not r["future"]]
w("## Counts")
w("")
w("| Item | Count |")
w("|---|---:|")
w(f'| Supply registers | {sum(1 for r in live_regs if r["side"] == "supply")} |')
w(f'| Return grilles | {sum(1 for r in live_regs if r["side"] == "return")} |')
w(f'| — of which circular | {sum(1 for r in live_regs if r["style"] == "circular")} |')
w(f"| Branch runs (one balancing damper each) | {len(branches)} |")
w(f'| Inferred direction changes | {sum(r["bends"] for r in rows if not r["future"])} |')
w("")
w("**Damper every takeoff regardless of what the balance calculation says.** A branch "
  "without one cannot be adjusted after the fact, and the first season in a house is when "
  "the balance is actually discovered.")
w("")

open(OUT, "w", encoding="utf-8").write("\n".join(L) + "\n")
print(f"wrote {OUT}  ({len(rows)} runs, {len(regs)} registers, "
      f"{sum(tally.values()) / 12:.0f} ft of duct)")
