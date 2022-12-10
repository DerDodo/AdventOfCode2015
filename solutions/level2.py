from typing import List, Tuple

from util.file_util import read_input_file


class Box:
    w: int
    h: int
    l: int

    def __init__(self, description: str):
        parts = description.split("x")
        [self.w, self.h, self.l] = [int(part) for part in parts]

    def get_needed_paper(self):
        return (2 * self.w * self.h +
                2 * self.w * self.l +
                2 * self.h * self.l +
                min(self.w * self.l, self.w * self.h, self.l * self.h))

    def get_needed_ribbon(self):
        return (min(2 * self.w + 2 * self.l, 2 * self.w + 2 * self.h, 2 * self.l + 2 * self.h) +
                self.w * self.l * self.h)


def parse_input_file() -> List[Box]:
    lines = read_input_file(2)
    return list(map(Box, lines))


def level2() -> Tuple[int, int]:
    boxes = parse_input_file()
    needed_paper = sum(map(Box.get_needed_paper, boxes))
    needed_ribbon = sum(map(Box.get_needed_ribbon, boxes))
    return needed_paper, needed_ribbon


if __name__ == '__main__':
    _needed_paper, _needed_ribbon = level2()
    print(f"Needed paper: {_needed_paper}")
    print(f"Needed paper: {_needed_ribbon}")
