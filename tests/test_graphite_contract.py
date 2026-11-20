import json
import re
import unittest
from pathlib import Path

from test_qwerty_contract import (
    KEY_LABELS as QWERTY_KEY_LABELS,
    MATRIX_COORDINATES as SILAKKA54_COORDINATES,
    SHIFTED_LABELS as QWERTY_SHIFTED_LABELS,
    primary_visualizer_label,
)


ROOT = Path(__file__).resolve().parents[1]
LAYER_IDS = ("base", "nav", "mouse", "sym", "num", "fun")
# The thumb key that is held to show each layer. Fun is a one-shot layer
# (OSL) from Nav or Mouse, so no key is held on it.
ACTIVE_LAYER_KEYS = {"nav": "LT2", "mouse": "LT3", "sym": "RT3", "num": "RT2"}

# Corne v4.1: 3x6 keys, 3 thumbs, and 2 extra keys per half. Vial stores the
# extra keys in column 6 and each right-hand row from the outer edge inwards.
CORNE_COORDINATES = {
    **{(row, column): f"L{row + 1}{column + 1}" for row in range(3) for column in range(6)},
    (0, 6): "LEX1",
    (1, 6): "LEX2",
    **{(3, column): f"LT{column - 2}" for column in range(3, 6)},
    **{(row, column): f"R{row - 3}{column + 1}" for row in range(4, 7) for column in range(6)},
    (4, 6): "REX1",
    (5, 6): "REX2",
    **{(7, column): f"RT{column - 2}" for column in range(3, 6)},
}

BOARDS = {
    "silakka54": ("app-graphite.json", "vial/miryoku-silakka54-graphite.vil", SILAKKA54_COORDINATES),
    "corne": ("app-corne-graphite.json", "vial/miryoku-corne-v41-graphite.vil", CORNE_COORDINATES),
}

# The ZMK config (jellydn/zmk-config config/combos.dtsi) is the source for the
# combos. The Corne Vial file has the same 11 combos and the same 50 ms term.
# The older Silakka54 Vial file has only 4 combos at 35 ms.
COMBO_SOURCE = "vial/miryoku-corne-v41-graphite.vil"

KEY_LABELS = {
    **QWERTY_KEY_LABELS,
    "KC_MNXT": "Next",
    "KC_MPRV": "Prev",
    "KC_QUOTE": "'",
    "M0": "Shot",
    "OSL(5)": "OS Fn",
    "QK_LAYER_LOCK": "Lock",
}
SHIFTED_LABELS = {
    **QWERTY_SHIFTED_LABELS,
    "KC_COMMA": "<",
    "KC_DOT": ">",
    "KC_QUOTE": '"',
    "KC_SLASH": "?",
}
COMBO_ACTIONS = {
    "KC_ENTER": "Enter",
    "KC_ESCAPE": "Escape",
    "KC_QUOTE": "Quote (')",
    "LGUI(KC_C)": "Copy (Cmd+C)",
    "LGUI(KC_Q)": "Quit app (Cmd+Q)",
    "LGUI(KC_X)": "Cut (Cmd+X)",
    "OSM(MOD_HYPR)": "Sticky Hyper (Cmd+Ctrl+Alt+Shift)",
    "OSM(MOD_LGUI)": "Sticky GUI (Cmd)",
    "OSM(MOD_MEH)": "Sticky Meh (Ctrl+Alt+Shift)",
}


def vial_label(keycode):
    if keycode in KEY_LABELS:
        return KEY_LABELS[keycode]
    if re.fullmatch(r"KC_[A-Z0-9]+", keycode):
        return keycode.removeprefix("KC_")
    match = re.fullmatch(r"LSFT\((.+)\)", keycode)
    if match:
        return SHIFTED_LABELS[match.group(1)]
    match = re.fullmatch(r"LGUI\((.+)\)", keycode)
    if match:
        return f"Cmd+{vial_label(match.group(1))}"
    match = re.fullmatch(r"(?:[LR](?:GUI|ALT|CTL|SFT)_T|LT\d)\((.+)\)", keycode)
    if match:
        return vial_label(match.group(1))
    raise KeyError(f"No display label for Vial keycode {keycode!r}")


