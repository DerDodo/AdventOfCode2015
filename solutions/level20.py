from collections import defaultdict


def level20_1(target_number: int) -> int:
    target_number = target_number // 10
    houses = defaultdict(int)
    limit = min(1_000_000, target_number)
    for house in range(1, limit):
        for elf in range(1, limit // house + 1):
            houses[house * elf] += elf
        if houses[house] >= target_number:
            return house


def level20_2(target_number: int) -> int:
    houses = defaultdict(int)
    limit = min(1_000_000, target_number)
    for elf in range(1, limit):
        for house in range(1, 51):
            houses[house * elf] += elf * 11
        if houses[elf] >= target_number:
            return elf


if __name__ == "__main__":
    _first_house1 = level20_1(33100000)
    print(f"First house (1): {_first_house1}")
    _first_house2 = level20_2(33100000)
    print(f"First house (2): {_first_house2}")
