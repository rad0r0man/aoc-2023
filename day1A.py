import sys
import os

# sys.path.append(os.path.dirname(os.path.realpath(__file__)))

# print(sys.path)
from tools.puzzle_reader import puzzle_reader

test_puzzle = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]


def create_int(string: str) -> int:
    left = None
    right = None
    for letter in string:
        if left is None and letter.isdigit():
            left = letter
            break

    for letter in reversed(string):
        if right is None and letter.isdigit():
            right = letter
            break

    return int(left + right)



def main():
    puzzle_input = puzzle_reader("day1A/puzzle_input.txt")

    print(sum([create_int(string) for string in puzzle_input]))


if __name__ == "__main__":
    main()
