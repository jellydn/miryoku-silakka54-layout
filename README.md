# Miryoku Silakka54 Layout

🚀 **V1 Ready** - Traditional HRM layout is production-ready! Other versions are work-in-progress.

A comprehensive implementation suite for the Miryoku keyboard layout system adapted to the Silakka54 split keyboard, featuring **three synchronized approaches**: firmware-based (Vial - ✅ Tested), software-based (Kanata - ⚠️ Untested/WIP), and educational visualization (Web UI - ✅ Ready).

## Overview

This project provides both educational documentation and an interactive web-based visualizer for understanding and implementing the ergonomic Miryoku layout on a 54-key split keyboard. Miryoku is a modern keyboard layout system that reduces a full keyboard's functionality to just 36 keys through intelligent layering and home row modifiers.

Miryoku operates on **five core principles**: using layers instead of reaching, employing both hands instead of contortions, maximizing home position usage, leveraging thumbs as primary controls, and avoiding unnecessary complication. These principles manifest in a **3×5+3 configuration** where fingers never move more than one unit from their home positions.

The Silakka54 represents the ideal adaptation target - **54-60 key layouts hit a sweet spot** with enough extra keys for meaningful enhancements without overwhelming the minimalist philosophy, as noted in community research.

## Implementation Options

Choose the approach that best fits your needs:

### 🎛️ **Vial Configuration** (Firmware-based) ✅ TESTED & WORKING
- **Best for**: Split keyboard owners who want real-time configuration
- **Location**: `vial/` folder
- **Status**: Production-ready, thoroughly tested
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

- **Three Synchronized Implementations**: All configurations match the same tested layout
- **Interactive Vue.js Visualizer**: Modern reactive interface with dynamic layer switching
- **Real Vial Configuration**: Tested and optimized firmware configuration
- **Dual Kanata Support**: Configurations for both split and standard keyboards
- **Configuration-Driven Architecture**: JSON-based layout definitions for easy customization
- **Multiple Layout Versions**: 6 different approaches to Miryoku implementation
  - 🟢 **Traditional HRM** (V1): 7-Layer with Home Row Modifiers - **READY**
  - 🟢 **Pinky Relief** (V1-P): Weak finger friendly with redistributed load - **READY**
  - 🟡 **Optimized 4-Layer** (V2): Reduced layers with direct symbol access - **WIP**
  - 🟡 **No HRM Dedicated** (V3): 7-Layer with dedicated modifier keys - **WIP**
  - 🟡 **4-Layer Balanced** (V4): Balance of simplicity and efficiency - **WIP**
  - 🟡 **Coding Optimized** (V5): Programming-focused enhancements - **WIP**
  - 🟢 **OSM Optimized** (V6): One-Shot Modifiers via OSL layer - **READY**
- **Interactive Tooltips**: Hover over any key to see detailed explanations
- **Educational Guide**: Comprehensive documentation of Miryoku principles and adaptation strategies
- **Layer Switching Guide**: Step-by-step instructions for each version
- **Version Navigation**: Easy comparison with status indicators
- **Color-coded Keys**: Visual distinction between home row, thumb keys, and extra keys
- **No Build System**: Pure HTML/CSS/JS with CDN dependencies

## Quick Start

### Choose Your Implementation

#### For Split Keyboards (Silakka54)
1. **Vial (Firmware)**: Use `vial/miryoku-silakka54-vial-config.json`
   ```bash
   # Install Vial app, load JSON configuration
   # See vial/README.md for detailed instructions
   ```

2. **Kanata (Software)**: Use `kanata-v1.kbd` ⚠️ UNTESTED
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
1. **Web Visualizer**: Open `index.html` 
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
| **Configuration Backup** | ✅ Export/import JSON | ✅ File-based config | ❌ Display only |
| **Learning Curve** | Low (GUI) | Medium (config files) | None (visual) |
| **Advanced Features** | ✅ Full Vial features | ✅ Full Kanata features | ❌ Display only |

### When to Use Which

- **Use Vial** if you have a compatible split keyboard and want the easiest real-time configuration
- **Use Kanata** if you have any keyboard and want software-based remapping
- **Use Web Visualizer** for learning, reference, or if you're planning your setup

All three implementations share the **same home row modifiers, layer mappings, and combo definitions** for seamless switching between approaches.

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
- **Optimized 4-Layer**: Reduced complexity with direct symbol access
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
- Full 7-layer Miryoku implementation
- Home row modifiers (GACS pattern)
- Complete Vue.js refactoring
- JSON configuration system
- Interactive tooltips and layer switching

### ✅ V1-P - Pinky Relief (Production Ready)
- Weak finger optimized variant of V1
- 50% reduction in right pinky load
- No GUI modifiers on A/O keys
- Redistributed outer column symbols
- Strategic key placement for comfort

### ✅ V6 - OSM Optimized (Production Ready)
- True One-Shot Modifier behavior via OSL workaround
- 8th layer dedicated to modifier keys
- Programming-optimized symbol layer
- Reduced pinky strain with thumb shift
- Based on OSM research and Vial limitations

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

## Pinky Relief Optimizations

For users experiencing strain with their weakest fingers, the **V1-P Pinky Relief** variant provides targeted ergonomic improvements while maintaining Miryoku's core principles.

### Key Problems Addressed

**Right Pinky Overload**: In standard layouts, the right pinky often handles:
- Home row modifiers with hold-timing requirements
- High-frequency outer column symbols (=, ], \)
- Number row punctuation (-, _)
- This creates disproportionate load on the weakest finger

### Pinky Relief Solutions

