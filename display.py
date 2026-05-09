HORIZONTAL_LINE = "+-------+-------+-------+"


def draw_row(grid, row):
    row_text = "| "
    for c in range(9):
        row_text += f"{grid[row, c]} " if grid[row, c] != "." else "  "
        if c % 3 == 2:
            row_text += "| "
    return row_text


def draw_grid(grid):
    lines = [HORIZONTAL_LINE]
    for r in range(9):
        lines.append(draw_row(grid, r))
        if r % 3 == 2:
            lines.append(HORIZONTAL_LINE)
    return "\n".join(lines)
