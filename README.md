# Tic Tac Toe with AI using Pygame

This repository contains a Tic Tac Toe game implemented in Python using Pygame. It features a graphical interface, AI opponent, and sound effects. The AI uses the Alpha-Beta pruning algorithm for optimal moves.

---

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Code Overview](#code-overview)
5. [How It Works](#how-it-works)
6. [Future Improvements](#future-improvements)

---

## Features

- **Graphical Interface:** Draws the Tic Tac Toe grid and updates it interactively.
- **AI Opponent:** An AI opponent using the Alpha-Beta pruning algorithm.
- **Sound Effects:** Sounds for player and AI moves, along with game notifications.
- **Dynamic Score Tracking:** Keeps track of wins, losses, and draws.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/am94an/TicTacToe.git
   cd TikTakToe
   ```

2. Install required dependencies:
   ```bash
   pip install pygame
   ```

3. Ensure you have Python 3.x installed.

---

## Usage

1. Run the game:
   ```bash
   python tic_tac_toe.py
   ```

2. Follow the instructions on the screen.
   - Press any key to start.
   - Make moves by clicking on the grid.
   - Press 'R' to restart or 'Q' to quit after the game ends.

---

## Code Overview

### Main Classes and Functions

#### `TicTacToe`
- Manages the game state, board updates, and checks for winners.

#### `alpha_beta`
- Implements the Alpha-Beta pruning algorithm for optimal AI decisions.

#### `draw_*` functions
- Handle drawing the board, start screen, end screen, and score screen.

#### `play`
- The main game loop that handles events and alternates turns between the player and AI.

---

## How It Works

1. **Game Loop:**
   - The game alternates turns between the player (X) and AI (O).
   - The game ends when there is a winner or a draw.

2. **AI Logic:**
   - Uses Alpha-Beta pruning for efficient decision-making.
   - The AI prioritizes winning moves, blocking the player, and minimizing/maximizing scores.

3. **Pygame Interface:**
   - Draws the grid and game elements dynamically.
   - Handles mouse input for player moves.

4. **Sound Effects:**
   - Uses Pygame's mixer to play sound effects for moves and game notifications.

---

## Future Improvements

- **Multiplayer Mode:** Add support for two players.
- **Difficulty Levels:** Allow players to choose between Easy, Medium, and Hard AI.
- **Mobile Compatibility:** Develop a mobile-friendly version.
- **Enhanced Graphics:** Improve the visual appeal with animations and better designs.

---

## Contribution

Feel free to fork this repository, make changes, and create pull requests. Contributions are welcome!

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

- [Pygame Documentation](https://www.pygame.org/docs/)
- Inspiration from classic Tic Tac Toe games.
