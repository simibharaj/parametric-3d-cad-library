// Parametric desktop stand for a standard card (CR80, 85.6 x 54 mm).
// Units: millimeters. Open in OpenSCAD (free): F5 preview, F6 render, then export STL.

$fn = 48;

card_width      = 85.6;   // CR80 width
card_thickness  = 0.8;    // typical card; thicker for metal cards
clearance       = 0.6;    // extra room so the card slides in
wall            = 5;      // material left on each side of the slot
floor_thickness = 4;      // material left under the slot (keep >= 3 for strength)
stand_depth     = 40;
stand_height    = 28;
slot_depth      = 18;     // how far the slot cuts down from the top
tilt            = 12;     // lean-back angle in degrees
corner_r        = 3;

slot_w = card_width + clearance;
slot_t = card_thickness + clearance;
stand_w = slot_w + 2 * wall;

assert(slot_depth <= stand_height - floor_thickness, "slot too deep: floor would be too thin");
assert(stand_w > slot_w, "stand must be wider than the slot");

module rounded_block(w, d, h, r) {
    hull() for (x = [r, w - r], y = [r, d - r]) translate([x, y, 0]) cylinder(r = r, h = h);
}

module card_slot() {
    translate([stand_w / 2, stand_depth / 2, stand_height - slot_depth])
    rotate([-tilt, 0, 0])
    translate([-slot_w / 2, -slot_t / 2, 0])
    cube([slot_w, slot_t, slot_depth * 2]);
}

difference() {
    rounded_block(stand_w, stand_depth, stand_height, corner_r);
    card_slot();
}
