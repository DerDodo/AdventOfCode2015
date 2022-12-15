import math
from typing import List, Tuple

from file_util import read_input_file


class Item:
    cost: int
    damage: int
    armor: int

    def __init__(self, cost: int, damage: int, armor: int):
        self.cost = cost
        self.damage = damage
        self.armor = armor


class Boss:
    hp: int
    damage: int
    armor: int

    def __init__(self, lines: List[str]):
        self.hp = int(lines[0].split(" ")[-1])
        self.damage = int(lines[1].split(" ")[-1])
        self.armor = int(lines[2].split(" ")[-1])

    def would_be_defeated_by(self, items: List[Item], player_hp: int) -> bool:
        player_damage = sum(map(lambda item: item.damage, items))
        player_armor = sum(map(lambda item: item.armor, items))

        boss_hp_loss = max(player_damage - self.armor, 1)
        player_hp_loss = max(self.damage - player_armor, 1)

        players_rounds_to_defeat = math.ceil(player_hp / player_hp_loss)
        boss_rounds_to_defeat = math.ceil(self.hp / boss_hp_loss)

        return players_rounds_to_defeat >= boss_rounds_to_defeat


def create_shop() -> Tuple[List[Item], List[Item], List[Item]]:
    weapons = [
        Item(8, 4, 0),
        Item(10, 5, 0),
        Item(25, 6, 0),
        Item(40, 7, 0),
        Item(74, 8, 0),
    ]
    armors = [
        Item(13, 0, 1),
        Item(31, 0, 2),
        Item(53, 0, 3),
        Item(75, 0, 4),
        Item(102, 0, 5),
    ]
    rings = [
        Item(25, 1, 0),
        Item(50, 2, 0),
        Item(100, 3, 0),
        Item(20, 0, 1),
        Item(40, 0, 2),
        Item(80, 0, 3),
    ]
    return weapons, armors, rings


def create_item_combinations(weapons: List[Item], armors: List[Item], rings: List[Item]) -> List[List[Item]]:
    item_combinations: List[List[Item]] = [[]]

    ring_combinations: List[List[Item]] = [[]]
    for i in range(len(rings)):
        ring_combinations.append([rings[i]])
        for j in range(i + 1, len(rings)):
            ring_combinations.append([rings[i], rings[j]])

    for weapon in weapons:
        for ring_combination in ring_combinations:
            item_combinations.append([weapon] + ring_combination)
            for armor in armors:
                item_combinations.append([weapon, armor] + ring_combination)

    return item_combinations


def parse_input_file() -> Boss:
    lines = read_input_file(21)
    return Boss(lines)


def level21(player_hp: int) -> Tuple[int, int]:
    boss = parse_input_file()
    weapons, armors, rings = create_shop()
    item_combinations = create_item_combinations(weapons, armors, rings)
    min_price_to_win = 10000
    max_price_to_lose = 0
    for item_combination in item_combinations:
        if boss.would_be_defeated_by(item_combination, player_hp):
            min_price_to_win = min(min_price_to_win, sum(map(lambda item: item.cost, item_combination)))
        else:
            max_price_to_lose = max(max_price_to_lose, sum(map(lambda item: item.cost, item_combination)))
    return min_price_to_win, max_price_to_lose


if __name__ == "__main__":
    _min_price_to_win, _max_price_to_lose = level21(100)
    print(f"Min price to win: {_min_price_to_win}")
    print(f"Max price to lose: {_max_price_to_lose}")
