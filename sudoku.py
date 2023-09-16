import argparse
from display import draw_grid
from utils import text_to_grid, get_moves, load_grid

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", default="words.txt",
                        help="Path to file containing unsolved sudoku puzzle")
    parser.add_argument("-u", "--unsolved", action="store_true",
                        help="Display the unsolved grid")
    parser.add_argument("-s", "--solved", action="store_true",
                        help="Display the solved grid")

    args = parser.parse_args()
    return args

def solve(grid):

    solved = False
    last_moves = -1

    while not solved:
        moves = get_moves(grid)
        if moves == last_moves:
            print("Can't solve")
            break
        else:
            last_moves = moves

        if len(moves) == 0:
            solved = True

        for pos, vals in moves.items():
            if len(vals) == 1:
                value = vals.pop()
                grid[pos] = value

    return grid

def main():
    args = get_arguments()
    grid = load_grid(args.file)

    if args.unsolved:
        print(draw_grid(grid))

    grid = solve(grid)

    if args.solved:
        print(draw_grid(grid))

main()