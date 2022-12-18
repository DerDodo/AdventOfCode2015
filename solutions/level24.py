from functools import reduce
from typing import List, Set

from file_util import read_input_file


def parse_input_file() -> List[int]:
    lines = read_input_file(24)
    presents = list(map(lambda line: int(line), lines))
    presents.sort(reverse=True)
    return presents


def get_all_possible_configuration(presents: List[int], remaining_weight: int):
    permutations = []
    for i in range(len(presents)):
        item = presents[i]
        if item == remaining_weight:
            permutations.append([item])
        elif item < remaining_weight:
            remaining_list = presents[i + 1 :]
            for permutation in get_all_possible_configuration(remaining_list, remaining_weight - item):
                permutations.append([item] + permutation)
    return permutations


def is_valid_configuration(all_presents: List[int], config: List[int]):
    remaining_presents = [present for present in all_presents if present not in config]
    target_weight = sum(config)
    configs = get_all_possible_configuration(remaining_presents, target_weight)
    return len(configs) > 1


def get_config_id(presents: List[int]) -> str:
    return "-".join(map(str, presents))


def level24(num_trunks: int) -> int:
    presents = parse_input_file()
    target_weight = sum(presents) // num_trunks
    configurations = get_all_possible_configuration(presents, target_weight)
    configurations_set: Set[str] = set()
    configurations_set.update([get_config_id(config) for config in configurations])
    valid_configurations = list(filter(lambda config: get_config_id(config) in configurations_set, configurations))
    min_presents = min(map(lambda config: len(config), valid_configurations))
    target_configurations = list(filter(lambda config: min_presents == len(config), valid_configurations))
    quantum_entanglements = map(lambda config: reduce(lambda x, y: x * y, config), target_configurations)
    return min(quantum_entanglements)


if __name__ == "__main__":
    print(f"Quantum entanglement (3): {level24(3)}")
    print(f"Quantum entanglement (4): {level24(4)}")
