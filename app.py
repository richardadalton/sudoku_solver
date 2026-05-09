from flask import Flask, render_template, request
from sudoku import solve

app = Flask(__name__)


def form_to_grid(form):
    return {(r, c): (form.get(f"cell_{r}_{c}", "").strip() or ".")
            for r in range(9) for c in range(9)}


def grid_to_rows(grid):
    return [[grid[(r, c)] for c in range(9)] for r in range(9)]


def is_solved(grid):
    return all(v != "." for v in grid.values())


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/solve", methods=["POST"])
def solve_puzzle():
    original = form_to_grid(request.form)
    result = solve(dict(original))
    return render_template(
        "index.html",
        original=grid_to_rows(original),
        result=grid_to_rows(result),
        solved=is_solved(result),
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)

