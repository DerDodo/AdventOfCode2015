from typing import List

from util.file_util import read_input_file


class LightGrid:
    lights: List[List[bool]]  # x,y

    def __init__(self):
        self.lights = [[False] * 1000 for i in range(1000)]

    def turn_on(self, start_x: int, start_y: int, end_x: int, end_y: int):
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                self.lights[x][y] = True

    def turn_off(self, start_x: int, start_y: int, end_x: int, end_y: int):
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                self.lights[x][y] = False

    def toggle(self, start_x: int, start_y: int, end_x: int, end_y: int):
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                self.lights[x][y] = not self.lights[x][y]

    def get_num_lit(self) -> int:
        return sum(map(lambda line: sum(map(lambda light: 1 if light == True else 0, line)), self.lights))


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
    lines = read_input_file(6, 1)
    return list(map(Command, lines))


if __name__ == '__main__':
    grid = LightGrid()
    commands = parse_input_file()

    for command in commands:
        command.execute(grid)

    print(f"Num lit lights: {grid.get_num_lit()}")
