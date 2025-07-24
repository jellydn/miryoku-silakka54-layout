# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Miryoku keyboard layout adaptation project for the Silakka54 split keyboard. It provides educational documentation and an interactive web visualizer for understanding and implementing the Miryoku layout system on a 54-key keyboard.

## Technology Stack

- Pure HTML5 with vanilla JavaScript
- Tailwind CSS (loaded via CDN)
- Static website - no build system required

## Development Commands

```bash
# Serve locally with live reload
npx serve

# Alternative local server options
python -m http.server 8000
python3 -m http.server 8000
```

## File Structure

- `index.html` - Interactive keyboard layout visualizer with 6-layer switching
- `Keyboard layout.md` - Comprehensive Miryoku adaptation guide and principles
- `README.md` - Project documentation and setup instructions

## Key Architecture

The visualizer implements a 6-layer keyboard system following Miryoku principles:
1. **Base layer** - Colemak-DH layout
2. **Navigation layer** - Arrow keys, page navigation
3. **Symbols layer** - Special characters and punctuation
4. **Numbers layer** - Numeric keypad layout
5. **Function layer** - F-keys and system functions
6. **Media layer** - Volume, playback controls

## Layout Principles

- Home row modifiers (GACS pattern: GUI, Alt, Ctrl, Shift)
- 3×5+3 thumb key configuration
- Ergonomic thumb key usage for layer switching
- Color-coded key categories for visual clarity

## Making Changes

Since this is a static site:
1. Edit HTML/CSS/JS directly in files
2. Refresh browser to see changes
3. No compilation or build step needed
4. Use `npx serve` for live development server