"""
Checks the numbers in models/card_stand.scad without needing OpenSCAD:
reads the parameters, then verifies wall, floor and tilt leave a printable part.
"""
import math
import re
import sys
from pathlib import Path

def read_params(path):
    text = Path(path).read_text()
    params = {}
    for name, value in re.findall(r"^(\w+)\s*=\s*([0-9.]+)\s*;", text, re.M):
        params[name] = float(value)
    return params

def check(p):
    problems = []
    slot_w = p["card_width"] + p["clearance"]
    slot_t = p["card_thickness"] + p["clearance"]
    stand_w = slot_w + 2 * p["wall"]
    tilt = math.radians(p["tilt"])
    # Lowest point of the tilted slot: bottom edge, lowered by half the slot thickness tilt
    bottom_z = p["stand_height"] - p["slot_depth"]
    lowest = bottom_z - (slot_t / 2) * math.sin(tilt)
    if lowest < p["floor_thickness"] - 0.5:
        problems.append(f"slot bottom reaches z={lowest:.2f}, floor too thin")
    if p["floor_thickness"] < 3:
        problems.append("floor_thickness < 3 mm is fragile")
    if p["wall"] < 3:
        problems.append("wall < 3 mm is fragile")
    # Back-lean should not push the slot through the back wall
    run = p["slot_depth"] * math.tan(tilt)
    if p["stand_depth"] / 2 + run + slot_t > p["stand_depth"] - 3:
        problems.append("tilted slot gets within 3 mm of the back face")
    return problems, {"stand_w": stand_w, "slot_w": slot_w, "slot_t": slot_t, "lowest_slot_z": lowest}

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else str(Path(__file__).parent.parent / "models" / "card_stand.scad")
    problems, info = check(read_params(path))
    print(info)
    if problems:
        print("PROBLEMS:"); [print(" -", x) for x in problems]; sys.exit(1)
    print("Geometry checks passed.")
