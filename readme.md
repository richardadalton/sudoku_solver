# Sudoku Solver

## Overview
Takes a string representation of an unsolved sudoku grid, and solves it.

## Implementation
The simple python implementation (sudoku.py) repeatedly iterates over the boards attempting to find squares that can only have one possible value based on the rules of Sudoku. Each time it updates the board with a value, it iterates again.

There is an unfinished alternative solution that uses recursion (sudoku_recursive.py)

## Installation

Just clone this repository

```bash
$ git clone https://github.com/richardadalton/sudoku_solver.git
```

## Running Sudoku Solver

```bash
$ python sudoku.py [-h] [-f FILE] [-u] [-s]

arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Path to file containing unsolved sudoku puzzle
  -u, --unsolved        Display the unsolved grid
  -s, --solved          Display the solved grid
```

## Puzzle File Format
Unsolved puzzles can be represented as text files using the following format.
White space is ignored so text can be arranged to match a grid layout.
Blank squares are represented by dots ('.').

```text
..3 .2. 6..
9.. 3.5 ..1
..1 8.6 4..

..8 1.2 9..
7.. ... ..8
..6 7.8 2..

..2 6.9 5..
8.. 2.3 ..9
..5 .1. 3..
```
