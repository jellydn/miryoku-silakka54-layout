# Vial Configuration for Miryoku Silakka54

This folder contains the complete Vial configuration used as the reference implementation for this project. The configuration has been tested and optimized for ergonomic use with small hands and represents the baseline that both the Kanata software implementation and web visualizer are aligned with.

## Overview

**Vial** is a real-time GUI-based keyboard configuration tool that runs on QMK-compatible keyboards. Unlike QMK which requires compilation and flashing, Vial allows you to modify your keyboard layout instantly through a visual interface.

### Why Use Vial?

- ✅ **Real-time changes**: No compilation or flashing required
- ✅ **Visual interface**: Drag-and-drop key configuration
- ✅ **Advanced features**: Tap-dance, combos, macros, key overrides
- ✅ **Instant testing**: Changes apply immediately for testing
- ✅ **Easy backup**: Save/load complete configurations

## File Contents

- **`miryoku-silakka54-vial-config.json`**: Complete Vial configuration file
  - 7-layer Miryoku implementation  
  - Optimized home row modifiers with tap-dance
  - 8 combo combinations for enhanced productivity
  - Fine-tuned timing settings (175ms base, 190ms/200ms tap-dance)
  - All layer mappings and special functions

## Hardware Requirements

### Supported Keyboards
This configuration is designed for:
- **Silakka54** split keyboard
- **54-key layout** with proper Vial firmware support
- **Similar split keyboards** with compatible key layouts

### Firmware Requirements
Your keyboard must have:
- ✅ **Vial-compatible firmware** installed
- ✅ **QMK with Vial support** compiled for your specific keyboard
- ✅ **USB connection** to computer running Vial app

## Installation & Setup

### Step 1: Install Vial Application

#### macOS
```bash
# Download from GitHub releases
brew install --cask vial

# Or download directly from: https://github.com/vial-kb/vial-gui/releases
```

#### Windows
```bash
# Download .exe from GitHub releases
# https://github.com/vial-kb/vial-gui/releases
```

#### Linux
```bash
# Download AppImage from GitHub releases
# https://github.com/vial-kb/vial-gui/releases

# Make executable and run
chmod +x Vial-*.AppImage
./Vial-*.AppImage
```

### Step 2: Prepare Your Keyboard

1. **Flash Vial-compatible firmware** to your Silakka54:
   - Download appropriate Vial firmware for your keyboard
   - Use QMK Toolbox or similar flashing tool
   - Ensure firmware includes Vial support

2. **Connect keyboard** via USB to your computer

3. **Verify detection**: Keyboard should appear in Vial app when connected

### Step 3: Load Configuration

1. **Open Vial application**
2. **Connect your keyboard** - it should appear in the device list
3. **Load configuration**:
   - File → Load → Select `miryoku-silakka54-vial-config.json`
   - Or drag and drop the JSON file into Vial
4. **Apply configuration** - changes happen instantly

### Step 4: Test Your Setup

1. **Test basic typing** - verify Colemak-DH layout works
2. **Test home row modifiers**:
   - Hold A briefly → should activate GUI modifier
   - Hold R, S, T → should activate Alt, Ctrl, Shift respectively
   - Hold N, E, I → should activate Shift, Ctrl, Alt respectively  
   - Hold O briefly → should activate GUI modifier
3. **Test layer switching**:
   - Hold Escape (left thumb) → Media layer
   - Hold Space (left thumb) → Navigation layer
   - Hold Tab (left thumb) → Mouse layer
   - Hold Enter (right thumb) → Symbols layer
   - Hold Backspace (right thumb) → Numbers layer
   - Hold Delete (right thumb) → Function layer
4. **Test combos**:
   - Q+W → Escape
   - L+U → Escape
   - X+C → Cut (Cmd+X)
   - C+D → Copy (Cmd+C)
   - And others listed below

## Configuration Details

### Home Row Modifiers (GACS Pattern)
| Key | Tap | Hold | Timing |
|-----|-----|------|--------|
| A | A | GUI/Super | 190ms (tap-dance) |
| R | R | Alt | 175ms |
| S | S | Control | 175ms |
| T | T | Shift | 175ms |
| N | N | Shift | 175ms |
| E | E | Control | 175ms |
| I | I | Alt | 175ms |
| O | O | GUI/Super | 200ms (tap-dance) |

### Layer Access (Thumb Keys)
| Key | Tap | Hold (Layer) | Vial Code |
|-----|-----|-------------|-----------|
| Left Escape | Escape | Media (1) | LT1(KC_ESCAPE) |
| Left Space | Space | Navigation (2) | LT2(KC_SPACE) |
| Left Tab | Tab | Mouse (3) | LT3(KC_TAB) |
| Right Enter | Enter | Symbols (4) | LT4(KC_ENTER) |
| Right Backspace | Backspace | Numbers (5) | LT5(KC_BSPACE) |
| Right Delete | Delete | Function (6) | LT6(KC_DELETE) |

