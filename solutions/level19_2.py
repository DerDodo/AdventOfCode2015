from random import randint
from typing import List, Tuple

from util.file_util import read_input_file


def parse_input(lines: List[str]) -> Tuple[List[Tuple[str, str]], str]:
    replacements: List[Tuple[str, str]] = []
    for line in lines:
        if line == "":
            break

        parts = line.split(" => ")
        replacements.append((parts[1], parts[0]))

    return replacements, lines[-1]


def level19_2_try(replacements, text) -> int:
    text_steps = [text]

    for num_steps in range(1000):
        replaced_something = False
        for replacement in replacements:
            if text_steps[-1].__contains__(replacement[0]):
                new_text = text_steps[-1].replace(replacement[0], replacement[1], 1)
                text_steps.append(new_text)
                replaced_something = True
                break
        if not replaced_something:
            if text_steps[-1] == "e":
                return num_steps
            else:
                raise ValueError(f"Cannot replace anything in {text_steps[-1]}")


def level19_2(lines: List[str]) -> int:
    replacements, text = parse_input(lines)
    steps_set = set()
    for _ in range(100):
        try:
            replacements.sort(key=lambda x: len(x[0]) + randint(0, 4), reverse=True)
            num_steps = level19_2_try(replacements, text)
            steps_set.add(num_steps)
        except ValueError:
            pass
    return min(steps_set)


if __name__ == "__main__":
    _num_steps = level19_2(read_input_file(19))
    print(f"Num steps (2): {_num_steps}")
