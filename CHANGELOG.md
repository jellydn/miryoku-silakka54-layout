# Changelog

All notable changes to the Miryoku Silakka54 Layout project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **Corne (Enthium v13) Layout** (index-corne-enthium.html): Latest Enthium v13 implementation for 3x6+3 split keyboards
  - **PWF/; layout**: Clockwise rotation of PWF and swap of /; compared to Enthium v12
  - **Improved ergonomics**: 52.5% reduction in long-distance row jumps, 30% reduction in right pinky SFBs
  - **6 complete layers**: Base (Enthium), Navigation, Mouse, Symbols, Numbers, Function
  - **7 combo keys**: Q, Z, V, Hyper, Meh, Escape, Enter for efficiency
  - **Optimized thumb cluster**: Backspace/Sym → R/Num → Empty (left to right)
  - **Performance metrics**: 0.55% SFBs, 0.07% LSBs, 45.82% rolls, 2.91% pinky off
  - **Enhanced tooltips**: Comprehensive explanations for Enthium-specific features
  - **Vial configuration**: Complete .vil file for easy firmware flashing
- **Updated Documentation**: README.md now includes Enthium v13 alongside other Corne layouts
- **Resource Links**: Added Enthium project and v13 release references

### Changed
- **Layout Ecosystem**: Now 9 complete layout options including latest Enthium v13
- **Corne Layout Options**: 3 complete Corne variants (Colemak-DH, Gallium, Enthium v13)

## [1.4.0] - 2025-01-24

### Added
- **Coding-Optimized Layout (V5)** (index-v5.html): Programming-focused enhancement of V4
  - **Direct bracket access**: [], {} on base layer without layer switching
  - **Immediate coding symbols**: =, +, -, * accessible without Shift
  - **IDE shortcuts layer**: Debugging (F5, F9, F10, F11), refactoring, navigation
  - **Code manipulation**: Line duplication (Ctrl+D), moving (Alt+↑/↓), commenting (Ctrl+/)
  - **String handling**: Direct access to quotes, escape characters, regex symbols
  - **Advanced tooltips**: Context-aware explanations for coding workflows
  - **Emerald color theme**: Easy identification as coding-focused variant
- **Enhanced Navigation**: All 5 layout versions now accessible from any page
- **Programming Workflow Integration**: Common IDE shortcuts and debugging keys

### Changed
- **Improved Layout Ecosystem**: Now 5 complete layout options for different needs
- **Better Developer Experience**: Specialized layout for programming workflows
- **Enhanced Documentation**: README reflects all 5 layout options

## [1.3.0] - 2025-01-24

### Added
- **4-Layer Balanced Layout** (index-v4.html): Perfect balance between simplicity and efficiency
  - Only 4 layers needed (vs 6 in traditional Miryoku)
  - Dedicated modifiers (no dual-function complexity)
  - Direct number row access for instant symbols
  - Combined Nav/Num layer for maximum efficiency
  - Comprehensive tooltip system with context-aware explanations
  - Amber color theme for easy identification
- **Enhanced Navigation**: Updated all versions to include 4-layer balanced option
- **Better Version Names**: Clearer naming across all layout versions
  - "Traditional HRM" instead of "Traditional 6-Layer"
  - "No HRM Dedicated" instead of "No HRM Version"
  - Consistent terminology for easier comparison

### Changed
- **Improved Layout Comparison**: All 4 versions now easily accessible from any page
- **Enhanced User Experience**: Clearer differentiation between layout approaches
- **Updated Documentation**: README reflects all 4 layout options with proper descriptions

## [1.2.0] - 2025-01-24

### Added
- **Interactive Tooltips System**: Comprehensive hover tooltips for all key functions
  - Traditional Version: Explains home row modifiers and dual-function keys
  - Optimized Version: Highlights direct symbol access and combined layers
  - No HRM Version: Shows dedicated modifier explanations and layer states
- **Enhanced Documentation**: Updated README with tooltip system details
- **Special State Explanations**: Tooltips for "---" states and layer inactive indicators
- **Context-Aware Tooltips**: Different explanations based on current layer

