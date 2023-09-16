
def load_grid(file):
    with open(file) as f:
        text = f.read().upper().split("\n")
    text = "".join(text).replace(" ", "")
    return {(r, c): text[r * 9 + c] for r in range(9) for c in range(9)}

def text_to_grid(str):
    str = str.replace(" ", "")
    return {(r, c): str[r * 9 + c] for r in range(9) for c in range(9)}

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