def combo_rows(vial):
    return [
        {
            "keys": " + ".join(vial_label(key) for key in combo[:-1] if key != "KC_NO"),
            "action": COMBO_ACTIONS[combo[-1]],
        }
        for combo in vial["combo"]
        if combo[-1] != "KC_NO"
    ]


def shift_override_rows(vial):
    return [
        f"Shift + {vial_label(override['trigger'])} → {vial_label(override['replacement'])}"
        for override in vial["key_override"]
        if override["trigger"] != "KC_NO"
    ]


class GraphiteContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.combo_vial = json.loads((ROOT / COMBO_SOURCE).read_text())

    def load(self, board):
        visualizer_path, vial_path, coordinates = BOARDS[board]
        return (
            json.loads((ROOT / visualizer_path).read_text()),
            json.loads((ROOT / vial_path).read_text()),
            coordinates,
        )

    def test_layers_match_vial_matrix(self):
        for board in BOARDS:
            visualizer, vial, coordinates = self.load(board)
            self.assertEqual([layer["id"] for layer in visualizer["layers"]], list(LAYER_IDS), board)
            for layer_index, layer_id in enumerate(LAYER_IDS):
                web_layer = visualizer["layerData"][layer_id]
                self.assertEqual(set(web_layer), set(coordinates.values()), f"{board}.{layer_id}")
                for (row, column), key_id in coordinates.items():
                    keycode = vial["layout"][layer_index][row][column]
                    expected = vial_label(keycode)
                    if ACTIVE_LAYER_KEYS.get(layer_id) == key_id:
                        expected = "___"
                    self.assertEqual(
                        primary_visualizer_label(web_layer[key_id]),
                        expected,
                        f"{board} {layer_id}.{key_id} must match Vial matrix ({row}, {column}) {keycode}",
                    )

    def test_combos_match_zmk_and_corne_vial(self):
        self.assertEqual(self.combo_vial["settings"]["2"], 50, "combo term in ms")
        expected = combo_rows(self.combo_vial)
        self.assertEqual(len(expected), 11)
        for board in BOARDS:
            visualizer, _, _ = self.load(board)
            self.assertEqual(visualizer["combos"], expected, board)

    def test_combo_keys_sit_on_marked_base_keys(self):
        for board in BOARDS:
            visualizer, _, _ = self.load(board)
            base = visualizer["layerData"]["base"]
            keys = visualizer["keyboardLayout"]
            all_keys = keys["leftKeys"] + keys["rightKeys"]
            marked = {primary_visualizer_label(base[key["id"]]) for key in all_keys if "combo-key" in key.get("class", "")}
            used = {label for combo in visualizer["combos"] for label in combo["keys"].split(" + ")}
            self.assertEqual(marked, used, board)

    def test_main_page_has_static_text_for_crawlers(self):
        page = (ROOT / "index.html").read_text()
        head = page[: page.index("</head>")]
        title = json.loads((ROOT / "app-graphite.json").read_text())["title"]
        self.assertIn(f"<title>{title}</title>", head)
        self.assertIn(f'<meta property="og:title" content="{title}">', head)
        for tag in ('name="description"', 'property="og:description"', 'property="og:url"', 'rel="canonical"'):
            self.assertRegex(head, rf'<(?:meta|link) {tag} (?:content|href)="[^"{{]+">')
        self.assertIn(f'<h1 v-else class="text-3xl font-bold text-center mb-4">{title}</h1>', page)

    def test_shift_overrides_match_vial(self):
        for board in BOARDS:
            visualizer, vial, _ = self.load(board)
            self.assertEqual(visualizer["shiftOverrides"], shift_override_rows(vial), board)
            self.assertEqual(len(visualizer["shiftOverrides"]), 4, board)


if __name__ == "__main__":
    unittest.main()