### Combo Combinations
| Keys | Result | Description |
|------|--------|-------------|
| Q + W | Escape | Easier than reaching top-left |
| Q + W + F | Cmd+Q | Quit application |
| L + U | Escape | Right-hand escape option |
| W + F | GUI modifier | Super/Cmd key |
| U + Y | Quote (') | Quick quote access |
| X + C | Cmd+X | Cut to clipboard |
| C + D | Cmd+C | Copy to clipboard |
| , + . | MEH | Alt+Ctrl+Shift+GUI |

### Vial Settings Applied
| Setting | Value | Purpose |
|---------|-------|---------|
| Tapping Term | 175ms | Base tap-hold timing |
| Combo Term | 50ms | Combo key timing |
| Tap Dance Term | 190ms (A), 200ms (O) | GUI key timing |
| Permissive Hold | Enabled | Easier modifier activation |
| Ignore Mod Tap Interrupt | Enabled | Prevents accidental mods |

## Customization Guide

### Modifying the Configuration

1. **In Vial app**:
   - Make changes directly in the GUI
   - Test immediately
   - Export when satisfied: File → Save

2. **Key remapping**:
   - Drag keys between positions
   - Change tap/hold behaviors
   - Modify layer assignments

3. **Timing adjustments**:
   - Settings → Tap-Hold Settings
   - Adjust based on your typing speed
   - Test thoroughly before saving

### Common Modifications

#### Adjust Home Row Modifier Timing
- **Faster typists**: Reduce tapping term to 160-170ms
- **Slower typists**: Increase tapping term to 180-200ms
- **Per-key timing**: Different values for different fingers

#### Add New Combos
1. Go to Combos tab in Vial
2. Click "Add Combo"
3. Select trigger keys and result
4. Set timing (typically 50ms)

#### Modify Layer Contents
1. Select layer from dropdown
2. Modify any key by clicking and selecting new function
3. Changes apply immediately

### Backup and Restore

#### Creating Backups
```bash
# In Vial app
File → Save → name-your-backup.json

# Store in safe location with descriptive names
miryoku-silakka54-base-config.json
miryoku-silakka54-gaming-variant.json
```

#### Restoring from Backup
```bash
# In Vial app  
File → Load → select-your-backup.json

# Or drag-and-drop JSON file into Vial
```

## Troubleshooting

### Keyboard Not Detected
1. **Check firmware**: Ensure Vial-compatible firmware is installed
2. **Try different USB port/cable**
3. **Restart Vial app**
4. **Check device permissions** (macOS/Linux may need input monitoring)

### Modifiers Not Working
1. **Check timing settings**: May need adjustment for your typing speed
2. **Verify key assignments**: Ensure keys are assigned to correct modifiers
3. **Test tap vs hold**: Practice deliberate tap/hold motions
4. **Check conflicts**: Ensure no system shortcuts interfere

### Combos Not Triggering
1. **Check combo timing**: Default 50ms may need adjustment
2. **Practice simultaneous press**: Keys must be pressed nearly simultaneously
3. **Verify combo setup**: Check trigger keys and results in Combos tab
4. **Test individual keys**: Ensure base keys work before combo testing

### Layer Switching Issues
1. **Check layer tap settings**: Verify LT assignments are correct
2. **Test hold duration**: May need longer hold for layer activation
3. **Verify layer contents**: Ensure layers have expected key mappings
4. **Check thumb key placement**: Ensure comfortable reach to layer keys

## Migration Between Systems

### From Vial to Kanata
Use the provided Kanata configurations which mirror this Vial setup:
- `kanata-v1.kbd` for split keyboards
- `kanata-standard-keyboards.kbd` for standard keyboards

### From Vial to QMK
Export Vial config and adapt to QMK C code:
1. Note all key assignments and timing settings
2. Implement in `keymap.c` with appropriate QMK functions
3. Compile and flash standard QMK firmware

### Sharing Configurations
- **JSON format**: Universal Vial format, works across devices
- **Include documentation**: Add notes about custom settings
- **Version compatibility**: Note Vial version used for configuration

## Support and Resources

- **Vial Documentation**: [https://get.vial.today/docs/](https://get.vial.today/docs/)
- **Vial GitHub**: [https://github.com/vial-kb/vial-gui](https://github.com/vial-kb/vial-gui)
- **QMK Documentation**: [https://docs.qmk.fm/](https://docs.qmk.fm/)
- **Miryoku Layout**: [https://github.com/manna-harbour/miryoku](https://github.com/manna-harbour/miryoku)

## Configuration Philosophy

This Vial configuration embodies several key principles:

1. **Ergonomic first**: Optimized for small hands and reduced strain
2. **Consistency**: Matches Kanata and web visualizer implementations
3. **Practical combos**: Only includes combos that provide real ergonomic benefit
4. **Conservative timing**: Settings balanced for accuracy over speed
5. **Layer orthogonality**: Each layer serves distinct, non-overlapping functions

The result is a practical, comfortable layout that serves as the foundation for both software-based alternatives and visual learning tools.