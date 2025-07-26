# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Miryoku keyboard layout adaptation project for the Silakka54 split keyboard. It provides educational documentation and an interactive web visualizer for understanding and implementing the Miryoku layout system on a 54-key keyboard.

## Technology Stack

- HTML5 with Vue.js framework
- Tailwind CSS (loaded via CDN)
- JSON-based configuration system
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

- `index.html` - Interactive keyboard layout visualizer (V1 Traditional HRM)
- `index-v1-pinky.html` - V1 Pinky Relief variant
- `index-v2.html`, `index-v3.html`, `index-v4.html`, `index-v5.html` - Additional layout versions (WIP)
- `app.json`, `app-v1-pinky.json`, `app-v2.json`, `app-v3.json`, `app-v4.json`, `app-v5.json` - JSON configuration files for each version
- `Keyboard layout.md` - Comprehensive Miryoku adaptation guide and principles
- `README.md` - Project documentation and setup instructions
- `miryoku-layers/` - Reference layer images and JSON files from official Miryoku

## Key Architecture

The visualizer implements a 7-layer keyboard system following Miryoku principles (layer ordering intentionally differs from upstream Miryoku for Silakka54 ergonomics):
1. **Base layer** - Colemak-DH layout
2. **Media layer** - Volume, playback controls
3. **Navigation layer** - Arrow keys, page navigation
4. **Mouse layer** - Mouse movement and clicks
5. **Symbols layer** - Special characters and punctuation
6. **Numbers layer** - Numeric keypad layout
7. **Function layer** - F-keys and system functions

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