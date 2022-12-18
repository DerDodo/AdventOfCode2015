from abc import abstractmethod
from typing import List, Dict

from file_util import read_input_file


class Operation:
    @abstractmethod
    def execute(self, computer, args: List[str]) -> int:
        pass


class Computer:
    registers: Dict[str, int]
    operations: Dict[str, Operation]

    def __init__(self, operations: Dict[str, Operation], start_value_a: int):
        self.registers = {"a": start_value_a, "b": 0}
        self.operations = operations

    def run(self, program: List[str], target_register: str) -> int:
        program_counter = 0
        while program_counter < len(program):
            parts = program[program_counter].split(" ")
            parts[1] = parts[1].replace(",", "")
            program_counter += self.operations[parts[0]].execute(self, parts[1:])
        return self.registers[target_register]


class Hlf(Operation):
    def execute(self, computer: Computer, args: List[str]) -> int:
        assert len(args) == 1
        computer.registers[args[0]] = computer.registers[args[0]] // 2
        return 1


class Tpl(Operation):
    def execute(self, computer: Computer, args: List[str]) -> int:
        assert len(args) == 1
        computer.registers[args[0]] = computer.registers[args[0]] * 3
        return 1


class Inc(Operation):
    def execute(self, computer: Computer, args: List[str]) -> int:
        assert len(args) == 1
        computer.registers[args[0]] = computer.registers[args[0]] + 1
        return 1


class Jmp(Operation):
    def execute(self, computer: Computer, args: List[str]) -> int:
        assert len(args) == 1
        return int(args[0])


class Jie(Operation):
    def execute(self, computer: Computer, args: List[str]) -> int:
        assert len(args) == 2
        if computer.registers[args[0]] % 2 == 0:
            return int(args[1])
        else:
            return 1


class Jio(Operation):
    def execute(self, computer: Computer, args: List[str]) -> int:
        assert len(args) == 2
        if computer.registers[args[0]] == 1:
            return int(args[1])
        else:
            return 1


def parse_input_file() -> List[str]:
    return read_input_file(23)


def level23(target_register: str, start_value_a: int) -> int:
    operations = {
        "hlf": Hlf(),
        "tpl": Tpl(),
        "inc": Inc(),
        "jmp": Jmp(),
        "jie": Jie(),
        "jio": Jio(),
    }
    computer = Computer(operations, start_value_a)
    return computer.run(parse_input_file(), target_register)


if __name__ == "__main__":
    print(f"b (a=0): {level23('b', 0)}")
    print(f"b (a=1): {level23('b', 1)}")
