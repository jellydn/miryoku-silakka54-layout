# Miryoku Silakka54 Layout

[![All Contributors](https://img.shields.io/github/all-contributors/jellydn/miryoku-silakka54-layout?color=ee8449&style=flat-square)](#contributors-)

🚀 **Ready** - Graphite (default), Colemak-DH and QWERTY layouts for the Silakka54, and Corne layouts.

A comprehensive implementation suite for the Miryoku keyboard layout system adapted to the Silakka54 split keyboard, with firmware-based layouts (Vial - ✅ Tested), software-based layouts (Kanata - ⚠️ Untested/WIP), and educational visualizations (Web UI - ✅ Ready). Implementation coverage differs by variant; the QWERTY variant currently supports Vial and the Web UI.

## Overview

This project provides both educational documentation and an interactive web-based visualizer for understanding and implementing the ergonomic Miryoku layout on a 54-key split keyboard. Miryoku is a modern keyboard layout system that reduces a full keyboard's functionality to just 36 keys through intelligent layering and home row modifiers.

Miryoku operates on **five core principles**: using layers instead of reaching, employing both hands instead of contortions, maximizing home position usage, leveraging thumbs as primary controls, and avoiding unnecessary complication. These principles manifest in a **3×5+3 configuration** where fingers never move more than one unit from their home positions.

The Silakka54 represents the ideal adaptation target - **54-60 key layouts hit a sweet spot** with enough extra keys for meaningful enhancements without overwhelming the minimalist philosophy, as noted in community research.

## Implementation Options

Choose the approach that best fits your needs:

### 🎛️ **Vial Configuration** (Firmware-based) ✅ TESTED & WORKING
- **Best for**: Split keyboard owners who want real-time configuration
- **Location**: `vial/` folder
- **Status**: The Colemak-DH and QWERTY saved layouts are production-ready and tested
- **Pros**: Real-time changes, visual interface, no software required
- **Cons**: Requires Vial-compatible firmware

### ⌨️ **Kanata Configuration** (Software-based) ⚠️ UNTESTED/WIP
- **Best for**: Any keyboard (MacBook, Keychron K7, standard keyboards)
- **Location**: `kanata-v1.kbd` (split) & `kanata-standard-keyboards.kbd` (standard)
- **Status**: Work in progress - configuration created but not tested
- **Pros**: Works with any keyboard, no firmware flashing required
- **Cons**: Software must run in background, needs testing

### 🌐 **Web Visualizer** (Educational) ✅ READY
- **Best for**: Learning the layout, reference, and planning
- **Location**: `index.html` and related files
- **Status**: Fully functional and tested
- **Pros**: Interactive learning, no installation, works anywhere
- **Cons**: Visualization only, not functional

## Features

- **Variant-specific Implementations**: Each layout lists its supported Vial, Kanata, and Web UI options
- **Interactive Vue.js Visualizer**: Modern reactive interface with dynamic layer switching
- **Real Vial Configuration**: Tested and optimized firmware configuration
- **Dual Kanata Support**: Configurations for both split and standard keyboards
- **Configuration-Driven Architecture**: JSON-based layout definitions for easy customization
- **Multiple Layouts**: Silakka54 and Corne variants of the Miryoku layout
  - 🟢 **Traditional HRM** (V1): 7-Layer with Home Row Modifiers - **READY**
  - 🟢 **Silakka54 QWERTY**: Tested Vial layout with Vim-style navigation - **READY**
  - 🟢 **Corne (Colemak-DH)**: Optimized for 3x6+3 split keyboards - **READY**
  - 🟢 **Corne (Gallium)**: Alternative alphabet layout for Corne - **READY**
  - 🟢 **Corne (Enthium v13)**: Enthium v13 layout with improved pinky comfort - **READY**
  - 🟢 **Corne (Promethium)**: Promethium layout adapted from `promethium.vil` - **READY**
  - 🟢 **Silakka54 (Graphite)**: Graphite alphabet layout for Silakka54 - **READY**
- **Interactive Tooltips**: Hover over any key to see detailed explanations
- **Educational Guide**: Comprehensive documentation of Miryoku principles and adaptation strategies
- **Layer Switching Guide**: Step-by-step instructions for each version
- **Board and Layout Switch**: Select the board and the base layout at the top of `index.html`
- **Color-coded Keys**: Visual distinction between home row, thumb keys, and extra keys
- **No Build System**: Pure HTML/CSS/JS with CDN dependencies

## Quick Start

### Choose Your Implementation

#### For Split Keyboards (Silakka54)
> **Note:** The maintainer's Silakka54 now runs **ZMK** with the Graphite layout:
> [jellydn/zmk-config](https://github.com/jellydn/zmk-config) (`config/base.keymap`, `config/combos.dtsi`).
> The web visualizer follows that config. `vial/miryoku-silakka54-graphite.vil` is the older Vial
> export of the same layers (4 combos at 35 ms). Keep it for reference only.

1. **Vial (Firmware)**: Choose a saved layout:
   - Graphite (reference; the ZMK config is the source): `vial/miryoku-silakka54-graphite.vil`
   - Colemak-DH (original): `vial/miryoku-silakka54-vial-config.json`
   - QWERTY: `vial/miryoku-silakka54-qwerty.vil`
   - Corne v4.1 Graphite (46 keys): `vial/miryoku-corne-v41-graphite.vil`
   ```bash
   # Install Vial, connect the keyboard, and load your chosen layout
   # If Vial treats the legacy JSON as a keyboard definition, copy it to a
   # filename ending in .vil and use File → Load saved layout
   # See vial/README.md for detailed instructions
   ```

2. **Kanata (Software)**: Use `kanata-v1.kbd` for the Colemak-DH V1 layout ⚠️ UNTESTED. A QWERTY Kanata configuration is not currently provided.
   ```bash
   sudo kanata --cfg kanata-v1.kbd
   # See KANATA.md for detailed instructions
   # WARNING: Configuration not yet tested - may need adjustments
   ```

#### For Standard Keyboards (MacBook, Keychron K7)
1. **Kanata (Software)**: Use `kanata-standard-keyboards.kbd` ⚠️ UNTESTED
   ```bash
   sudo kanata --cfg kanata-standard-keyboards.kbd
   # See KANATA.md for detailed instructions
   # WARNING: Configuration not yet tested - may need adjustments
   ```

#### For Learning & Reference
1. **Web Visualizer**: Open `index.html`. Select the board (Silakka54 or Corne v4.1) and the base
   layout (Graphite, Colemak-DH or QWERTY). Graphite on the Silakka54 is the default. The selection
   is in the URL, for example `index.html?base=qwerty` or `index.html?board=corne`.
   ```bash
   npx serve
   # Then open browser to displayed URL (typically http://localhost:3000)
   ```

### Local Development

Serve the project locally using npx:

```bash
npx serve
```

Then open your browser to the displayed URL (typically `http://localhost:3000`).

Validate the Vial-to-visualizer contracts (QWERTY, Graphite for Silakka54 and Corne v4.1) and the JSON files before you submit changes:

```bash
python3 -m unittest discover -s tests -v
jq empty app*.json vial/*.json vial/*.vil .all-contributorsrc
git diff --check
```

### Get Official Miryoku Layer Specifications

To check against official Miryoku layer specifications:

```bash
npx degit manna-harbour/miryoku/data/layers#master miryoku-layers
```

This downloads the official Miryoku layer JSON files for reference and validation.

### Alternative Servers

```bash
# Python 3
python3 -m http.server 8000

# Python 2
python -m http.server 8000

# Node.js live-server
npx live-server
```

### Direct Access

You can also open `index.html` directly in your web browser, though some features may work better with a local server.

## Implementation Comparison

| Feature | Vial ✅ | Kanata ⚠️ | Web Visualizer ✅ |
|---------|----------|------------|-------------------|
| **Status** | **TESTED & WORKING** | **UNTESTED/WIP** | **READY** |
| **Target Users** | Split keyboard owners | Any keyboard users | Everyone |
| **Setup Complexity** | Medium (firmware flash) | Low (software install) | None (browser) |
| **Real-time Changes** | ✅ Instant | ❌ Restart required | ❌ Reference only |
| **Keyboard Support** | Vial-compatible only | Any keyboard | N/A |
| **Background Software** | ❌ None needed | ✅ Runs in background | ❌ None needed |
| **Offline Usage** | ✅ Always works | ✅ Always works | ✅ Always works |
| **Configuration Backup** | ✅ Export/import `.vil` | ✅ File-based config | ❌ Display only |
| **Learning Curve** | Low (GUI) | Medium (config files) | None (visual) |
| **Advanced Features** | ✅ Full Vial features | ✅ Full Kanata features | ❌ Display only |

### When to Use Which

- **Use Vial** if you have a compatible split keyboard and want the easiest real-time configuration
- **Use Kanata** if you have any keyboard and want software-based remapping
- **Use Web Visualizer** for learning, reference, or if you're planning your setup

The Colemak-DH V1 files provide the Vial, Kanata, and Web UI approaches. The QWERTY variant currently provides Vial and Web UI files only. Check each variant before switching because its layer mappings and combos can differ.

## How to Use This Layout

### Understanding the Layer System

The Miryoku layout uses **multiple layers with orthogonal functionality** - each layer serves a single purpose per hand and is accessed through thumb-key holds on the opposite hand:

- **Base layer**: Colemak-DH alpha layout with essential punctuation
- **Navigation layer** (right hand): Inverted-T arrow arrangement, clipboard functions, page controls
- **Symbols layer** (left hand): Direct access to shifted numbers and programming symbols
- **Numbers layer**: Standard numpad arrangement 
- **Function layer**: F1-F12 in logical positions
- **Media layer**: System controls and media functions

**Key concepts:**
- **Tap thumb keys**: Space, Enter, Backspace (primary functions)
- **Hold thumb keys**: Activate layers on the opposite hand
- **Home row modifiers**: GACS pattern (GUI on pinkies, Alt on ring, Ctrl on middle, Shift on index)
- **Orthogonal design**: Each layer serves distinct functions to ensure intuitive access patterns

### Layer Access Pattern

```
Left Thumb Hold → Right Hand Layers
- Hold Space → Navigation layer (arrows, clipboard)
- Hold Tab → Mouse layer (pointer and wheel controls)

Right Thumb Hold → Left Hand Layers
- Hold Enter → Symbols layer (punctuation, operators)
- Hold Backspace → Numbers layer (numpad layout)
- Hold Delete → Function layer (F-keys, system)

Left Thumb Hold → Media Layer
- Hold Escape → Media layer (playback and volume controls)
```

### Visualizer Usage

1. Open the visualizer in your browser
2. Click layer buttons to switch between keyboard layers
3. Hover over keys to see their functions and modifiers
4. Note the color coding: blue for home row, green for thumb keys
5. Use this as reference when configuring your firmware

### Recommended Implementation

Based on community feedback and ergonomic research, follow this implementation order. **Home row modifiers represent the steepest learning curve, requiring 2-3 weeks of dedicated practice**, but the ergonomic benefits justify this investment.

#### Phase 1: Core Foundation (Week 1-2)
1. **Preserve the sacred core** - Center the 36-key Miryoku layout within Silakka54's arrangement
2. **Start with base layer only** - Focus on Colemak-DH layout (or specify `MIRYOKU_ALPHAS=QWERTY/DVORAK` if preferred)
3. **Add home row modifiers gradually** - Begin with just Shift on index fingers, symmetric mirroring for both hands
4. **Practice daily** - 15-30 minutes of deliberate practice
5. **Use typing tests** - Focus on accuracy over speed initially

#### Phase 2: Layer Integration (Week 3-4)  
1. **Add Navigation layer** - Hold space for inverted-T arrows, clipboard (Cut/Copy/Paste on bottom row)
2. **Master thumb holds** - Practice the tap vs hold distinction with dual-function approach
3. **Add Symbols layer** - Direct access eliminates three-key chords (e.g., "!" = Sym + 1)
4. **Adjust timing** - Fine-tune tapping terms: 240ms for pinkies, 160ms for index fingers

#### Phase 3: Full System & Silakka54 Enhancements (Week 5-6)
1. **Add remaining layers** - Numbers (numpad layout), Function (F1-F12), Media
2. **Utilize number row strategically** - Place 1-0 above alphas for immediate access
3. **Follow overflow patterns** - Use outer columns for [, ], ; in standard positions
4. **Enhance thumb clusters** - Extra positions for Tab/Escape or specialized toggles
5. **Consider combos** - Adjacent key combinations (JK→Escape, DF→Tab) for virtual expansion

### Adaptation Timeline Expectations

Research shows consistent patterns in successful adaptations:

- **Days 1-7**: Frustrating but normal - expect 30-50% speed reduction
- **Days 8-21**: Gradual improvement - speed recovery to 70-80%  
- **Days 22-42**: Muscle memory formation - approach original speed
- **Days 43+**: Ergonomic benefits realized - potential speed increase

**Critical insight**: The most effective approach treats the 36-key core as inviolate, using extra keys as functional enhancements rather than replacements. The Silakka54's extra keys should feel like natural extensions rather than departures from Miryoku's elegant design.

## Interactive Features

### Tooltip System
All layout versions now include comprehensive tooltips that appear when you hover over any key:

#### Traditional Version (index.html)
- **Home row modifiers**: "A key | Hold: GUI/Super modifier"
- **Layer switching**: "Space key | Hold: Navigation layer" 
- **Dual-function keys**: Clear explanation of tap vs hold behavior

## Architecture

### Modern Vue.js Implementation
- **Frontend**: Vue.js 3 with CDN import (no build system)
- **Styling**: Tailwind CSS for responsive design
- **Data**: JSON configuration files for each layout version
- **Deployment**: Static files, works with any web server

### File Structure

- `index.html` - Main visualizer with the board and base layout switch (Vue.js app). The title, description and Open Graph tags are static HTML, so link previews and search engines see real text.
- `app-graphite.json` - Silakka54 Graphite data (default). Layers come from `vial/miryoku-silakka54-graphite.vil`; combos come from the ZMK config.
- `app-corne-graphite.json` - Corne v4.1 Graphite data (46 keys), from `vial/miryoku-corne-v41-graphite.vil`
- `app.json` - Silakka54 Colemak-DH (V1) data
- `app-qwerty.json` - Silakka54 QWERTY data with Vim-style navigation
- `index-graphite.html`, `index-qwerty.html` - Redirects to `index.html`, so old links continue to work
- `index-corne.html` - Corne 42-key Colemak-DH layout (Vue.js app)
- `app-corne.json` - Corne Colemak-DH configuration data
- `index-corne-gallium.html` - Corne 42-key Gallium layout (Vue.js app)
- `app-corne-gallium.json` - Corne Gallium configuration data
- `index-corne-enthium.html` - Corne 42-key Enthium v13 layout (Vue.js app)
- `app-corne-enthium.json` - Corne Enthium v13 configuration data
- `index-corne-promethium.html` - Corne 42-key Promethium layout (Vue.js app)
- `app-corne-promethium.json` - Corne Promethium configuration data
- `Keyboard layout.md` - **Comprehensive Miryoku adaptation guide** with detailed research on successful implementations, community feedback, and specific Silakka54 recommendations
- `CLAUDE.md` - Development guidance for Claude Code

## Layout Layers

1. **Base** - Variant-specific alpha layout with home row modifiers
2. **Media** - Volume and playback controls
3. **Navigation** - Arrow keys, page navigation, clipboard operations
4. **Mouse** - Pointer, wheel, and button controls
5. **Symbols** - Special characters and punctuation marks
6. **Numbers** - Numeric keypad layout
7. **Function** - F-keys and system functions

## Key Principles

- **Home Row Modifiers**: GACS pattern (GUI, Alt, Ctrl, Shift)
- **Layer Switching**: Thumb keys for accessing different layers
- **Ergonomic Design**: Minimize finger movement and maximize comfort
- **3×5+3 Core**: Preserve Miryoku's 36-key essence within the 54-key layout

## Development Status

### ✅ V1 - Traditional HRM (Production Ready)
- Full 7-layer Miryoku implementation
- Home row modifiers (GACS pattern)
- Complete Vue.js refactoring
- JSON configuration system
- Interactive tooltips and layer switching

### ✅ Silakka54 QWERTY (Production Ready)
- Tested Vial saved layout in `vial/miryoku-silakka54-qwerty.vil`
- Standard QWERTY alpha arrangement with GACS home row modifiers
- Home row modifiers: GUI (A/;), Alt (S/L), Ctrl (D/K), Shift (F/J)
- Vim-style `H/J/K/L` movement on both Navigation and Mouse layers
- Eight combos moved with their physical key positions for QWERTY
- Matching web visualizer in `index-qwerty.html` and `app-qwerty.json`

### ✅ Corne 42-Key Layouts (Production Ready)

#### Corne (Colemak-DH)
- Optimized for 3x6+3 split keyboards (Corne, Lily58, etc.)
- Pure Miryoku layout without extra keys
- 5 layers: Base, Navigation, Mouse, Symbols, Numbers, Function
- Standard home row modifiers (GACS pattern)
- Clean Escape key (no layer functionality)
- Perfect for users wanting authentic Miryoku experience

#### Corne (Gallium)
- Alternative alphabet layout optimized for finger balance
- 6 layers: Base (Gallium), Navigation, Mouse, Symbols, Numbers, Function
- Home row modifiers: GUI (N/I), Alt (R/E), Ctrl (T/A), Shift (S/H)
- 8 combo keys for efficiency (imported from Vial configuration)
- Base layout: B-L-D-C-V (left) / J-Y-O-U-, (right)
- Perfect for users wanting optimized letter placement with Miryoku principles

#### Corne (Enthium v13)
- Latest Enthium v13 (PWF/;) layout with significant ergonomic improvements
- Clockwise rotation of PWF and swap of /; compared to Enthium v12
- 6 layers: Base (Enthium), Navigation, Mouse, Symbols, Numbers, Function
- Home row modifiers: GUI (C/S), Alt (I/N), Ctrl (A/T), Shift (E/H)
- 7 combo keys for missing letters and modifiers (Q, Z, V, Hyper, Meh, Escape, Enter)
- Base layout:
  - Top row: [ Q Y O U = ] (left) / Z X L P D - (right)
  - Home row: B C I A E - (left) / W S N T H K (right)
  - Bottom row: ( ' , . / ; (left) / ) J M G F V (right)
- Right thumb cluster: Backspace/Sym → R/Num → Empty (left to right)
- Performance improvements over v12:
  - 52.5% reduction in long-distance row jumps
  - 30% reduction in right pinky same-finger bigrams
  - 9.63% reduction in pinky off-home movements
  - Restores P on upper row for comfortable SP, PL, PH, XP rolls
  - Moves W to home row pinky, converting WN to inward roll
  - Moves F to lower row ring finger for better ergonomics
- Perfect for users wanting the latest optimized Enthium layout with enhanced comfort

#### Corne (Promethium)
- Promethium layout imported from `~/Projects/dotfiles/mics/corne/promethium.vil`
- 6 layers: Base (Promethium), Navigation, Mouse, Symbols, Numbers, Function
- Home row modifiers: GUI (S/C), Alt (N/I), Ctrl (T/E), Shift (H/A)
- 4 combos: Y+U → Escape, P+L → Enter, W+G → Hyper, '+. → Meh
- Thumb behavior: Left (Esc, R/Nav, Tab/Mouse), Right (Enter, Space/Num, Backspace/Sym)
- Perfect for users wanting Promethium alpha positions with Miryoku-style layering

### ✅ Silakka54 (Graphite) - default

- Source: [jellydn/zmk-config](https://github.com/jellydn/zmk-config) (`config/base.keymap`, `config/combos.dtsi`). The Silakka54 runs ZMK.
- Graphite alphabet layout by [rdavison](https://github.com/rdavison/graphite-layout)
- 6 layers: Base (Graphite), Navigation, Mouse, Symbols, Numbers, Function (one-shot from Mouse)
- Home row modifiers: GUI (N/I), Alt (R/E), Ctrl (T/A), Shift (S/H)
- Base layout (3×5 core):
  - Left: `B L D W Z` / `N R T S G` / `Q X M C V`
  - Right: `' F O U J` / `Y H A E I` / `K P . - /`
- Thumbs: `=`, Space/Nav, Tab/Mouse | Enter/Sym, Backspace/Num, `;`
- 11 combos, base layer only, combo term 50 ms:
  - B+L → Esc, F+U → Esc, L+W → Enter, B+L+D → Cmd+Q
  - L+D → sticky GUI, D+W → sticky Hyper, F+O → sticky Meh, .+- → sticky Meh
  - Q+X → Cut, X+M → Copy, O+U → `'`
- Shift overrides: Shift+`'` → `_`, Shift+`,` → `?`, Shift+`-` → `"`, Shift+`/` → `<`
- Upcoming ([zmk-config PR #4](https://github.com/jellydn/zmk-config/pull/4), not merged): Leader key. Leader `B O O T` enters the bootloader, Leader `R E S E T` restarts the half.

### ✅ Corne v4.1 (Graphite)

- Source: `qmk/corne-v4.1-graphite.vil` in [jellydn/zmk-config](https://github.com/jellydn/zmk-config), copied to `vial/miryoku-corne-v41-graphite.vil`
- 46 keys: 3×6, 3 thumbs and 2 extra keys per half
- Same Graphite layers, 11 combos (50 ms, base layer only) and shift overrides as the Silakka54
- Extra keys on the base layer: left ← and Play/Pause, right → and Next track. Outer thumbs: `=` and `;`
- RGB: Typing Heatmap is the default effect after a Vial EEPROM reset

## Contributing

This project uses Vue.js 3 with a configuration-driven architecture:

1. **Fork the repository**
2. **Edit configuration**: Modify the `app*.json` file of the layout
3. **Test locally**: Use `npx serve` to run development server
4. **Add new versions**: Add an `app-<name>.json` file and an entry in `LAYOUTS` in `index.html`
5. **Submit pull request**

### Adding New Layout Versions
1. Copy `index.html` → `index-vX.html`
2. Copy `app.json` → `app-vX.json`
3. Update configuration in JSON file
4. Update version navigation in HTML
5. Test with local server

## Firmware Implementation

### QMK Setup (Recommended)

1. **Enable Required Features** in `config.h`:
   ```c
   #define PERMISSIVE_HOLD
   #define TAPPING_TERM 200
   #define TAPPING_TERM_PER_KEY
   ```

2. **Configure Home Row Modifiers**:
   ```c
   // Left: GUI(A), Alt(R), Ctrl(S), Shift(T)
   // Right: Shift(N), Ctrl(E), Alt(I), GUI(O)
   LGUI_T(KC_A), LALT_T(KC_R), LCTL_T(KC_S), LSFT_T(KC_T)
   ```

3. **Set Per-Key Timing**:
   ```c
   uint16_t get_tapping_term(uint16_t keycode, keyrecord_t *record) {
       switch (keycode) {
           case LSFT_T(KC_T): return 160;  // Index fingers (faster)
           case LGUI_T(KC_A): return 240;  // Pinkies (slower)
           default: return TAPPING_TERM;
       }
   }
   ```

### Vial Setup (GUI Alternative)

1. Flash Vial-compatible firmware for your keyboard
2. Open Vial application and connect keyboard
3. Configure **Tap Hold** keys for home row modifiers
4. Set thumb keys as **Layer Tap** (tap for key, hold for layer)
5. Adjust timing in Settings → Tap-Hold Settings (200ms base)

### ZMK Setup (Wireless Option)

1. **Configure Hold-Tap Behaviors**:
   ```
   &mt {
       flavor = "balanced";
       tapping-term-ms = <200>;
   };
   ```

2. **Use Different Flavors by Position**:
   - `balanced` for most keys
   - `tap-preferred` for index fingers
   - Longer timing for weaker fingers

### Silakka54-Specific Adaptations

Following successful community implementations and the documented **56-key Sofle adaptation** best practices:

- **Preserve the sacred core** - Center the 36-key Miryoku layout exactly as standard specification
- **Strategic number row** - Place 1-0 in familiar positions, consider leaving outermost positions for layer toggles
- **Established outer patterns** - Follow Miryoku's overflow logic: [, ], ; in standard row positions for muscle memory
- **Thoughtful thumb enhancement** - Use 1-2 extra thumb positions for specialized toggles (gaming mode, function lock) or workflow-specific operations
- **Full keyboard layer** - Implement specialized layer activating all 54 keys for gaming/applications
- **Virtual expansion via combos** - Adjacent key combinations (JK→Escape, DF→Tab) can add 6-8 virtual keys without physical additions

**Key principle**: Extra keys should provide convenient access to additional functions without compromising the ergonomic benefits of the core layout. The goal is enhancing Miryoku's philosophy rather than replacing it.

## Home Row Modifiers Configuration

Home row modifiers are often the most challenging aspect of Miryoku but provide significant ergonomic benefits once mastered. Proper configuration is crucial for a smooth experience.

### Common Issues and Solutions

**Problem**: Slow response, accidental modifier activation, or typing errors with home row mods  
**Solution**: Optimize your tap-hold settings based on your typing style and keyboard firmware

### Vial Configuration (GUI Method)

If you're using Vial to configure your keyboard, navigate to **Settings → Tap-Hold Settings** and optimize these parameters:

#### Core Settings

| Setting | Recommended Value | Purpose |
|---------|------------------|---------|
| **Tapping Term** | 160-175ms (fast typists)<br>175-190ms (normal speed) | How long to hold before registering as modifier |
| **Permissive Hold** | ✅ Enabled | Makes firmware more lenient about registering holds |
| **Ignore Mod Tap Interrupt** | ✅ Enabled | Prevents accidental modifier activation during fast typing |
| **Tapping Force Hold** | ❌ Disabled | Would require holding for full term (less responsive) |
| **Retro Tapping** | ❌ Disabled | Not useful for home row mods |

#### Advanced Settings

| Setting | Value | Notes |
|---------|-------|-------|
| **Tap Code Delay** | 0ms | Fine as default |
| **Tap Hold Caps Delay** | 80ms | Fine as default |
| **Tapping Toggle** | 5 | Not relevant for HRM |

### QMK Advanced Configuration

For more precise control, implement per-key timing based on finger strength and usage patterns:

```c
// In your keymap.c
uint16_t get_tapping_term(uint16_t keycode, keyrecord_t *record) {
    switch (keycode) {
        // Index fingers - strongest, fastest
        case LSFT_T(KC_T):  // Left index
        case RSFT_T(KC_N):  // Right index
            return 150;
            
        // Middle fingers - strong, reliable
        case LCTL_T(KC_S):  // Left middle
        case RCTL_T(KC_E):  // Right middle
            return 160;
            
        // Ring fingers - weaker, need more time
        case LALT_T(KC_R):  // Left ring
        case RALT_T(KC_I):  // Right ring
            return 180;
            
        // Pinkies - weakest, slowest
        case LGUI_T(KC_A):  // Left pinky
        case RGUI_T(KC_O):  // Right pinky
            return 200;
            
        default:
            return TAPPING_TERM;
    }
}
```

### Troubleshooting Guide

#### Issue: Accidental Modifier Activation
**Symptoms**: Letters turn into modifier shortcuts (e.g., typing "the" triggers window switching)
**Solutions**:
1. ✅ Enable **Ignore Mod Tap Interrupt**
2. ✅ Enable **Permissive Hold**
3. 📉 Reduce **Tapping Term** by 10ms increments
4. 🎯 Practice deliberate tap vs hold motions

#### Issue: Modifiers Not Activating
**Symptoms**: Holding keys doesn't trigger modifiers when expected
**Solutions**:
1. 📈 Increase **Tapping Term** by 10ms increments
2. ✅ Ensure **Permissive Hold** is enabled
3. 🎯 Practice holding keys slightly longer
4. 🔄 Test with deliberate, slower movements

#### Issue: Inconsistent Behavior
**Symptoms**: Sometimes works, sometimes doesn't
**Solutions**:
1. 🎯 Implement per-key timing (stronger fingers = shorter timing)
2. 🎬 Record typing sessions to identify patterns
3. 📊 Use QMK debugging to analyze timing
4. 🔄 Gradual adaptation: start with longer timing, decrease over time

### Adaptation Strategy

#### Week 1: Foundation
- Start with **longer tapping terms** (200-220ms)
- Focus on **deliberate movements**
- Practice **tap vs hold distinction**
- Use **typing tests** to build muscle memory

#### Week 2-3: Optimization
- Gradually **reduce tapping terms** by 5-10ms
- Implement **per-key timing** for different fingers
- Focus on **common key combinations**
- Monitor and **adjust based on error patterns**

#### Week 4+: Mastery
- Fine-tune timing to personal preferences
- Develop **consistent finger pressure**
- Achieve **seamless modifier usage**
- Enjoy **ergonomic benefits** of reduced hand movement

### Firmware-Specific Notes

#### Vial/QMK
- Use the GUI for **real-time adjustments**
- **Save settings** after each change
- **Test thoroughly** before committing
- Consider **different profiles** for different typing contexts

#### ZMK (Wireless)
```devicetree
&mt {
    flavor = "balanced";
    tapping-term-ms = <175>;
    quick_tap_ms = <0>;
};
```

### Success Metrics

You'll know your configuration is optimal when:
- ✅ **95%+ typing accuracy** maintained
- ✅ **Modifiers activate reliably** when intended
- ✅ **No accidental shortcuts** during normal typing
- ✅ **Comfortable, natural feeling** key presses
- ✅ **Consistent behavior** across different typing speeds

Remember: **Perfect configuration is personal** - what works for others may need adjustment for your typing style, finger strength, and keyboard switch characteristics.

## Resources

- [Miryoku Official Repository](https://github.com/manna-harbour/miryoku) - Original layout and documentation
- [Miryoku QMK Reference](https://github.com/manna-harbour/miryoku_qmk) - QMK implementation
- [Enthium Layout](https://github.com/sunaku/enthium) - Engrammer meets Promethium keyboard layout
- [Enthium v13 Release](https://github.com/sunaku/enthium/releases/tag/v13) - Latest Enthium release with PWF/; improvements
- [Colemak-DH Layout](https://colemakmods.github.io/mod-dh/) - Optimized alpha layout
- [Alternative Keyboard Layouts Guide](https://getreuer.info/posts/keyboards/alt-layouts/index.html#which-alt-keyboard-layout-should-i-learn) - Comprehensive comparison and selection guide
- [QMK Firmware](https://qmk.fm/) - Customizable keyboard firmware
- [ZMK Firmware](https://zmk.dev/) - Wireless keyboard firmware
- [Vial](https://vial.rocks/) - GUI for QMK configuration
- [Home Row Mods Guide](https://precondition.github.io/home-row-mods) - Detailed implementation guide

## Contributors ✨

Thanks go to these contributors ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/jellydn"><img src="https://avatars.githubusercontent.com/u/870029?s=100" width="100px;" alt="Dung Duc Huynh (Kaka)"/><br /><sub><b>Dung Duc Huynh (Kaka)</b></sub></a><br /><a href="https://github.com/jellydn/miryoku-silakka54-layout/commits?author=jellydn" title="Code">💻</a> <a href="https://github.com/jellydn/miryoku-silakka54-layout/commits?author=jellydn" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/SlenderB13"><img src="https://avatars.githubusercontent.com/u/62191201?s=100" width="100px;" alt="Lucas Silva"/><br /><sub><b>Lucas Silva</b></sub></a><br /><a href="https://github.com/jellydn/miryoku-silakka54-layout/commits?author=SlenderB13" title="Code">💻</a> <a href="https://github.com/jellydn/miryoku-silakka54-layout/commits?author=SlenderB13" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://ampcode.com/"><img src="https://avatars.githubusercontent.com/u/289058786?s=100" width="100px;" alt="Amp"/><br /><sub><b>Amp</b></sub></a><br /><a href="https://github.com/jellydn/miryoku-silakka54-layout/commits?author=ampagent" title="Code">💻</a> <a href="https://github.com/jellydn/miryoku-silakka54-layout/commits?author=ampagent" title="Documentation">📖</a></td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td align="center" size="13px" colspan="7">
        <img src="https://raw.githubusercontent.com/all-contributors/all-contributors-cli/1b8533af435da9854653492b1327a23a4dbd0a10/assets/logo-small.svg">
          <a href="https://all-contributors.js.org/docs/en/bot/usage">Add your contributions</a>
        </img>
      </td>
    </tr>
  </tfoot>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [All Contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome.