### Changed
- **Improved User Experience**: Keys now provide instant explanations on hover
- **Better Learning Curve**: Tooltips help users understand complex dual-function keys
- **Enhanced README**: Added interactive features section with detailed tooltip documentation

## [1.1.0] - 2025-01-24

### Added
- **No Home Row Modifiers Version** (index-v3.html): Alternative layout with dedicated modifier keys
  - Dedicated Shift, Ctrl, Alt, GUI keys on outer columns and thumb positions
  - Same 6-layer system without dual-function complexity
  - Easier learning curve for traditional keyboard users
- **Comprehensive Layer Switching Guides**: Detailed instructions for each version
  - Physical keyboard usage explanations
  - Visualizer interaction guides
  - Version-specific benefits and use cases
- **Three-Way Navigation**: Easy switching between all layout versions
- **Enhanced Legends**: Improved explanations and color coding for each version
- **Consistent Modern Styling**: Applied 3.5rem key sizes and improved typography across all versions

### Changed
- **Updated Navigation**: All versions now link to each other with clear labeling
- **Improved Color Themes**: Blue (traditional), Green (optimized), Purple (no-HRM)
- **Better Mobile Experience**: Responsive navigation with flex layout
- **Enhanced User Experience**: Clear version comparison and selection

## [1.0.0] - 2025-01-24

### Added
- **Initial Release**: Complete Miryoku Silakka54 layout visualization system
- **Traditional 6-Layer Layout** (index.html): Full Miryoku implementation
  - Home row modifiers with GACS pattern
  - 6 distinct layers: Base, Navigation, Symbols, Numbers, Function, Media
  - Colemak-DH alpha layout integration
- **Optimized 3-Layer Layout** (index-v2.html): Streamlined version
  - Reduced layer switching with direct symbol access
  - Combined Nav/Function layer for efficiency
  - 90% of coding tasks without layer switching
- **Interactive Visualizer**: 
  - Clickable layer buttons
  - Hover effects on keys
  - Color-coded key categories
  - Responsive design
- **Comprehensive Documentation**:
  - README.md with implementation guides
  - Keyboard layout.md with detailed Miryoku principles
  - CLAUDE.md for development guidance
- **Educational Content**:
  - Miryoku philosophy and core principles
  - Adaptation strategies for 54-key keyboards
  - Community research insights
  - Implementation timelines and expectations
- **GitHub Pages Deployment**: Live interactive demos
- **Multiple Export Formats**: QMK, Vial, and ZMK implementation guides

### Technical Features
- **Pure HTML/CSS/JavaScript**: No build system required
- **Tailwind CSS**: Modern styling with CDN integration
- **Responsive Design**: Works on desktop and mobile devices
- **Modular Architecture**: Easy to extend and customize
- **Git Version Control**: Full project history and collaboration

## Project Structure

```
miryoku-silakka54-layout/
├── index.html              # Traditional HRM layout (6 layers)
├── index-v2.html           # Optimized 3-layer layout  
├── index-v3.html           # No HRM dedicated layout (6 layers)
├── index-v4.html           # 4-layer balanced layout
├── index-v5.html           # Coding-optimized layout (4 layers)
├── README.md               # Project documentation
├── CHANGELOG.md            # This file
├── CLAUDE.md               # Development guidance
├── Keyboard layout.md      # Detailed Miryoku guide
├── v3-vs-v4-comparison.md  # Layout comparison guide
└── .git/                   # Version control
```

## Links

- **Live Demo**: https://jellydn.github.io/miryoku-silakka54-layout/
- **Repository**: https://github.com/jellydn/miryoku-silakka54-layout
- **Miryoku Official**: https://github.com/manna-harbour/miryoku

---

**Legend:**
- `Added` for new features
- `Changed` for changes in existing functionality  
- `Deprecated` for soon-to-be removed features
- `Removed` for now removed features
- `Fixed` for any bug fixes
- `Security` for vulnerability fixes