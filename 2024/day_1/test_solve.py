import pytest
import solve

lines = """
3   4
4   3
2   5
1   3
3   9
3   3
"""

def test_solve():
    (result, result2) = solve.solve(lines.split("\n"))
    assert result == 11
    assert result2 == 31
