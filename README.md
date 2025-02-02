# Battleship Game

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Java](https://img.shields.io/badge/Java-11%2B-orange)

![Battleship](cat-battleship.jpeg)

## Overview
Battleship is a classic strategy game where players try to sink each other's fleet of ships. This repository contains two implementations of Battleship:
- **Version 1: Python**: A simple terminal-based version designed for an *Introduction to Computer Programming* course.
- **Version 2: Java**: A graphical implementation using the `DrawingPanel` for an *Algorithms in Programming* course.

## Features:
### Python Version
- Terminal-based user interface.
- Ability to start a new game or load a saved game.
- Ship placement and turn-based attacks.
- Save and load functionality using `pickle`.

### Java Version
- Graphical user interface using `DrawingPanel`.
- Two-player turn-based gameplay.
- Recursive game loop to handle player turns.
- Ship placement with validation.
- Hit and miss indicators on the game board.

## Installation & Usage
### Clone the Repository
To get started, clone the repository and navigate to the relevant directory:
```sh
git clone https://github.com/CeliePierre/Battleship.git
```

#### Version 1: Python:
1. Ensure you have Python 3.8 or later installed.
2. Change directory.
    ```sh
    cd v1
    ```
3. Run the BattleShip program.
    ```sh
    python BattleShip.py
    ```

#### Version 2: Java:
1. Ensure you have Java 11 or later installed.
2. Change directory.
    ```sh
    cd v2
    ```
3. Compile and run the BattleShip program.
    ```sh
    javac Battleship2.java
    java Battleship2
    ```

## License
This project is for educational purposes and does not require a license.
