from typing import Tuple

from util.file_util import read_input_file


def get_value1(line: str) -> int:
    value = 0
    count_next = False
    for character in line:
        if count_next:
            if character == "\"" or character == "\\":
                value += 1
            elif character == "x":
                value += 3
            else:
                raise ValueError(f"Forbidden character in line: character: {character}, line: {line}")
            count_next = False
        elif character == "\\":
            count_next = True
    return 2 + value


def get_value2(line: str) -> int:
    num_quotes = line.count("\"")
    num_backslashes = line.count("\\")
    return 2 + num_quotes + num_backslashes


def level8() -> Tuple[int, int]:
    lines = read_input_file(8)
    answer1 = sum(map(get_value1, lines))
    answer2 = sum(map(get_value2, lines))
    return answer1, answer2


if __name__ == '__main__':
    _answer1, _answer2 = level8()
    print(f"Answer 1: {_answer1}")
    print(f"Answer 2: {_answer2}")
