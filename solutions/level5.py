from typing import Tuple

from util.file_util import read_input_file


def is_nice1(line: str):
    num_vowels = 0
    has_double_character = False
    has_naughty_string = False
    last_character = None
    for character in line:
        if character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
            num_vowels += 1

        if last_character == character:
            has_double_character = True

        combination = f"{last_character}{character}"
        if combination == "ab" or combination == "cd" or combination == "pq" or combination == "xy":
            has_naughty_string = True

        last_character = character

    return num_vowels >= 3 and has_double_character and not has_naughty_string


def is_nice2(line: str):
    has_xyx_pattern = False
    has_repeating_combination = False
    last_character = None
    before_last_character = None
    last_combination = None
    before_last_combination = None
    combinations = set()

    for character in line:
        if character == before_last_character:
            has_xyx_pattern = True

        combination = f"{last_character}{character}"
        if combination != last_combination or combination == before_last_combination:
            if combination in combinations:
                has_repeating_combination = True
            combinations.add(combination)

        before_last_character = last_character
        last_character = character
        before_last_combination = last_combination
        last_combination = combination

    return has_xyx_pattern and has_repeating_combination


def level5() -> Tuple[int, int]:
    lines = read_input_file(5)
    num_nice1 = sum(1 if is_nice1(line) else 0 for line in lines)
    num_nice2 = sum(1 if is_nice2(line) else 0 for line in lines)
    return num_nice1, num_nice2


if __name__ == '__main__':
    _num_nice1, _num_nice2 = level5()
    print(f"Num nice1 lines: {_num_nice1}")
    print(f"Num nice2 lines: {_num_nice2}")
