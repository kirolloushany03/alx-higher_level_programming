#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
from sys import argv

if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)

N = 0

try:
    N = int(argv[1])

    if N < 4:
        print("N must be at least 4")
        exit(1)
except Exception:
    print("N must be a number")
    exit(1)

full_cols = set()
full_positve_d = set()
full_negtive_d = set()
c_solution = []
solutions = []


def get_solutions(row):
    """get all possible solutions"""
    for col in range(N):
        if (
            col in full_cols
            or (row - col) in full_positve_d
            or (row + col) in full_negtive_d
        ):
            continue
        add_new(row, col)
        if row == N - 1:
            solutions.append(c_solution.copy())
            remove_old(row, col)
            return
        get_solutions(row + 1)
        remove_old(row, col)


def add_new(row, col):
    """add a new node"""
    c_solution.append([row, col])
    full_cols.add(col)
    full_positve_d.add(row - col)
    full_negtive_d.add(row + col)


def remove_old(row, col):
    """remove an old node"""
    c_solution.remove([row, col])
    full_cols.remove(col)
    full_positve_d.remove(row - col)
    full_negtive_d.remove(row + col)


get_solutions(0)
for solution in solutions:
    print(solution)
