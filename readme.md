# Sudoku Solver

Solves sudoku puzzles using constraint propagation with backtracking. Available as both a CLI tool and a Flask web app.

## How it works

The solver first fills in any cell that has only one possible value (constraint propagation), then falls back to recursive backtracking with a minimum-remaining-values heuristic for harder puzzles that require guessing.

## Installation

```bash
git clone https://github.com/richardadalton/sudoku_solver.git
cd sudoku_solver
pip install -r requirements.txt
```

## CLI usage

```bash
python sudoku.py [-h] [-f FILE] [-u] [-s]

arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Path to puzzle file (default: sudoku.txt)
  -u, --unsolved        Display the unsolved grid
  -s, --solved          Display the solved grid
```

Example:

```bash
python sudoku.py -f sudoku.txt -u -s
```

## Web app

```bash
python app.py
```

Then open `http://127.0.0.1:5001` in your browser. Enter a puzzle and click **Solve**.

## Puzzle file format

White space and blank lines are ignored, so puzzles can be laid out as a grid.
Empty cells are represented by dots (`.`).

```
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
