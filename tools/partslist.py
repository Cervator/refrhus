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

# --- Cost, planning grade -------------------------------------------------
# Installed $/ft bands. Broad on purpose: fabrication, access and region move
# these more than size does, and a single figure would imply precision we do
# not have. Round is double-wall insulated spiral at 5-9in; rect is shop-
# fabricated galvanised, with the large trunk sections sitting at the top.
BANDS = {"round": (12, 30), "rect": (10, 25)}
round_ft = sum(d["length"] for d in ducts if d["shape"] == "round" and not d["future"]) / 12
rect_ft = sum(d["length"] for d in ducts if d["shape"] != "round" and not d["future"]) / 12
n_sup = sum(1 for r in live_regs if r["side"] == "supply")
n_ret = sum(1 for r in live_regs if r["side"] == "return")

cost = [
    ("Round duct, double-wall spiral", f"{round_ft:.0f} ft",
     round_ft * BANDS["round"][0], round_ft * BANDS["round"][1]),
    ("Rectangular and oval, fabricated", f"{rect_ft:.0f} ft",
     rect_ft * BANDS["rect"][0], rect_ft * BANDS["rect"][1]),
    ("Supply registers", f"{n_sup}", n_sup * 15, n_sup * 60),
    ("Return grilles", f"{n_ret}", n_ret * 25, n_ret * 100),
    ("Balancing dampers", f"{len(branches)}", len(branches) * 25, len(branches) * 60),
]
lo = sum(c[2] for c in cost)
hi = sum(c[3] for c in cost)

w("## Cost — planning grade only")
w("")
w("**Every figure here is a band, and the bands are wide on purpose.** Fabrication, "
  "access and region move installed duct pricing more than size does, so a single "
  "number would imply a precision this does not have. Use it to compare options "
  "against each other — which is what it is actually for — not to budget.")
w("")
w("| Item | Quantity | Low | High |")
w("|---|---:|---:|---:|")
for label, qty, a, b in cost:
    w(f"| {label} | {qty} | ${a:,.0f} | ${b:,.0f} |")
w(f"| **Ductwork subtotal** | | **${lo:,.0f}** | **${hi:,.0f}** |")
w("")
w("**All figures are pre-incentive.** No rebate, tax credit or utility programme is "
  "netted off anywhere in this document. Incentives change by year, by model and by "
  "jurisdiction, and a quote that quietly assumes one is a quote that cannot be "
  "compared against another.")
w("")
w("**Fittings are missing from that subtotal and they are not a rounding error.** "
  "Elbows, tees, takeoffs, boots and transitions commonly run **30–50% of a duct "
  "job's material cost**, and none of them are modelled here — so treat the straight-"
  "duct figure as roughly two thirds of the real material story.")
w("")
w("### Labour is already inside those bands")
w("")
w("The $/ft figures above are *installed*, not material-only, so labour is not a line "
  "to add — it is most of what the band's width represents. For sanity-checking a "
  "quote that separates them: duct labour alone runs roughly **$5–15 per linear foot**, "
  "and HVAC labour is **$75–150 per hour per technician**.")
w("")
w("Published estimates of labour's *share* of a duct job disagree sharply — one puts it "
  "near 22% of a whole-house replacement, another at 60%. **That spread is a signal, "
  "not noise:** it is the difference between duct run through open basement joists and "
  "duct fished through finished walls. This house is both, which is exactly why the "
  "bands here are wide and why a walkthrough quote will beat any figure on this page.")
w("")
w("### Ducted extras, priced separately")
w("")
w("| Option | Installed | Note |")
w("|---|---|---|")
w("| Media air cleaner | **$400–1,000** | A deep pleated filter in the return. The "
  "default choice, and the one with no downside beyond filter changes |")
w("| UV treatment | **$400–800**, up to $3,500 | Coil-sterilising lamps at the low end; "
  "in-duct air treatment at the high end. Effectiveness claims vary far more than price does |")
w("| Whole-house humidifier | **$400–1,200**, up to $2,500 | Bypass or steam. Steam "
  "costs more and actually holds a setpoint |")
w("")
w("**A media cleaner has a real interaction with this design and the others do not.** "
  "A deep filter adds static pressure to the return side, and the return side is "
  "already this system's constraint — see the main-floor return path above. Size the "
  "filter cabinet generously and account for its pressure drop in the same breath as "
  "the return trunk, rather than adding it afterwards. **The others are additions to "
  "the system; filtration is a change to it.**")
w("")
w("### Equipment, and why the number to quote is 4 tons")
w("")
w("Manual S on the current model recommends **3.5 tons**. The number to put in front of "
  "a contractor is **4.0**, and the reason is the state of the model rather than a "
  "preference for headroom.")
w("")
w("The load calculation runs against geometry that is knowingly incomplete, and **every "
  "gap in it points the same way**:")
w("")
w("- **No grade line.** Basement walls are classed below-grade over their whole height. "
  "Taking the professionals' measured U-value alone moves the load to roughly 3.8 tons.")
w("- **The second-floor roof is not drawn.** Ceiling area is modelled at 984 ft² against "
  "a professional report's 1,547 — a third of that surface is missing, and it is the "
  "hot side of the house.")
w("- **The load has risen at almost every correction.** 31,757 → 37,962 → 42,097, then "
  "down to 39,694 only because the basement was finally *measured* rather than "
  "estimated. The sizing verdict on the existing 4-ton unit has flipped between "
  "oversized and well-matched three times.")
w("")
w("**A sizing verdict that flips with each correction is one to hold loosely.** 3.5 tons "
  "is what today's model says; 3.8 is what one known-missing input alone would make it; "
  "and the remaining gaps have not been priced at all. Rounding to the next tier is the "
  "cheap direction to be wrong in — an oversized heat pump with inverter turndown "
  "short-cycles far less than a single-stage unit would, while an undersized one has no "
  "remedy short of replacement.")
w("")
w("| | Installed, pre-incentive |")
w("|---|---:|")
w("| 3.5-ton cold-climate heat pump, this class | $5,000–9,000 |")
w("| **4.0-ton — the tier to quote** | **$5,500–10,500** |")
w("")
w("The Bosch IDS Ultra is the candidate on file. Treat both rows as placeholders until "
  "a dealer quotes the specific model: published pricing for this equipment comes "
  "largely from aggregator sites rather than distributors.")
w("")
w("### What this is for: one air handler or two")
w("")
w("The number that matters is not the total, it is **the delta between one unit and "
  "two**. The current proposal is a second *internal* ducted handler rather than one in "
  "the knee-wall attic, which is a materially better idea — an internal unit sits in "
  "conditioned space, so the duct losses that make attic equipment a bad retrofit bet "
  "do not apply. It is argued with on its merits in "
  "[`ducting-scheme.md`](ducting-scheme.md).")
w("")
w("On cost alone, the delta is a second indoor unit, a second filter, a second "
  "condensate path, a second service point and a second maintenance schedule for as "
  "long as the house stands — against a riser that **has to be built anyway** for the "
  "main floor.")
w("")
w("But cost is not what decides it. **This turns on static pressure**, and the two "
  "schemes share most of their ductwork regardless of which wins, so the straight-duct "
  "total above barely moves between them. Get the fitting counts; they settle it.")
w("")
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
