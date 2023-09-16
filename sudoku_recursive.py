from display import draw_grid
from utils import get_moves

# start = "..693.25..23584.1..1.....93.89.1...6....47...675...1.2..1.72....5..6.8.426.8.3..."
# start = "..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3.."
start = "......... ......... ......... ......... ..1...... ......2.. ......... ......... ........."


def text_to_grid(str):
    grid = {}
    for r in range(9):
        for c in range(9):
            char = str[r * 9 + c]
            if char == '.':
                grid[(r, c)] = {1, 2, 3, 4, 5, 6, 7, 8, 9}
            else:
                grid[(r, c)] = {int(char)}

    return grid



def solved(grid):
    count = len([k for k, v in grid.items() if len(v) == 1])
    return count == 81




def find_singles(moves):
    return { k : v for k, v in moves.items() if len(v) == 1}

def update_grid(grid, move):
    pos, num = move
    new_grid = dict(grid)
    new_grid[pos] = num.pop()
    return new_grid




def solve(grid):
    moves = get_moves(grid)
    print(moves)
    lengths = []
    return grid




grid = text_to_grid(start.replace(" ", ""))
print(grid)
print(solved(grid))
