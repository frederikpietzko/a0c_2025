import pytest

from solution import solve, transpose_diagonally, transpose, solve2

input = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

probelm = """
...S.
..A..
.M...
X....
"""

def test_solution():
    result = solve(probelm.split("\n"))
    assert result == 1
    result = solve(input.split("\n"))
    assert result == 18

test_m = """
ABC
KLM
XYZ
"""
def test_transpose():
    test = list(filter(lambda line: len(line) > 0, test_m.split("\n")))
    diagonal = transpose_diagonally(test)
    assert diagonal == [
        "A",
        "KB",
        "XLC",
        "YM",
        "Z"
    ]
    transposed = transpose(test)
    assert transposed == [
        "XKA",
        "YLB",
        "ZMC"
    ]
    diagonal_revered = transpose_diagonally(transposed)
    assert diagonal_revered == [
        "X",
        "YK",
        "ZLA",
        "MB",
        "C"
    ]

test_i_2 = """
M.S
.A.
M.S
"""

def test_solve_2():
    result = solve2(test_i_2.split("\n"))
    assert result == 1
    result = solve2(input.split("\n"))
    assert result == 9
