# pygame-of-life

A simple implementation of Conway’s Game of Life written in Pygame.  Allows for choice of ruleset and has controls to pause, clear, and randomly populate the game board, as well as the ability to directly draw on the map to either add or remove cells.

## Controls
Mouse: draw on the game board, flipping the state of cells that are drawn over.  Best used when the game is paused, though it does work even when the game is running.

Space: Play/pause.

Enter: Randomly populate the center region of the game board.

Backspace: Clear the game board.

## Quick Start

 - Clone this repo
 - Install `Python3`, `numpy`, and `Pygame`:

   ```
   sudo apt-get update
   sudo apt install python3
   sudo apt install python3-pip
   python3 -m pip install -U pygame --user
   python3 -m pip install -U numpy --user
   ```
 - Start the game with `python3 conway.py`
