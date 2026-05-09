def load_grid(file):
    with open(file) as f:
        text = f.read().upper().split("\n")
    text = "".join(text).replace(" ", "")
    return {(r, c): text[r * 9 + c] for r in range(9) for c in range(9)}


def text_to_grid(s):
    s = "".join(s.upper().split())
    return {(r, c): s[r * 9 + c] for r in range(9) for c in range(9)}


def same_row(grid, pos):
    row, _ = pos
    return {grid[row, c] for c in range(9) if grid[row, c] != "."}


def same_col(grid, pos):
    _, col = pos
    return {grid[r, col] for r in range(9) if grid[r, col] != "."}


def same_box(grid, pos):
    row, col = pos
    r0, c0 = (row // 3) * 3, (col // 3) * 3
    return {grid[r, c] for r in range(r0, r0 + 3)
                        for c in range(c0, c0 + 3)
                        if grid[r, c] != "."}


def possible_values(grid, pos):
    taken = same_row(grid, pos) | same_col(grid, pos) | same_box(grid, pos)
    return {"1", "2", "3", "4", "5", "6", "7", "8", "9"} - taken
