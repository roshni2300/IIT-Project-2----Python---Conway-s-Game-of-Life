# Conway's Game of Life – Pygame Implementation
This is a Python-based simulation of Conway's Game of Life, a classic example of cellular automata. Each cell on a grid evolves over discrete time steps according to a few simple rules. The visualization is handled using Pygame, offering an interactive experience where users can build and observe patterns in real time.

# Overview
Conway's Game of Life is a zero-player game where the system evolves based on its initial state. This implementation includes a graphical interface, basic keyboard controls, and pattern save/load functionality, allowing users to experiment with various cell arrangements.

# Features
**Interactive Grid**: Click to toggle cells between alive and dead.

**Simulation Controls**:


Space: Start or pause the simulation

N: Advance the simulation by one generation

R: Populate the grid with a random distribution of live cells

S: Save the current state to a file

L: Load a saved pattern from a file

# Requirements
1. Python 3
2. pygame
   
   Install this way: pip install pygame

# Getting Started
1. Clone the repository

   git clone https://github.com/yourusername/conway-life.git
   cd conway-life

2. Run the simulation:

   python life.py  --width 40 --height 20 --fps 6

# Optional Arguments

--width: Number of columns in the grid (default: 40)

--height: Number of rows (default: 20)

--fps: Simulation speed in frames per second (default: 6)

# Game Rules
1. Each cell interacts with its eight neighboring cells based on the following rules:

2. Fewer than 2 live neighbors → Cell dies (underpopulation)

3. 2 or 3 live neighbors → Cell survives

4. More than 3 live neighbors → Cell dies (overcrowding)

5. Exactly 3 live neighbors → Dead cell becomes alive (reproduction)

# Saving and Loading Patterns
1. Press S to write the current pattern of live cells to a file named patterns.txt
2. Press L to load the pattern from the same file
3. The format used is a list of coordinate pairs for all living cells.

# Notes
This version focuses on a clean and interactive experience without additional performance or data visualization tools. Ideal for learning the fundamentals of cellular automata and Pygame-based development.



