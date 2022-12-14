from typing import List

from util.file_util import read_input_file


class LightGrid:
    lights: List[List[int]]  # x,y

    def __init__(self):
        self.lights = [[False] * 1000 for _ in range(1000)]

    def turn_on(self, start_x: int, start_y: int, end_x: int, end_y: int):
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                self.lights[x][y] += 1

    def turn_off(self, start_x: int, start_y: int, end_x: int, end_y: int):
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                self.lights[x][y] = max(self.lights[x][y] - 1, 0)

    def toggle(self, start_x: int, start_y: int, end_x: int, end_y: int):
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                self.lights[x][y] += 2

    def get_num_lit(self) -> int:
        return sum(map(lambda line: sum(line), self.lights))


class Command:
    action: str
    start_x: int
    start_y: int
    end_x: int
    end_y: int

    def __init__(self, line: str):
        line = line.replace("turn on", "turnon")
        line = line.replace("turn off", "turnoff")
        parts = line.split(" ")
        self.action = parts[0]

        start = parts[1].split(",")
        end = parts[3].split(",")

        self.start_x = int(start[0])
        self.start_y = int(start[1])
        self.end_x = int(end[0])
        self.end_y = int(end[1])

    def execute(self, light_grid: LightGrid):
        if self.action == "turnon":
            light_grid.turn_on(self.start_x, self.start_y, self.end_x, self.end_y)
        elif self.action == "turnoff":
            light_grid.turn_off(self.start_x, self.start_y, self.end_x, self.end_y)
        elif self.action == "toggle":
            light_grid.toggle(self.start_x, self.start_y, self.end_x, self.end_y)
        else:
            raise ValueError(f"Invalid command: {self.action}")


def parse_input_file() -> List[Command]:
    lines = read_input_file(6)
    return list(map(Command, lines))


def level6_2() -> int:
    grid = LightGrid()
    commands = parse_input_file()

    for command in commands:
        command.execute(grid)

    return grid.get_num_lit()


if __name__ == "__main__":
    _num_lit = level6_2()
    print(f"Num lit lights: {_num_lit}")
