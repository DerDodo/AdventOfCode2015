from typing import List, Tuple

from util.file_util import read_input_file


class AuntSue:
    id: int
    children: int | None
    cats: int | None
    samoyeds: int | None
    pomeranians: int | None
    akitas: int | None
    vizslas: int | None
    goldfish: int | None
    trees: int | None
    cars: int | None
    perfumes: int | None

    def __init__(self, line: str):
        parts = line.replace(":", "").replace(",", "").split(" ")
        self.id = int(parts[1])
        self.children = None
        self.cats = None
        self.samoyeds = None
        self.pomeranians = None
        self.akitas = None
        self.vizslas = None
        self.goldfish = None
        self.trees = None
        self.cars = None
        self.perfumes = None
        for i in range(2, len(parts), 2):
            self.__setattr__(parts[i], int(parts[i + 1]))

    def fits1(self, other) -> bool:
        return (
            (self.children is None or self.children == other.children)
            and (self.cats is None or self.cats == other.cats)
            and (self.samoyeds is None or self.samoyeds == other.samoyeds)
            and (self.pomeranians is None or self.pomeranians == other.pomeranians)
            and (self.akitas is None or self.akitas == other.akitas)
            and (self.vizslas is None or self.vizslas == other.vizslas)
            and (self.goldfish is None or self.goldfish == other.goldfish)
            and (self.trees is None or self.trees == other.trees)
            and (self.cars is None or self.cars == other.cars)
            and (self.perfumes is None or self.perfumes == other.perfumes)
        )

    def fits2(self, other) -> bool:
        return (
            (self.children is None or self.children == other.children)
            and (self.cats is None or self.cats > other.cats)
            and (self.samoyeds is None or self.samoyeds == other.samoyeds)
            and (self.pomeranians is None or self.pomeranians < other.pomeranians)
            and (self.akitas is None or self.akitas == other.akitas)
            and (self.vizslas is None or self.vizslas == other.vizslas)
            and (self.goldfish is None or self.goldfish < other.goldfish)
            and (self.trees is None or self.trees > other.trees)
            and (self.cars is None or self.cars == other.cars)
            and (self.perfumes is None or self.perfumes == other.perfumes)
        )


def parse_input_file() -> List[AuntSue]:
    lines = read_input_file(16)
    return list(map(AuntSue, lines))


def level16() -> Tuple[int, int]:
    aunt_sues = parse_input_file()
    aunt_pattern = AuntSue(
        "Sue 0: children: 3, cats: 7, samoyeds: 2, pomeranians: 3, akitas: 0, vizslas: 0,"
        + "goldfish: 5, trees: 3, cars: 2, perfumes: 1"
    )
    correct_sue1 = list(filter(lambda a: a.fits1(aunt_pattern), aunt_sues))
    correct_sue2 = list(filter(lambda a: a.fits2(aunt_pattern), aunt_sues))
    return correct_sue1[0].id, correct_sue2[0].id


if __name__ == "__main__":
    _aunt_sue1, _aunt_sue2 = level16()
    print(f"Aunt Sue (1): {_aunt_sue1}")
    print(f"Aunt Sue (2): {_aunt_sue2}")
