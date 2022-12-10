from level3_1 import Santa
from util.file_util import read_input_file


def level3_2(description: str) -> int:
    next_santa = 0
    santas = [Santa(), Santa()]
    santas[0].deliver()

    for character in description:
        if character == "^":
            santas[next_santa].move_y(-1)
        elif character == "v":
            santas[next_santa].move_y(1)
        elif character == "<":
            santas[next_santa].move_x(-1)
        elif character == ">":
            santas[next_santa].move_x(1)
        santas[next_santa].deliver()
        next_santa = abs(next_santa - 1)

    houses = santas[0].houses.union(santas[1].houses)
    return len(houses)


if __name__ == '__main__':
    _num_houses = level3_2(read_input_file(3)[0])
    print(f"Num houses both santa's: {_num_houses}")
