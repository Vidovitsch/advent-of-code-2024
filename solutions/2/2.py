import pathlib
import re
from typing import List, Tuple

from advent_helper.decorators import process_puzzle_input
from advent_helper.puzzle import Puzzle

CURRENT = pathlib.Path(__file__).parent

PuzzleInput = List[List[int]]


def process_input(input: List[str]) -> PuzzleInput:
    return [[int(number) for number in line.split()] for line in input]


@process_puzzle_input(process_input)
def solve(input: PuzzleInput) -> int:
    safe = 0

    for report in input:
        if not is_save(report):
            for i in range(len(report)):
                report_without_number = [
                    number for j, number in enumerate(report) if i != j
                ]
                if is_save(report_without_number):
                    safe += 1
                    break
        else:
            safe += 1

    return safe


def is_save(report) -> bool:
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    if min(differences) < 0 and max(differences) > 0:
        return False

    for difference in differences:
        if abs(difference) < 1 or abs(difference) > 3:
            return False

    return True


if __name__ == "__main__":
    (
        Puzzle("Day 2: Red-Nosed Reports (part 1)", CURRENT / "input.txt")
        .add_test({"input_path": CURRENT / "test_1.txt", "expected_result": 4})
        .solve(solve)
    )
