from typing import Tuple

from util.file_util import read_input_file


def level1() -> Tuple[int, int]:
    description = read_input_file(1)[0]
    count_opening = description.count("(")
    count_closing = description.count(")")
    final_floor = count_opening - count_closing

    current_floor = i = 0
    for character in description:
        i += 1
        if character == "(":
            current_floor += 1
        else:
            current_floor -= 1

        if current_floor == -1:
            return final_floor, i

    raise ValueError("Didn't enter basement!")


if __name__ == "__main__":
    _final_floor, _entering_basement = level1()
    print(f"Final floor: {_final_floor}")
    print(f"Entering basement at: {_entering_basement}")
