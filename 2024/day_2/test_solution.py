import pytest
from solution import solve

input = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

def test_solution():
    res = solve(input.split("\n"))
    assert res == 2

def test_solution_2():
    res = solve(input.split("\n"), enable_problem_dampener=True)
    assert res == 4
