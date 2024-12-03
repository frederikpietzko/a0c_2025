import re

find_mul = re.compile("mul\((\d+),(\d+)\)")
find_do = re.compile("do\(\)")
find_dont = re.compile("don't\(\)")

def solve(lines: list[str]) -> int:
    lines = list(filter(lambda line: len(line) > 0, lines))
    return sum(map(calculate, lines))

def solve2(lines: list[str]) -> int:
    lines = list(filter(lambda line: len(line) > 0, lines))
    # return sum(map(calc_rec, lines))
    return calc_rec("".join(lines))

def calc_rec(line: str) -> int:
    if line == "":
        return 0
    next_dont = find_dont.search(line)
    if next_dont is None:
        return calculate(line)
    next_do = find_do.search(line)
    if next_do is None:
        return calculate(line[:next_dont.start()])
    return calculate(line[:next_dont.start()]) + calc_rec(line[next_do.end():])

def calculate(line: str) -> int:
    matches = find_mul.findall(line)
    return sum(map(lambda match: int(match[0]) * int(match[1]), matches))

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()
    part1 = solve(lines)
    print(f"Part 1: {part1}")
    part2 = solve2(lines)
    print(f"Part 2: {part2}")
