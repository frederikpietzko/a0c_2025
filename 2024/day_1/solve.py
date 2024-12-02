from queue import PriorityQueue
from collections import defaultdict


def solve(lines: list[str]):
    left = PriorityQueue()
    right = PriorityQueue()
    freqs = defaultdict(int)

    for line in filter(lambda x: len(x) > 0, lines):
        l, r = line.split("   ")
        left.put(int(l))
        right.put(int(r))
        freqs[int(r)] += 1

    result = 0
    result2 = 0

    while not left.empty() and not right.empty():
        l = left.get()
        r = right.get()
        diff = max(l, r) - min(l, r)
        result += diff
        result2 += l * freqs[l]

    return result, result2


if __name__ == "__main__":
    with open("input.txt", mode='r') as f:
        lines = f.readlines()
    result = solve(lines)
    print("The result is: ", result)
