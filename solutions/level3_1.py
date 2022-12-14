from typing import Set

from util.file_util import read_input_file


class Santa:
    x: int
    y: int
    houses = Set[str]

    def __init__(self):
        self.x = self.y = 0
        self.houses = set()

    def move_x(self, by: int):
        self.x += by

    def move_y(self, by: int):
        self.y += by

    def deliver(self):
        destination_id = f"{self.x}/{self.y}"
        self.houses.add(destination_id)


def level3_1(description: str) -> int:
    santa = Santa()
    santa.deliver()

    for character in description:
        if character == "^":
            santa.move_y(-1)
        elif character == "v":
            santa.move_y(1)
        elif character == "<":
            santa.move_x(-1)
        elif character == ">":
            santa.move_x(1)
        santa.deliver()

    return len(santa.houses)


if __name__ == "__main__":
    _num_houses = level3_1(read_input_file(3)[0])
    print(f"Num houses only santa: {_num_houses}")
