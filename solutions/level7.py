from abc import abstractmethod
from typing import Dict, Tuple

from util.file_util import read_input_file_id


class CircuitContent:
    wires: Dict

    def __init__(self):
        self.wires = {}

    def add_operation(self, wire: str, operation):
        self.wires[wire] = operation

    def get_value(self, wire: str) -> int:
        return self.wires[wire].eval(self)


class InputProvider:
    @abstractmethod
    def get_value(self, circuit: CircuitContent) -> int:
        pass


class ValueInputProvider(InputProvider):
    value: int

    def __init__(self, line: str):
        self.value = int(line)

    def get_value(self, circuit: CircuitContent) -> int:
        return self.value


class WireInputProvider(InputProvider):
    wire: str
    value: int | None

    def __init__(self, wire: str):
        self.wire = wire
        self.value = None

    def get_value(self, circuit: CircuitContent) -> int:
        if self.value is None:
            self.value = circuit.get_value(self.wire)
        return self.value


def create_input_provider(value: str) -> InputProvider:
    if value.isdecimal():
        return ValueInputProvider(value)
    else:
        return WireInputProvider(value)


class Operation:
    @abstractmethod
    def eval(self, circuit: CircuitContent) -> int:
        pass


class ValueOperation(Operation):
    input: InputProvider

    def __init__(self, line: str):
        self.input = create_input_provider(line)

    def eval(self, circuit: CircuitContent) -> int:
        return self.input.get_value(circuit)


class NotOperation(Operation):
    input: InputProvider

    def __init__(self, line: str):
        self.input = create_input_provider(line)

    def eval(self, circuit: CircuitContent) -> int:
        return ~(self.input.get_value(circuit))


class AndOperation(Operation):
    left: InputProvider
    right: InputProvider

    def __init__(self, left: str, right: str):
        self.left = create_input_provider(left)
        self.right = create_input_provider(right)

    def eval(self, circuit: CircuitContent) -> int:
        return self.left.get_value(circuit) & self.right.get_value(circuit)


class OrOperation(Operation):
    left: InputProvider
    right: InputProvider

    def __init__(self, left: str, right: str):
        self.left = create_input_provider(left)
        self.right = create_input_provider(right)

    def eval(self, circuit: CircuitContent) -> int:
        return self.left.get_value(circuit) | self.right.get_value(circuit)


class LeftShiftOperation(Operation):
    wire: InputProvider
    value: InputProvider

    def __init__(self, wire: str, value: str):
        self.wire = create_input_provider(wire)
        self.value = create_input_provider(value)

    def eval(self, circuit: CircuitContent) -> int:
        return self.wire.get_value(circuit) << self.value.get_value(circuit)


class RightShiftOperation(Operation):
    wire: InputProvider
    value: InputProvider

    def __init__(self, wire: str, value: str):
        self.wire = create_input_provider(wire)
        self.value = create_input_provider(value)

    def eval(self, circuit: CircuitContent) -> int:
        return self.wire.get_value(circuit) >> self.value.get_value(circuit)


def create_operation(line: str) -> Operation:
    parts = line.split(" ")
    if len(parts) == 1:
        return ValueOperation(line)
    elif len(parts) == 2:
        if parts[0] == "NOT":
            return NotOperation(parts[1])
        else:
            raise ValueError(f"Unknown command: {line}")
    elif len(parts) == 3:
        if parts[1] == "AND":
            return AndOperation(parts[0], parts[2])
        elif parts[1] == "OR":
            return OrOperation(parts[0], parts[2])
        elif parts[1] == "LSHIFT":
            return LeftShiftOperation(parts[0], parts[2])
        elif parts[1] == "RSHIFT":
            return RightShiftOperation(parts[0], parts[2])
        else:
            raise ValueError(f"Unknown command: {line}")
    else:
        raise ValueError(f"Unknown command: {line}")


class Circuit:
    wires: CircuitContent

    def __init__(self):
        self.wires = CircuitContent()

    def add_operation(self, wire: str, operation: Operation):
        self.wires.add_operation(wire, operation)

    def get_value(self, wire: str) -> int:
        return self.wires.get_value(wire)


def parse_input_file(file_id: int) -> Circuit:
    lines = read_input_file_id(7, file_id)
    circuit = Circuit()
    for line in lines:
        parts = line.split(" -> ")
        circuit.add_operation(parts[1], create_operation(parts[0]))
    return circuit


def level7(file_id: int, wire: str) -> int:
    grid = parse_input_file(file_id)

    result = grid.get_value(wire)
    if result < 0:
        result += (1 << 16)
    return result


if __name__ == '__main__':
    _result_1 = level7(1, "a")
    _result_2 = level7(2, "a")
    print(f"Wire a (1): {_result_1}")
    print(f"Wire a (2): {_result_2}")
