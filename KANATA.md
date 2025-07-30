# Kanata Layout Implementation

This document provides guidance for implementing the Miryoku Silakka54 layout using the [Kanata](https://github.com/jtroo/kanata) keyboard remapping software.

## Overview

Kanata is a cross-platform keyboard remapping tool that allows for advanced key behavior customization, including:
- Home row modifiers with tap-hold functionality
- Layer switching and activation
- Chord combinations for virtual key expansion
- Advanced key timing logic to prevent accidental modifier activation

The `kanata-v1.kbd` file implements the **V1 Traditional HRM** layout with all 7 layers and home row modifiers following the GACS pattern.

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

## Installation and Setup

### Prerequisites
1. **Install Kanata**: Download from [GitHub releases](https://github.com/jtroo/kanata/releases)
2. **Platform-specific setup**:
   - **Windows**: Run as administrator, may need to disable Windows Defender real-time protection temporarily
   - **Linux**: May need to add user to `input` group and configure udev rules
   - **macOS**: Requires input monitoring permissions in System Preferences

### Configuration Steps

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

3. **Test the layout**:
   - Verify base layer typing works correctly
   - Test home row modifiers with tap and hold actions
   - Confirm layer switching with thumb keys
   - Validate chord combinations

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