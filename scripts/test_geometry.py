from check_geometry import check, read_params
from pathlib import Path

SCAD = Path(__file__).parent.parent / "models" / "card_stand.scad"

def test_default_model_is_printable():
    problems, _ = check(read_params(SCAD))
    assert problems == []

def test_slot_is_narrower_than_stand():
    _, info = check(read_params(SCAD))
    assert info["slot_w"] < info["stand_w"]

def test_thin_floor_is_flagged():
    p = read_params(SCAD); p["floor_thickness"] = 1.0
    problems, _ = check(p)
    assert any("floor" in x for x in problems)

def test_too_deep_slot_is_flagged():
    p = read_params(SCAD); p["slot_depth"] = 27.0
    problems, _ = check(p)
    assert problems
