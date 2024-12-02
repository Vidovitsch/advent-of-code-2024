import pathlib
import re
from typing import List, Tuple

from advent_helper.decorators import process_puzzle_input
from advent_helper.puzzle import Puzzle

CURRENT = pathlib.Path(__file__).parent

PuzzleInput = Tuple[List[int], List[int]]


def process_input(input: List[str]) -> PuzzleInput:
    lists: PuzzleInput = ([], [])

    for line in input:
        left, right = line.split("   ")
        lists[0].append(int(left))
        lists[1].append(int(right))

    return lists


@process_puzzle_input(process_input)
def solve(input: PuzzleInput) -> int:
    left = sorted(input[0])
    right = sorted(input[1])

    return sum(abs(left[i] - right[i]) for i in range(len(left)))


if __name__ == "__main__":
    (
        Puzzle("Day 1: Historian Hysteria (part 1)", CURRENT / "input.txt")
        .add_test({"input_path": CURRENT / "test_1.txt", "expected_result": 11})
        .solve(solve)
    )
