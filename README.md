# Miryoku Silakka54 Layout

🚀 **V1 Ready** - Traditional HRM layout is production-ready! Other versions are work-in-progress.

An interactive Vue.js-based visualization and educational resource for adapting the Miryoku keyboard layout system to the Silakka54 split keyboard.

## Overview

This project provides both educational documentation and an interactive web-based visualizer for understanding and implementing the ergonomic Miryoku layout on a 54-key split keyboard. Miryoku is a modern keyboard layout system that reduces a full keyboard's functionality to just 36 keys through intelligent layering and home row modifiers.

Miryoku operates on **five core principles**: using layers instead of reaching, employing both hands instead of contortions, maximizing home position usage, leveraging thumbs as primary controls, and avoiding unnecessary complication. These principles manifest in a **3×5+3 configuration** where fingers never move more than one unit from their home positions.

The Silakka54 represents the ideal adaptation target - **54-60 key layouts hit a sweet spot** with enough extra keys for meaningful enhancements without overwhelming the minimalist philosophy, as noted in community research.

## Features

- **Interactive Vue.js Visualizer**: Modern reactive interface with dynamic layer switching
- **Configuration-Driven Architecture**: JSON-based layout definitions for easy customization
- **Multiple Layout Versions**: 5 different approaches to Miryoku implementation
  - 🟢 **Traditional HRM** (V1): 6-Layer with Home Row Modifiers - **READY**
  - 🟡 **Optimized 4-Layer** (V2): Reduced layers with direct symbol access - **WIP**
  - 🟡 **No HRM Dedicated** (V3): 6-Layer with dedicated modifier keys - **WIP**
  - 🟡 **4-Layer Balanced** (V4): Balance of simplicity and efficiency - **WIP**
  - 🟡 **Coding Optimized** (V5): Programming-focused enhancements - **WIP**
- **Interactive Tooltips**: Hover over any key to see detailed explanations
- **Educational Guide**: Comprehensive documentation of Miryoku principles and adaptation strategies
- **Layer Switching Guide**: Step-by-step instructions for each version
- **Version Navigation**: Easy comparison with status indicators
- **Color-coded Keys**: Visual distinction between home row, thumb keys, and extra keys
- **No Build System**: Pure HTML/CSS/JS with CDN dependencies

## Quick Start

### Local Development

Serve the project locally using npx:

```bash
npx serve
```

Then open your browser to the displayed URL (typically `http://localhost:3000`).

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

## How to Use This Layout

### Understanding the Layer System

The Miryoku layout uses **6 layers with orthogonal functionality** - each layer serves a single purpose per hand and is accessed through thumb-key holds on the opposite hand:

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
- Hold Tab → Numbers layer (numpad layout)

Right Thumb Hold → Left Hand Layers  
- Hold Enter → Symbols layer (punctuation, operators)
- Hold Escape → Function layer (F-keys, system)
```

### Visualizer Usage

1. Open the visualizer in your browser
2. Click layer buttons to switch between keyboard layers
3. Hover over keys to see their functions and modifiers
4. Note the color coding: blue for home row, green for thumb keys
5. Use this as reference when configuring your firmware

### Recommended Implementation (V2 Approach)

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

#### Optimized Version (index-v2.html)
- **Direct symbol access**: "Backtick (`) key | Shift: Tilde (~)"
- **Combined layers**: "Space key | Hold: Nav/Function layer (combined!)"
- **Efficiency notes**: Highlights reduced layer switching requirements

#### No HRM Version (index-v3.html)
- **Dedicated modifiers**: "Dedicated Control modifier (always Ctrl)"
- **Layer states**: "Layer inactive (not being held)" for "---" keys
- **Traditional feel**: Familiar modifier placement explanations

#### Coding Optimized Version (index-v5.html)
- **Direct bracket access**: "Direct brackets: [ and ] keys (no layer needed)"
- **IDE shortcuts**: "F5: Start debugging or run code", "Ctrl+D: Duplicate current line"
- **Code navigation**: "Alt+↑: Move line up", "Ctrl+/: Toggle line comment"
- **Numbers layer combo**: "Hold both Code + Nav keys simultaneously for numpad access"
- **Programming focus**: Optimized tooltips for coding workflows and IDE integration

