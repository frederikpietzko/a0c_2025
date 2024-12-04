import re

xmas = re.compile("XMAS")
samx = re.compile("SAMX")


def solve(matrix: list[str]):
    matrix = list(filter(lambda x: len(x) > 0, matrix))
    count = 0
    for row in matrix:
        count += len(xmas.findall(row))
        count += len(samx.findall(row))

    transposed = transpose(matrix)

    for row in transposed:
        count += len(xmas.findall(row))
        count += len(samx.findall(row))

    diagonal = transpose_diagonally(matrix)
    for row in diagonal:
        count += len(xmas.findall(row))
        count += len(samx.findall(row))

    rev_diagonal = transpose_diagonally(transposed)
    for row in rev_diagonal:
        count += len(xmas.findall(row))
        count += len(samx.findall(row))

    return count


def transpose_diagonally(matrix: list[str]):
    transposed = []
    ROW = len(matrix)
    COL = len(matrix[0])
    for line in range(1, ROW + COL):
        transposed.append("")
        start_col = max(0, line - ROW)
        count = min(line, (COL - start_col), ROW)
        for j in range(0, count):
            value = matrix[min(ROW, line) - j - 1][start_col + j]
            transposed[line - 1] += value
    return transposed


def transpose(matrix: list[str]):
    transposed = []

    for i in range(len(matrix[0])):
        transposed.append("")
        for j in range(len(matrix)):
            transposed[i] += matrix[j][i]
        transposed[i] = transposed[i][::-1]
    return transposed


def solve2(matrix: list[str]):
    matrix = list(filter(lambda x: len(x) > 0, matrix))
    count = 0
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            if is_cross(matrix, (i, j)):
                count += 1
    return count


def is_cross(matrix: list[str], pos: tuple[int, int]) -> bool:
    x, y = pos

    cross = [
        [get(matrix, (x - 1, y - 1)), get(matrix, (x, y)), get(matrix, (x + 1, y + 1))],
        [get(matrix, (x - 1, y + 1)), get(matrix, (x, y)), get(matrix, (x + 1, y - 1))]
    ]
    matching = list(
        filter(
            lambda row: row == "MAS" or row == "SAM",
            map(lambda row: "".join(row), cross)
        )
    )
    return len(matching) == 2


def get(matrix: list[str], pos: tuple[int, int]) -> str:
    return matrix[pos[0]][pos[1]]


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()
    part1 = solve(lines)
    print(f"Part 1: {part1}")
    part2 = solve2(list(map(lambda line: line.strip("\n"), lines)))
    print(f"Part 2: {part2}")
