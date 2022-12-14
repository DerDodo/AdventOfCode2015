from typing import List, Dict, Tuple

from util.file_util import read_input_file


class Happiness:
    person: str
    neighbor: str
    happiness_gain: int

    def __init__(self, line: str = None, person: str = None, neighbor: str = None, happiness_gain: int = 0):
        if line is not None:
            parts = line.split(" ")
            self.person = parts[0]
            self.neighbor = parts[-1][0:-1]
            multiplier = 1 if parts[2] == "gain" else -1
            self.happiness_gain = multiplier * int(parts[3])
        else:
            self.person = person
            self.neighbor = neighbor
            self.happiness_gain = happiness_gain


class HappinessEvaluator:
    happiness_dict = Dict[str, Dict[str, int]]

    def __init__(self, happinesses: List[Happiness]):
        self.happiness_dict = {}
        for happiness in happinesses:
            if happiness.person not in self.happiness_dict:
                self.happiness_dict[happiness.person] = {}
            self.happiness_dict[happiness.person][happiness.neighbor] = happiness.happiness_gain

    def evaluate(self, persons: List[str]) -> int:
        happiness_value = 0
        num_persons = len(persons)
        for i in range(num_persons):
            happiness_value += self.happiness_dict[persons[i]][persons[(i - 1) % num_persons]]
            happiness_value += self.happiness_dict[persons[i]][persons[(i + 1) % num_persons]]
        return happiness_value


def parse_input_file(include_me: bool) -> Tuple[HappinessEvaluator, List[str]]:
    lines = read_input_file(13)
    happinesses = list(map(lambda l: Happiness(line=l), lines))
    persons = list(set(map(lambda h: h.person, happinesses)))
    if include_me:
        for person in persons:
            happinesses.append(Happiness(person="me", neighbor=person, happiness_gain=0))
            happinesses.append(Happiness(person=person, neighbor="me", happiness_gain=0))
        persons.append("me")
    return HappinessEvaluator(happinesses), persons


def generate_all_permutations(persons: List[str]) -> List[List[str]]:
    if len(persons) == 0:
        return []

    if len(persons) == 1:
        return [persons]

    permutations = []
    for i in range(len(persons)):
        start = persons[i]
        remaining_list = persons[:i] + persons[i + 1 :]
        for permutation in generate_all_permutations(remaining_list):
            permutations.append([start] + permutation)
    return permutations


def level13(include_me: bool) -> int:
    happiness_evaluator, persons = parse_input_file(include_me)
    all_permutations = generate_all_permutations(persons)
    return max(map(lambda p: happiness_evaluator.evaluate(p), all_permutations))


if __name__ == "__main__":
    print(f"Max happiness (without me): {level13(False)}")
    print(f"Max happiness (with me): {level13(True)}")
