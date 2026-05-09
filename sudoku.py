import argparse
from display import draw_grid
from utils import load_grid, possible_values


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", default="sudoku.txt",
                        help="Path to file containing unsolved sudoku puzzle")
    parser.add_argument("-u", "--unsolved", action="store_true",
                        help="Display the unsolved grid")
    parser.add_argument("-s", "--solved", action="store_true",
                        help="Display the solved grid")
    return parser.parse_args()


def _propagate(grid):
    """Fill in any cell that has exactly one possible value, repeatedly."""
    changed = True
    while changed:
        changed = False
        for pos in grid:
            if grid[pos] == ".":
                vals = possible_values(grid, pos)
                if len(vals) == 1:
                    grid[pos] = vals.pop()
                    changed = True
    return grid


def _backtrack(grid):
    """Pick the most constrained empty cell and try each candidate."""
    best_pos, best_vals = None, None
    for pos in grid:
        if grid[pos] == ".":
            vals = possible_values(grid, pos)
            if len(vals) == 0:
                return None  # contradiction
            if best_vals is None or len(vals) < len(best_vals):
                best_pos, best_vals = pos, vals

    if best_pos is None:
        return grid  # all cells filled

    for val in best_vals:
        candidate = _propagate({**grid, best_pos: val})
        result = _backtrack(candidate)
        if result is not None:
            return result

    return None


def solve(grid):
    grid = _propagate(dict(grid))
    if any(v == "." for v in grid.values()):
        result = _backtrack(grid)
        if result is not None:
            return result
    return grid


def main():
    args = get_arguments()
    grid = load_grid(args.file)

    if args.unsolved:
        print(draw_grid(grid))

    grid = solve(grid)

    if any(v == "." for v in grid.values()):
        print("Can't solve")

    if args.solved:
        print(draw_grid(grid))


if __name__ == "__main__":
    main()