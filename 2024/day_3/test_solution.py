import pytest
from solution import solve, solve2

input = """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""

def test_solution():
    result = solve(input.split("\n"))
    assert result == 161

input2 = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""

def test_part_2():
    result = solve2(input2.split("\n"))
    assert result == 48 * 2
