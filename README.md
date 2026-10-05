# Parametric 3D CAD Library

Small parametric models written as code, so you change a number instead of re-drawing the part.

## Models
- `models/card_stand.scad`: a desktop stand for a standard bank-card-size card (85.6 x 54 mm). Set the card thickness, clearance, wall, floor and lean angle at the top of the file.

## Use it
1. Install OpenSCAD (free, openscad.org).
2. Open `models/card_stand.scad`, press F5 to preview and F6 to render, then export an STL for your slicer.

## Checks
`scripts/check_geometry.py` reads the parameters and checks the numbers that make a part printable: the slot is narrower than the stand, the floor under the slot is at least 3 mm, walls are at least 3 mm, and the tilted slot stays clear of the back face. The model also has `assert()` lines that stop OpenSCAD if the parameters are unsafe.
```
pip install pytest
cd scripts && python check_geometry.py && pytest
```

## Honest status
The geometry checks are plain arithmetic on the parameters. The `.scad` file has **not been rendered or printed as part of this repo's tests** (OpenSCAD was not available when it was written). Preview it before printing and adjust `clearance` to your printer.