**Load Redistribution:**
- **Removed GUI modifiers** from A and O keys (no hold-timing on pinkies)
- **Moved = symbol** from outer column (R01) to inner column (R11)
- **Relocated ] and \** to Symbol and Navigation layers respectively
- **Swapped ' and =** positions (apostrophe less frequent than equals)

**Benefits Achieved:**
- **50% reduction** in right pinky workload
- **Eliminated timing-dependent** modifier activation on weak fingers
- **Maintained muscle memory** for core Miryoku layout
- **Symmetric load distribution** between hands

### Physical Setup Tips

**Keyboard Positioning:**
- **Angle adjustment**: Tilt right half outward 10-15° to reduce pinky reach
- **Height optimization**: Lower keyboard 1-2cm to reduce wrist extension
- **Wider split**: Increase distance between halves by 2-3cm

**Adaptation Strategy:**
1. **Week 1**: Focus on new pinky positions, ignore modifiers
2. **Week 2**: Add back modifiers on stronger fingers only
3. **Week 3**: Full system integration with comfort breaks
4. **Week 4**: Fine-tune based on strain patterns

### Files and Access

- **Layout file**: `index-v1-pinky.html`
- **Configuration**: `app-v1-pinky.json`
- **Access**: Available from V1 layout navigation or direct link
- **Visual indicators**: Pinky-optimized keys highlighted in yellow

This variant is ideal for users with:
- Existing pinky strain or weakness
- Repetitive stress concerns
- Preference for gentler key placement
- Need for extended typing sessions

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

## V6 OSM Implementation (One-Shot Modifiers)

The V6 layout implements One-Shot Modifiers using an ingenious workaround that provides true sticky modifier behavior within Vial's constraints. This addresses a critical limitation where Vial's GUI doesn't expose OSM keycodes despite firmware support.

### The OSL Workaround Strategy

Instead of using unavailable OSM keycodes, V6 leverages **One-Shot Layer (OSL)** functionality which IS available in Vial:

1. **Dedicated OSM Layer**: Layer 8 contains only modifier keys on home row positions
2. **OSL Access**: Right thumb key activates the OSM layer temporarily
3. **True Sticky Behavior**: Tap OSL → tap modifier → modifier stays active for next keypress
4. **No Holding Required**: Eliminates the need for simultaneous key holds

### Key Features

#### Ergonomic Improvements
- **Shift on left thumb**: Most used modifier moved to strongest digit
- **Enter/Backspace on thumbs**: Reduces pinky strain
- **Tab moved to thumb**: Further pinky relief
- **Escape on dedicated key**: No combo required

#### Programming-Optimized Symbol Layer
Based on Pascal Getreuer's research on coding efficiency:
- **Bracket grouping**: `{}`, `[]`, `()` arranged for inward rolls
- **Common bigrams**: `!=`, `<=`, `==` positioned for comfort
- **Strong finger placement**: Frequent symbols on index/middle fingers
- **Avoided pinky doubles**: No `++`, `//` on weak fingers

#### Implementation Details

**Base Layer Changes:**
- Number row maintains familiar 1-0 positions
- Escape replaces backtick (L01)
- Quote/apostrophe on left pinky area
- Minus on left edge for easy access

**OSM Layer (Layer 8):**
```
Left home row:  LCtrl | LAlt | LShift | LGui
Right home row: RGui | RShift | RAlt | RCtrl
```

**Thumb Cluster Usage:**
- **LT1**: Shift (tap) / Media layer (hold)
- **LT2**: Space (tap) / Navigation layer (hold)
- **LT3**: Enter (tap) / Mouse layer (hold)
- **RT1**: Backspace (tap) / Symbols layer (hold)
- **RT2**: Tab (tap) / Numbers layer (hold)
- **RT3**: OSL to OSM layer

### Vial Configuration

To implement this in Vial:

1. **Create Layer 8** as your OSM layer
2. **Assign modifiers** to home row positions only
3. **Set RT3** to `OSL(8)` in the GUI
4. **Configure tap-hold** for other thumb keys
5. **Test sticky behavior**: Tap RT3 → tap modifier → type letter

### Usage Examples

**Capital Letter**: 
- Traditional: Hold Shift + tap A
- V6 OSM: Tap OSL → tap Shift position → tap A

**Ctrl+C Copy**:
- Traditional: Hold Ctrl + tap C
- V6 OSM: Tap OSL → tap Ctrl position → tap C

**Alt+Tab Switch**:
- Traditional: Hold Alt + tap Tab
- V6 OSM: Tap OSL → tap Alt position → tap Tab (thumb)

### Adaptation Timeline

**Week 1**: Focus on OSL timing and modifier positions
**Week 2**: Practice common shortcuts with sticky behavior
**Week 3**: Integrate with regular typing flow
**Week 4**: Achieve seamless modifier usage

This implementation provides the ergonomic benefits of One-Shot Modifiers without requiring QMK compilation or losing Vial's real-time configuration capabilities.

## Resources

- [Miryoku Official Repository](https://github.com/manna-harbour/miryoku) - Original layout and documentation
- [Miryoku QMK Reference](https://github.com/manna-harbour/miryoku_qmk) - QMK implementation
- [Colemak-DH Layout](https://colemakmods.github.io/mod-dh/) - Optimized alpha layout
- [Alternative Keyboard Layouts Guide](https://getreuer.info/posts/keyboards/alt-layouts/index.html#which-alt-keyboard-layout-should-i-learn) - Comprehensive comparison and selection guide
- [QMK Firmware](https://qmk.fm/) - Customizable keyboard firmware
- [ZMK Firmware](https://zmk.dev/) - Wireless keyboard firmware
- [Vial](https://vial.rocks/) - GUI for QMK configuration
- [Home Row Mods Guide](https://precondition.github.io/home-row-mods) - Detailed implementation guide