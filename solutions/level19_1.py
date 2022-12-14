from typing import List, Tuple, Dict, Set

from util.file_util import read_input_file


def parse_input(lines: List[str]) -> Tuple[Dict[str, List[str]], str]:
    replacements: Dict[str, List[str]] = {}
    for line in lines:
        if line == "":
            break

        parts = line.split(" => ")
        if parts[0] not in replacements:
            replacements[parts[0]] = []

        replacements[parts[0]].append(parts[1])
    return replacements, lines[-1]


def find_distinct_replacements(text: str, molecule: str, replacements: List[str]) -> Set[str]:
    parts = f"<{text}>".split(molecule)
    new_molecules = set()
    for i in range(len(parts) - 1):
        left = molecule.join(parts[0 : i + 1])
        right = molecule.join(parts[i + 1 :])
        for replacement in replacements:
            new_molecule = f"{left}{replacement}{right}"
            new_molecules.add(new_molecule[1:-1])
    return new_molecules


def level19_1(lines: List[str]) -> int:
    replacements, text = parse_input(lines)
    distinct_molecules = set()
    for replacement_key in replacements:
        new_molecules = find_distinct_replacements(text, replacement_key, replacements[replacement_key])
        distinct_molecules.update(new_molecules)
    return len(distinct_molecules)


if __name__ == "__main__":
    _num_molecules = level19_1(read_input_file(19))
    print(f"Num molecules (1): {_num_molecules}")
