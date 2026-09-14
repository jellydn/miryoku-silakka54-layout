import html
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LAYER_IDS = ("base", "media", "nav", "mouse", "sym", "num", "fun")
ACTIVE_LAYER_KEYS = {
    "media": "LT1",
    "nav": "LT2",
    "mouse": "LT3",
    "sym": "RT3",
    "num": "RT2",
    "fun": "RT1",
}

# Vial stores each right-hand row from the keyboard center outwards. The web
# visualizer IDs use physical left-to-right labels, so this explicit coordinate
# map prevents silent reversals such as swapping Undo and Save.
MATRIX_COORDINATES = {
    **{(row, column): f"L{row}{column + 1}" for row in range(4) for column in range(6)},
    **{(4, column): f"LT{column - 2}" for column in range(3, 6)},
    **{(row, column): f"R{row - 5}{column + 1}" for row in range(5, 9) for column in range(6)},
    **{(9, column): f"RT{column - 2}" for column in range(3, 6)},
}

KEY_LABELS = {
    "KC_BSLASH": "\\",
    "KC_BSPACE": "Bksp",
    "KC_BTN1": "LClick",
    "KC_BTN2": "RClick",
    "KC_BTN3": "MClick",
    "KC_CAPSLOCK": "Caps",
    "KC_COMMA": ",",
    "KC_DELETE": "Del",
    "KC_DOT": ".",
    "KC_DOWN": "↓",
    "KC_END": "End",
    "KC_ENTER": "Enter",
    "KC_EQUAL": "=",
    "KC_ESCAPE": "Esc",
    "KC_GRAVE": "`",
    "KC_HOME": "Home",
    "KC_INSERT": "Ins",
    "KC_LALT": "Alt",
    "KC_LBRACKET": "[",
    "KC_LCTRL": "Ctrl",
    "KC_LEFT": "←",
    "KC_LGUI": "GUI",
    "KC_LSHIFT": "Shift",
    "KC_MFFD": "Next",
    "KC_MINUS": "-",
    "KC_MPLY": "Play",
    "KC_MRWD": "Prev",
    "KC_MSTP": "Stop",
    "KC_MS_D": "M↓",
    "KC_MS_L": "M←",
    "KC_MS_R": "M→",
    "KC_MS_U": "M↑",
    "KC_MUTE": "Mute",
    "KC_NO": "",
    "KC_PAUSE": "Pause",
    "KC_PGDOWN": "PgDn",
    "KC_PGUP": "PgUp",
    "KC_PSCREEN": "PrtSc",
    "KC_RALT": "Alt",
    "KC_RBRACKET": "]",
    "KC_RCTRL": "Ctrl",
    "KC_RGUI": "GUI",
    "KC_RIGHT": "→",
    "KC_RSHIFT": "Shift",
    "KC_SCROLLLOCK": "ScrLk",
    "KC_SCOLON": ";",
    "KC_SLASH": "/",
    "KC_SPACE": "Space",
    "KC_TAB": "Tab",
    "KC_TRNS": "___",
    "KC_UP": "↑",
    "KC_VOLD": "Vol-",
    "KC_VOLU": "Vol+",
    "KC_WH_D": "WhlD",
    "KC_WH_L": "WhlL",
    "KC_WH_R": "WhlR",
    "KC_WH_U": "WhlU",
}

SHIFTED_LABELS = {
    "KC_0": ")",
    "KC_1": "!",
    "KC_2": "@",
    "KC_3": "#",
    "KC_4": "$",
    "KC_5": "%",
    "KC_6": "^",
    "KC_7": "&",
    "KC_8": "*",
    "KC_9": "(",
    "KC_BSLASH": "|",
    "KC_EQUAL": "+",
    "KC_GRAVE": "~",
    "KC_LBRACKET": "{",
    "KC_MINUS": "_",
    "KC_RBRACKET": "}",
    "KC_SCOLON": ":",
}


def primary_visualizer_label(value):
    with_line_breaks = re.sub(r"<br\s*/?>", "\n", value, flags=re.IGNORECASE)
    plain_text = html.unescape(re.sub(r"<[^>]+>", "", with_line_breaks))
    return plain_text.split("\n", 1)[0]


class QwertyContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.visualizer = json.loads((ROOT / "app-qwerty.json").read_text())
        cls.vial = json.loads((ROOT / "vial/miryoku-silakka54-qwerty.vil").read_text())

    def vial_label(self, keycode):
        if keycode in KEY_LABELS:
            return KEY_LABELS[keycode]
        if re.fullmatch(r"KC_[A-Z0-9]+", keycode):
            return keycode.removeprefix("KC_")

        match = re.fullmatch(r"LSFT\((.+)\)", keycode)
        if match:
            return SHIFTED_LABELS[match.group(1)]

        match = re.fullmatch(r"LGUI\((.+)\)", keycode)
        if match:
            return f"Cmd+{self.vial_label(match.group(1))}"

        match = re.fullmatch(r"(?:L|R)(?:ALT|CTL|SFT)_T\((.+)\)", keycode)
        if match:
            return self.vial_label(match.group(1))

        match = re.fullmatch(r"LT\d\((.+)\)", keycode)
        if match:
            return self.vial_label(match.group(1))

        match = re.fullmatch(r"TD\((\d+)\)", keycode)
        if match:
            return self.vial_label(self.vial["tap_dance"][int(match.group(1))][0])

        self.fail(f"No display conversion is defined for Vial keycode {keycode!r}")

    def test_all_seven_layers_match_vial_matrix(self):
        self.assertEqual([layer["id"] for layer in self.visualizer["layers"]], list(LAYER_IDS))
        self.assertEqual(set(self.visualizer["layerData"]), set(LAYER_IDS))

        for layer_index, layer_id in enumerate(LAYER_IDS):
            web_layer = self.visualizer["layerData"][layer_id]
            self.assertEqual(set(web_layer), set(MATRIX_COORDINATES.values()))

            for coordinate, visualizer_id in MATRIX_COORDINATES.items():
                matrix_row, matrix_column = coordinate
                keycode = self.vial["layout"][layer_index][matrix_row][matrix_column]
                expected = self.vial_label(keycode)
                if ACTIVE_LAYER_KEYS.get(layer_id) == visualizer_id:
                    self.assertIn(keycode, {"KC_NO", "KC_TRNS"})
                    expected = "___"
                actual = primary_visualizer_label(web_layer[visualizer_id])
                self.assertEqual(
                    actual,
                    expected,
                    f"{layer_id}.{visualizer_id} must match Vial matrix {coordinate} ({keycode})",
                )

    def test_referenced_tap_dances_match_labels_holds_and_timings(self):
        base_layer = self.visualizer["layerData"]["base"]
        tap_dance_keys = {
            visualizer_id: keycode
            for coordinate, visualizer_id in MATRIX_COORDINATES.items()
            if (keycode := self.vial["layout"][0][coordinate[0]][coordinate[1]]).startswith("TD(")
        }
        self.assertEqual(set(tap_dance_keys), {"L22", "R22"})

        for visualizer_id, keycode in tap_dance_keys.items():
            tap, hold, _, _, timing = self.vial["tap_dance"][int(keycode[3:-1])]
            tooltip = self.visualizer["tooltips"][visualizer_id]
            self.assertEqual(primary_visualizer_label(base_layer[visualizer_id]), self.vial_label(tap))
            self.assertIn(f"Tap Dance: {self.vial_label(tap)}/{self.vial_label(hold)}", tooltip)
            self.assertIn(f"({timing}ms timing)", tooltip)

    def test_all_eight_vial_combos_match_visualizer_reference(self):
        active_combos = [combo for combo in self.vial["combo"] if combo[-1] != "KC_NO"]
        self.assertEqual(len(active_combos), 8)

        expected_rows = {}
        result_labels = {
            "KC_ESCAPE": "Escape",
            "LGUI(KC_Q)": "Quit App (Cmd+Q)",
            "OSM(MOD_LGUI)": "GUI/Super modifier",
            "OSM(MOD_MEH)": "MEH (Alt+Ctrl+Shift)",
            "KC_QUOTE": "Quote (')",
            "LGUI(KC_C)": "Copy (Cmd+C)",
            "LGUI(KC_X)": "Cut (Cmd+X)",
        }
        for combo in active_combos:
            trigger = " + ".join(self.vial_label(key) for key in combo[:-1] if key != "KC_NO")
            expected_rows[trigger] = result_labels[combo[-1]]

        page = (ROOT / "index-qwerty.html").read_text()
        combo_rows = re.findall(
            r'<div class="flex justify-between items-center p-2 bg-gray-50 rounded">\s*'
            r'<span[^>]*>([^<]+)</span>\s*<span[^>]*>→</span>\s*<span>([^<]+)</span>',
            page,
        )
        self.assertEqual(dict(combo_rows), expected_rows)

    def test_every_visualizer_has_qwerty_navigation(self):
        pages = sorted(ROOT.glob("index*.html"))
        self.assertGreater(len(pages), 1)
        for page in pages:
            contents = page.read_text()
            if page.name == "index-qwerty.html":
                self.assertIn("Current: Silakka54 QWERTY", contents)
            else:
                self.assertIn('href="index-qwerty.html"', contents, page.name)


if __name__ == "__main__":
    unittest.main()
