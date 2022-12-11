from typing import List, Tuple

from util.file_util import read_input_file


class Container:
    id: int
    volume: int

    def __init__(self, _id: int, volume: int):
        self.id = _id
        self.volume = volume


def parse_input_file() -> List[Container]:
    lines = read_input_file(17)
    containers = list()
    for i in range(len(lines)):
        containers.append(Container(i, int(lines[i])))
    return containers


def find_all_fill_options(containers: List[Container], remaining_volume: int) -> List[List[Container]]:
    permutations = []
    for i in range(len(containers)):
        item = containers[i]
        if item.volume == remaining_volume:
            permutations.append([item])
        elif item.volume < remaining_volume:
            remaining_list = containers[i + 1:]
            for permutation in find_all_fill_options(remaining_list, remaining_volume - item.volume):
                permutations.append([item] + permutation)
    return permutations


def level17(volume: int) -> Tuple[int, int]:
    containers = parse_input_file()
    filled_containers = find_all_fill_options(containers, volume)
    min_number_of_containers = min(map(lambda c: len(c), filled_containers))
    num_options_with_min_containers = len(list(filter(lambda c: len(c) == min_number_of_containers, filled_containers)))
    return len(filled_containers), num_options_with_min_containers


if __name__ == '__main__':
    _num_combinations, _num_options_with_min_containers = level17(150)
    print(f"Num combinations (1): {_num_combinations}")
    print(f"Num combinations (2): {_num_options_with_min_containers}")
