from typing import List

from util.file_util import read_input_file


class Box:
    w: int
    h: int
    l: int

    def __init__(self, description: str):
        parts = description.split("x")
        [self.w, self.h, self.l] = [eval(part) for part in parts]

    def get_needed_paper(self):
        return (2 * self.w * self.h +
                2 * self.w * self.l +
                2 * self.h * self.l +
                min(self.w * self.l, self.w * self.h, self.l * self.h))

    def get_needed_ribbon(self):
        return (min(2 * self.w + 2 * self.l, 2 * self.w + 2 * self.h, 2 * self.l + 2 * self.h) +
                self.w * self.l * self.h)


def parse_input_file() -> List[Box]:
    lines = read_input_file(2, 1)
    return list(map(Box, lines))


if __name__ == '__main__':
    boxes = parse_input_file()

    needed_paper = sum(map(Box.get_needed_paper, boxes))
    print(f"Needed paper: {needed_paper}")

    needed_ribbon = sum(map(Box.get_needed_ribbon, boxes))
    print(f"Needed paper: {needed_ribbon}")
