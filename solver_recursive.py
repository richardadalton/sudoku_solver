from display import draw_grid

# start = "..693.25..23584.1..1.....93.89.1...6....47...675...1.2..1.72....5..6.8.426.8.3..."
start = "..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3.."


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







def same_row(grid, pos):
    row, col = pos
    return set([grid[row, c] for c in range(9) if grid[row, c] != "0"])



def same_col(grid, pos):
    row, col = pos
    return set([grid[r, col] for r in range(9) if grid[r, col] != "0"])



def same_square(grid, pos):

    def square_range(n):
        lower = (n // 3) * 3
        upper = lower + 3
        return range(lower, upper)

    row, col = pos
    row_range = square_range(row)
    col_range = square_range(col)
    return set([grid[r, c] for r in row_range
                               for c in col_range
                                   if grid[r, c] != "."])



def possible_values(grid, pos):
    all = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
    on_row = same_row(grid, pos)
    on_col = same_col(grid, pos)
    in_square = same_square(grid, pos)
    taken = on_row.union(on_col).union(in_square)
    return all.difference(taken)


def get_moves(grid):
    moves = {}
    for position in grid:
        if grid[position] == ".":
            possible = possible_values(grid, position)
            if len(possible) > 0:
                moves[position] = possible
    return moves


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




grid = text_to_grid(start)
print(grid)
print(solved(grid))
