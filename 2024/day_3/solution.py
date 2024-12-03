import re
from collections import namedtuple

find_all = re.compile("(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))")

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

Mul = namedtuple("mul", ["left", "right"])
Do = namedtuple("do", [])
Dont = namedtuple("dont", [])

def solve3(lines: list[str]) -> int:
    result = parse("".join(lines))
    return calculate3(result)


def calculate3(instructions: list[Mul | Do | Dont]) -> int:
    mode = True
    result = 0
    for inst in instructions:
        match inst:
            case Mul(left, right):
                if mode:
                    result += left * right
            case Do():
                mode = True
            case Dont():
                mode = False
            case _:
                raise Exception("Invalid input")
    return result


def parse(line: str) -> list[Mul | Do | Dont]:
    return list(map(parse_to, find_all.findall(line)))

def parse_to(op: str) -> Mul | Do | Dont:
    match list(op):
        case ['m', 'u', 'l', *_]:
            match = find_mul.findall(op)[0]
            return Mul(int(match[0]), int(match[1]))
        case ['d', 'o', 'n', '\'', 't', *_]:
            return Dont()
        case ['d', 'o', *_]:
            return Do()
        case _:
            raise Exception("Invalid case!")

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()
    part1 = solve(lines)
    print(f"Part 1: {part1}")
    part2 = solve3(lines)
    print(f"Part 2: {part2}")
