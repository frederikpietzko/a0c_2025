from typing import Iterable


def solve(lines: list[str], enable_problem_dampener: bool = False):
    lines: Iterable[str] = filter(lambda x: len(x) > 0, lines)
    reports = (list(map(int, line.split(" "))) for line in lines)
    safe_reports = 0
    for report in reports:
        safe = is_safe(report)
        if not safe and enable_problem_dampener:
            safe = problem_dampener(report)

        if safe:
            safe_reports += 1
    return safe_reports

def problem_dampener(report: list[int]) -> bool:
    for i in range(0, len(report)):
        copy = report.copy()
        copy.pop(i)
        if is_safe(copy):
            return True
    return False


def is_safe(report: list[int]) -> bool:
    if report != sorted(report) and report != sorted(report, reverse=True):
        return False
    safe = True
    last_value = report[0]
    for value in report[1:]:
        diff = max(last_value, value) - min(last_value, value)
        if diff < 1 or diff > 3:
            safe = False
            break
        last_value = value
    return safe

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    res = solve(lines)
    print(f'Part 1: {res}')
    res = solve(lines, enable_problem_dampener=True)
    print(f'Part 2: {res}')