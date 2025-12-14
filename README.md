# Chess (Pygame)
Chess (Pygame) is a compact drag-and-drop chess sandbox built with Python and Pygame. It supports pseudo-legal move generation, turn tracking, last-move highlighting, hint dots for available destinations, optional move and capture sounds, and theme-driven colors for fast asset swaps. Assets live under `assets/images/imgs-80px/` (or `imgs-128px/`) and are named `{color}_{piece}.png` (for example, `white_pawn.png`). Sounds are optional (`assets/sounds/move.wav`, `assets/sounds/capture.wav`).

## Structure
- `main.py` — game entry and event loop
- `src/board.py` — board state and move generation
- `src/piece.py` — piece model and sprite loading
- `src/move.py`, `src/square.py` — move and square helpers
- `src/dragger.py` — drag-and-drop handling
- `src/game.py` — rendering, turns, sounds
- `src/const.py`, `src/color.py`, `src/theme.py`, `src/config.py` — sizes, colors, theme, config
- `src/sound.py` — optional sounds

## Run
Python 3.9+ and `pygame` are required.

```bash
pip install pygame
python main.py
```

Controls: drag a piece to move; press `R` to reset; close the window to quit. If assets are missing, pieces fall back to simple shapes and sounds are skipped. Move rules are simplified—extend them to add check, mate, castling, and en passant.
