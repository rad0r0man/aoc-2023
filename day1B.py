import re

from tools.puzzle_reader import puzzle_reader
from day1A import create_int


nums_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def replace_from_dict(input_str):
    for word, num in nums_dict.items():
        if input_str.startswith(word):
            return num + replace_from_dict(input_str[len(word) :])
    return input_str[0] + replace_from_dict(input_str[1:]) if input_str else ""

def main():
    sample_puzzle = puzzle_reader("day1B/sample.txt")

    str_list = [replace_from_dict(s.lower()) for s in sample_puzzle]
    print(sum([create_int(string) for string in str_list]))


if __name__ == "__main__":
    main()
