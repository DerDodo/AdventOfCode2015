from typing import List

from util.file_util import read_input_file


class Reindeer:
    speed: int
    flying_duration: int
    resting_duration: int
    passed_distance: int
    points: int
    is_resting: bool
    remaining_time_in_state: int

    def __init__(self, line: str):
        parts = line.split(" ")
        self.speed = int(parts[3])
        self.flying_duration = int(parts[6])
        self.resting_duration = int(parts[13])
        self.passed_distance = 0
        self.points = 0
        self.is_resting = False
        self.remaining_time_in_state = self.flying_duration

    def fly_for(self, duration: int):
        while duration > 0:
            duration_in_step = min(self.remaining_time_in_state, duration)
            self.remaining_time_in_state -= duration_in_step
            duration -= duration_in_step

            if not self.is_resting:
                self.passed_distance += self.speed * duration_in_step

            if self.remaining_time_in_state == 0:
                self.is_resting = not self.is_resting
                self.remaining_time_in_state = self.resting_duration if self.is_resting else self.flying_duration


def parse_input_file() -> List[Reindeer]:
    lines = read_input_file(14)
    return list(map(Reindeer, lines))


def level14_1(duration: int) -> int:
    reindeer = parse_input_file()
    for r in reindeer:
        r.fly_for(duration)
    winning_distance = max(map(lambda _r: _r.passed_distance, reindeer))
    return winning_distance


def level14_2(duration: int) -> int:
    reindeer = parse_input_file()
    for _ in range(duration):
        for r in reindeer:
            r.fly_for(1)
        leading_distance = max(map(lambda _r: _r.passed_distance, reindeer))
        for r in reindeer:
            if r.passed_distance == leading_distance:
                r.points += 1
    return max(map(lambda _r: _r.points, reindeer))


if __name__ == "__main__":
    print(f"Winning distance: {level14_1(2503)}")
    print(f"Winning points: {level14_2(2503)}")
