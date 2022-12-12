from typing import List

from util.file_util import read_input_file


class LightGrid:
    lights: List[List[bool]]  # y,x
    broken_corners: bool

    def __init__(self, lines: List[str], broken_corners: bool):
        self.lights = []
        self.broken_corners = broken_corners

        for line in lines:
            light_line = list(map(lambda c: False if c == '.' else True, line))
            self.lights.append(light_line)

        if broken_corners:
            self.lights[0][0] = True
            self.lights[len(self.lights) - 1][0] = True
            self.lights[0][len(self.lights[0]) - 1] = True
            self.lights[len(self.lights) - 1][len(self.lights[0]) - 1] = True

    def get_num_lit(self) -> int:
        return sum(map(lambda line: sum(map(lambda light: 1 if light else 0, line)), self.lights))

    def animate(self):
        new_lights = []
        for y in range(len(self.lights)):
            new_line = []
            for x in range(len(self.lights[y])):
                new_line.append(self.animate_light(x, y))
            new_lights.append(new_line)
        self.lights = new_lights

    def animate_light(self, x: int, y: int) -> bool:
        if self.broken_corners and self.is_corner(x, y):
            return True

        num_neighbors_on = self.get_num_neighbors_on(x, y)
        if self.lights[y][x]:
            return num_neighbors_on == 2 or num_neighbors_on == 3
        else:
            return num_neighbors_on == 3

    def get_num_neighbors_on(self, x: int, y: int) -> int:
        num_neighbors_on = 0
        for y_plus in [-1, 0, 1]:
            check_y = y + y_plus
            for x_plus in [-1, 0, 1]:
                check_x = x + x_plus
                if (0 <= check_x < len(self.lights[0]) and
                        0 <= check_y < len(self.lights) and
                        self.lights[check_y][check_x] and (y_plus != 0 or x_plus != 0)):
                    num_neighbors_on += 1
        return num_neighbors_on

    def is_corner(self, x: int, y: int) -> bool:
        return (x == 0 or x == len(self.lights[0]) - 1) and (y == 0 or y == len(self.lights) - 1)

    def print(self):
        for line in self.lights:
            print("".join(map(lambda light: "#" if light else ".", line)))


def parse_input_file(broken_corners: bool) -> LightGrid:
    lines = read_input_file(18)
    return LightGrid(lines, broken_corners)


def level18(num_steps: int, broken_corners: bool) -> int:
    light_grid = parse_input_file(broken_corners)
    for _ in range(num_steps):
        light_grid.animate()
    return light_grid.get_num_lit()


if __name__ == '__main__':
    _num_lit = level18(100, False)
    print(f"Num lit (1): {_num_lit}")
    _num_lit = level18(100, True)
    print(f"Num lit (2): {_num_lit}")