### Version Navigation
Each layout includes navigation buttons to easily compare between:
- **Traditional HRM**: Full Miryoku experience with home row modifiers
- **Optimized 3-Layer**: Reduced complexity with direct symbol access
- **No HRM Dedicated**: Familiar modifier keys for easier transition
- **4-Layer Balanced**: Perfect balance between simplicity and efficiency
- **Coding Optimized**: Programming-focused with direct bracket access and IDE shortcuts

## Architecture

### Modern Vue.js Implementation
- **Frontend**: Vue.js 3 with CDN import (no build system)
- **Styling**: Tailwind CSS for responsive design
- **Data**: JSON configuration files for each layout version
- **Deployment**: Static files, works with any web server

### File Structure

- `index.html` - V1 Traditional HRM layout (Vue.js app)
- `app.json` - V1 configuration data
- `index-v2.html` - V2 Optimized 4-Layer layout (Vue.js app)
- `app-v2.json` - V2 configuration data
- `Keyboard layout.md` - **Comprehensive Miryoku adaptation guide** with detailed research on successful implementations, community feedback, and specific Silakka54 recommendations
- `CLAUDE.md` - Development guidance for Claude Code

## Layout Layers

1. **Base** - Colemak-DH alpha layout with home row modifiers
2. **Navigation** - Arrow keys, page navigation, clipboard operations
3. **Symbols** - Special characters and punctuation marks
4. **Numbers** - Numeric keypad layout
5. **Function** - F-keys and system functions
6. **Media** - Volume and playback controls

## Key Principles

- **Home Row Modifiers**: GACS pattern (GUI, Alt, Ctrl, Shift)
- **Layer Switching**: Thumb keys for accessing different layers
- **Ergonomic Design**: Minimize finger movement and maximize comfort
- **3×5+3 Core**: Preserve Miryoku's 36-key essence within the 54-key layout

## Development Status

### ✅ V1 - Traditional HRM (Production Ready)
- Full 6-layer Miryoku implementation
- Home row modifiers (GACS pattern)
- Complete Vue.js refactoring
- JSON configuration system
- Interactive tooltips and layer switching

### 🚧 V2 - Optimized 4-Layer (Work in Progress)
- Reduced to 4 layers for efficiency
- Direct symbol access on base layer
- Separated Navigation and Function layers
- Vue.js implementation complete
- UI refinements ongoing

### 🚧 V3-V5 (Planned)
- V3: No HRM Dedicated modifiers
- V4: 4-Layer Balanced approach  
- V5: Coding-optimized version
- Vue.js refactoring pending

## Contributing

This project uses Vue.js 3 with a configuration-driven architecture:

1. **Fork the repository**
2. **Edit configuration**: Modify `app.json` or `app-v2.json` for layout changes
3. **Test locally**: Use `npx serve` to run development server
4. **Add new versions**: Create new `index-vX.html` and `app-vX.json` files
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

## Resources

- [Miryoku Official Repository](https://github.com/manna-harbour/miryoku) - Original layout and documentation
- [Miryoku QMK Reference](https://github.com/manna-harbour/miryoku_qmk) - QMK implementation
- [Colemak-DH Layout](https://colemakmods.github.io/mod-dh/) - Optimized alpha layout
- [Alternative Keyboard Layouts Guide](https://getreuer.info/posts/keyboards/alt-layouts/index.html#which-alt-keyboard-layout-should-i-learn) - Comprehensive comparison and selection guide
- [QMK Firmware](https://qmk.fm/) - Customizable keyboard firmware
- [ZMK Firmware](https://zmk.dev/) - Wireless keyboard firmware
- [Vial](https://vial.rocks/) - GUI for QMK configuration
- [Home Row Mods Guide](https://precondition.github.io/home-row-mods) - Detailed implementation guide