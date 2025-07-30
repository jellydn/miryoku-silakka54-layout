# Kanata Layout Implementation

⚠️ **WARNING: UNTESTED/WORK IN PROGRESS** ⚠️

> **Note**: These Kanata configurations have been created based on the tested Vial configuration but have NOT been tested on actual hardware. They may require adjustments to work correctly. Please report any issues you encounter.

This document provides guidance for implementing the Miryoku layout using [Kanata](https://github.com/jtroo/kanata) keyboard remapping software on **both split keyboards and standard keyboards**.

## Overview

Kanata is a cross-platform keyboard remapping tool that allows for advanced key behavior customization, including:
- Home row modifiers with tap-hold functionality
- Layer switching and activation  
- Chord combinations for virtual key expansion
- Advanced key timing logic to prevent accidental modifier activation

We provide **two configurations**:
- **`kanata-v1.kbd`**: Optimized for **Silakka54 split keyboards** (54 keys)
- **`kanata-standard-keyboards.kbd`**: Adapted for **standard keyboards** (MacBook, Keychron K7, etc.)

Both implement the **V1 Traditional HRM** layout with all 7 layers and home row modifiers following the GACS pattern.

## Features

### Home Row Modifiers (GACS Pattern)
- **Left hand**: A(GUI via tap-dance), R(Alt), S(Ctrl), T(Shift)
- **Right hand**: N(Shift), E(Ctrl), I(Alt), O(GUI via tap-dance)
- **Smart timing**: Uses `key-timing` logic with 220ms threshold to prevent accidental activation during fast typing
- **Vial-aligned timing**: 175ms base tap-hold-release, 190ms for A, 200ms for O (matching Vial configuration)
- **Tap-dance for GUI keys**: A and O use tap-dance behavior exactly like the Vial setup

### Layer System
1. **Base Layer**: Colemak-DH layout with home row modifiers
2. **Media Layer**: Volume controls, media playback, system functions
3. **Navigation Layer**: Arrow keys, clipboard operations, page navigation
4. **Mouse Layer**: Mouse movement, clicks, and wheel controls
5. **Symbols Layer**: Programming symbols and special characters
6. **Numbers Layer**: Numpad layout with shifted number access
7. **Function Layer**: F1-F12 keys and system functions

### Chord Combinations (Vial-Aligned)
Implements chord combinations matching your Vial configuration:
- **Q + W**: Escape
- **Q + W + F**: Cmd+Q (quit application)
- **L + U**: Escape 
- **W + F**: GUI modifier (Super/Cmd key)
- **U + Y**: Quote character (')
- **X + C**: Cmd+X (cut)
- **C + D**: Cmd+C (copy)
- **, + .**: MEH modifier (Alt+Ctrl+Shift+GUI)

### Thumb Key Layer Access
- **Left thumb**: Esc(Media), Space(Nav), Tab(Mouse)
- **Right thumb**: Enter(Sym), Backspace(Num), Delete(Fun)

## Choosing Your Configuration

### For Split Keyboards (Silakka54, Corne, etc.)
Use **`kanata-v1.kbd`** if you have:
- Silakka54 split keyboard
- Similar 54-key split keyboards
- Custom split keyboards with thumb clusters

### For Standard Keyboards  
Use **`kanata-standard-keyboards.kbd`** if you have:
- **MacBook keyboards** (built-in or external)
- **Keychron K7** (65%, 75%, TKL layouts) 
- **Most standard QWERTY keyboards**
- **Gaming keyboards** with standard layouts

## Installation and Setup

### Prerequisites
1. **Install Kanata**: Download from [GitHub releases](https://github.com/jtroo/kanata/releases)
2. **Platform-specific setup**:
   - **Windows**: Run as administrator, may need to disable Windows Defender real-time protection temporarily
   - **Linux**: May need to add user to `input` group and configure udev rules
   - **macOS**: Requires input monitoring permissions in System Preferences

### Configuration Steps

#### For Split Keyboards (Silakka54)
1. **Copy the configuration file**:
   ```bash
   cp kanata-v1.kbd ~/.config/kanata/config.kbd
   ```

2. **Start Kanata**:
   ```bash
   # Linux/macOS
   sudo kanata --cfg ~/.config/kanata/config.kbd
   
   # Windows (as administrator)
   kanata.exe --cfg config.kbd
   ```

#### For Standard Keyboards (MacBook/Keychron K7)
1. **Copy the standard keyboard configuration**:
   ```bash
   cp kanata-standard-keyboards.kbd ~/.config/kanata/config.kbd
   ```

2. **Start Kanata**:
   ```bash
   # Linux/macOS  
   sudo kanata --cfg ~/.config/kanata/config.kbd
   
   # Windows (as administrator)
   kanata.exe --cfg config.kbd
   ```

### Testing Your Setup

3. **Test the layout**:
   - Verify base layer typing works correctly
   - Test home row modifiers with tap and hold actions
   - Confirm layer switching works with your keyboard's keys
   - Validate chord combinations

## Key Differences Between Configurations

### Split Keyboard Configuration (`kanata-v1.kbd`)
- **Dedicated thumb cluster**: Uses actual thumb keys for layer switching
- **54-key layout**: Optimized for minimal key count
- **Thumb key access**: Esc(Media), Space(Nav), Tab(Mouse), Enter(Sym), Backspace(Num), Delete(Fun)
- **Combos**: Q+W, L+U, X+C, H+, combinations
- **Pure Miryoku**: Closest to original Miryoku design philosophy

### Standard Keyboard Configuration (`kanata-standard-keyboards.kbd`)
- **Repurposed existing keys**: Uses Caps Lock, Right Shift, etc. for layer access
- **More keys available**: Includes function row, arrow keys, full layout
- **Layer access adaptations**:
  - **Caps Lock** → Escape/Media layer
  - **Space** → Space/Navigation layer (hold for nav)
  - **Tab** → Tab/Mouse layer (hold for mouse)  
  - **Enter** → Enter/Symbols layer (hold for symbols)
  - **Backspace** → Backspace/Numbers layer (hold for numbers)
  - **Right Shift** → Function layer access
- **Modified combos**: Adapted for QWERTY positions (Q+W, U+I, X+C, C+V)
- **Compatibility**: Works with existing function keys and arrow keys

### Home Row Modifiers (Both Configurations)
Both use the same GACS pattern:
- **A key**: Tap-dance A/GUI (190ms timing)
- **S/R key**: Alt modifier (175ms)
- **D/S key**: Control modifier (175ms)  
- **F/T key**: Shift modifier (175ms)
- **J/N key**: Shift modifier (175ms)
- **K/E key**: Control modifier (175ms)
- **L/I key**: Alt modifier (175ms)
- **;/O key**: Tap-dance ;/GUI (200ms timing)

## Quick Start Guide

### For MacBook Users
1. **Download**: `kanata-standard-keyboards.kbd`
2. **Key changes you'll notice**:
   - **Caps Lock** becomes Escape (tap) or Media layer (hold)
   - **Home row keys** (A, S, D, F, J, K, L, ;) become modifiers when held
   - **Space, Tab, Enter, Backspace** access different layers when held
   - **All function keys and arrow keys work normally**
3. **Most useful combos**:
   - **Q+W** = Escape (easier than reaching top-left)
   - **X+C** = Cut, **C+V** = Copy (faster than Cmd shortcuts)
   - **,+.** = MEH modifier for advanced shortcuts

### For Keychron K7 Users  
1. **Download**: `kanata-standard-keyboards.kbd`
2. **Switch your K7 to Mac mode** (Fn+K+C for 3 seconds)
3. **Key adaptations**:
   - **Your existing layout works** - this adds functionality on top
   - **Home row modifiers** replace need for pinky reaching
   - **Caps Lock** → Media controls when held
   - **Right Shift** → Function layer (F1-F12 on left hand)
4. **Gaming mode**: Temporarily disable Kanata when gaming to avoid conflicts

### For Split Keyboard Users (Silakka54)
1. **Download**: `kanata-v1.kbd` 
2. **Pure Miryoku experience**:
   - **Thumb clusters** handle all layer switching
   - **54 keys only** - no extra keys to distract
   - **Optimized combos** for split layout
   - **True Miryoku philosophy** - minimal keys, maximum efficiency

## Customization Guide

### Adjusting Timing Settings

The configuration includes timing parameters that can be tuned to your typing style:

```lisp
;; Key timing threshold (currently 250ms)
((key-timing 3 less-than 250)) $char break

;; Tap-hold-release timeout (200ms tap, 500ms hold)
(tap-hold-release-timeout 200 500 $char $mod $char)
```

**Recommended adjustments**:
- **Fast typists**: Reduce timing to 200-220ms
- **Slower typists**: Increase timing to 280-300ms
- **Chord sensitivity**: Adjust chord timeout (currently 50ms)

### Modifying Key Mappings

To customize key positions, edit the `(deflayer base)` section:

```lisp
(deflayer base
  grv  1    2    3    4    5    6    7    8    9    0    -
  tab  q    w    f    p    b    j    l    u    y    '    =
  [    @a_gui @r_alt @s_ctl @t_sft g    m    @n_sft @e_ctl @i_alt @o_gui ]
  ;    z    x    c    d    v    k    h    ,    .    /    \
              @esc_media @spc_nav @tab_mouse @del_fun @bsp_num @ent_sym
)
```

### Adding Custom Layers

To add a new layer (e.g., gaming layer):

1. **Define the layer**:
   ```lisp
   (deflayer gaming
     _    _    _    _    _    _    _    _    _    _    _    _
     tab  q    w    e    r    t    y    u    i    o    p    _
     caps a    s    d    f    g    h    j    k    l    ;    _
     lsft z    x    c    v    b    n    m    ,    .    /    _
                 spc  _    _    _    _    _
   )
   ```

2. **Add layer toggle**:
   ```lisp
   (defalias
     gaming_toggle (layer-toggle gaming)
   )
   ```

3. **Assign to a key**: Replace any key with `@gaming_toggle`

## Layer-Specific Usage

### Navigation Layer (Hold Space)
- **Arrow cluster**: H, J, K, L → ←, ↓, ↑, →
- **Clipboard**: Z, X, C, V → Undo, Cut, Copy, Paste
- **Page navigation**: Home, Page Down, Page Up, End
- **System**: Caps Lock, Insert, Delete

### Symbols Layer (Hold Enter)
- **Top row**: {, &, *, (, } for programming
- **Home row**: :, $, %, ^, + for operators
- **Bottom row**: ~, !, @, #, | for special chars
- **Thumb cluster**: (, ), _ for quick access

### Numbers Layer (Hold Backspace)
- **Numpad layout**: 7, 8, 9 on top row
- **Arithmetic**: +, -, *, / in logical positions
- **Brackets**: [, ] for arrays and indexing
- **Symbols**: ;, =, `, \ with shifted variants

## Troubleshooting

### Common Issues

#### Home Row Modifiers Not Working
- **Check timing**: Ensure you're holding keys long enough (>250ms)
- **Verify syntax**: Confirm `@a_gui` aliases are defined correctly
- **Test isolation**: Try simpler tap-hold without timing logic

#### Accidental Modifier Activation
- **Increase timing threshold**: Change from 250ms to 300ms
- **Check typing speed**: Fast typing may trigger timing logic incorrectly
- **Adjust chord timing**: Reduce chord timeout if conflicts occur

#### Layer Switching Problems
- **Confirm thumb key mappings**: Verify `@spc_nav` aliases work
- **Test individual layers**: Comment out other layers to isolate issues
- **Check key conflicts**: Ensure no duplicate key assignments

#### Performance Issues
- **Reduce complexity**: Comment out unused chord definitions
- **Optimize timing**: Higher thresholds = less processing overhead
- **Check system resources**: Kanata should use minimal CPU

### Debug Mode

Enable debug output to troubleshoot:

```bash
# Add to start of config file
(defcfg
  process-unmapped-keys no
  log-layer-changes yes
)

# Run with verbose output
kanata --cfg config.kbd --log debug
```

## Advanced Features

### Conditional Layers
Create context-sensitive layers that activate based on application:

```lisp
(defvar
  current-app chrome
)

(deflayer chrome-specific
  ;; Chrome-specific shortcuts
  _    _    _    _    _    _    _    _    _    _    _    _
  _    _    _    _    _    _    _    _    _    _    _    _
  _    _    _    _    _    _    _    _    _    _    _    _
  _    _    _    _    _    _    _    _    _    _    _    _
              _    _    _    _    _    _
)
```

### Macro Integration
Define complex macros for common workflows:

```lisp
(defalias
  email_sig (macro
    "Best regards," ret
    "Your Name" ret
    "your.email@company.com"
  )
)
```

### One-Shot Modifiers
For single-use modifiers without holding:

```lisp
(defalias
  osm_ctrl (one-shot 500 lctl)
  osm_shift (one-shot 500 lsft)
)
```

## Performance Optimization

### Reducing Latency
- **Minimize complex logic**: Use simple tap-hold where possible
- **Optimize chord definitions**: Remove unused combinations
- **Profile timing**: Use shortest safe timing values

### System Integration
- **Startup automation**: Add Kanata to system startup
- **Profile switching**: Create different configs for different contexts
- **Backup configuration**: Version control your `.kbd` files

## Migration from Other Tools

### From QMK/Vial
- **Timing translation**: QMK's `TAPPING_TERM` ≈ Kanata's tap-hold timeout
- **Layer mapping**: Direct 1:1 layer correspondence
- **Modifier keys**: Same GACS pattern, different syntax

### From Karabiner-Elements (macOS)
- **Complex modifications**: Convert to Kanata aliases
- **Application-specific**: Use conditional layers
- **Device targeting**: Kanata uses device filtering

### From AutoHotkey (Windows)
- **Hotkey conversion**: Map to Kanata aliases
- **Script logic**: Use defvar and conditional expressions
- **System integration**: Similar startup and permissions model

## Community and Support

- **GitHub Issues**: [Kanata Issues](https://github.com/jtroo/kanata/issues)
- **Discord**: Kanata community server
- **Documentation**: [Kanata Configuration Guide](https://github.com/jtroo/kanata/blob/main/docs/config.adoc)
- **Examples**: [Community configurations](https://github.com/jtroo/kanata/tree/main/cfg_samples)

## Contributing Improvements

To contribute improvements to this configuration:

1. **Test thoroughly**: Validate on multiple platforms
2. **Document changes**: Update this file with modifications
3. **Follow conventions**: Maintain existing naming patterns
4. **Performance**: Ensure changes don't impact responsiveness
5. **Compatibility**: Test with different Kanata versions

The goal is to provide a robust, well-documented implementation that serves as both a functional layout and a learning resource for the community.