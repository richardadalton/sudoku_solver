
horizonal_line = "+-------+-------+-------+"

def draw_row(grid, row):
    row_text = "| "
    for c in range(9):
        if grid[row, c] == ".":
            row_text += "  "
        else:
            row_text += "{0} ".format(grid[row, c])
        if c % 3 == 2:
            row_text += "| "
    return row_text


def draw_grid(grid):
    grid_text = [horizonal_line]

    for r in range(9):
        grid_text.append(draw_row(grid, r))
        if r % 3 == 2:
            grid_text.append(horizonal_line)

    return "\n".join(grid_text)
