import pathlib
import collections
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
    left = input[0]
    counter = collections.Counter(input[1])

    return sum(counter[number] * number for number in left)


if __name__ == "__main__":
    (
        Puzzle("Day 1: Historian Hysteria (part 2)", CURRENT / "input.txt")
        .add_test({"input_path": CURRENT / "test_1.txt", "expected_result": 31})
        .solve(solve)
    )
