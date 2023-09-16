from display import draw_grid
from utils import text_to_grid, get_moves

# start = "746931258 923584.1. .1.....93   .89.1...6 ....47... 675...1.2   ..1.72... .5..6.8.4 26.8.3..."
start = "..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3.."
# start = "9.....1..64..9...51.7...43....3.5....79..6.8..6.1...23..28.3...8....7.16...5.2.4."
# start = "................................................................................."

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

        print("Moves", len(moves))
        if len(moves) == 0:
            solved = True

        for pos, vals in moves.items():
            if len(vals) == 1:
                value = vals.pop()
                grid[pos] = value

    return grid

def main():
    grid = text_to_grid(start)
    print(draw_grid(grid))
    grid = solve(grid)
    print(draw_grid(grid))

main()