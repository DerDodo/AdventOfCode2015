from solutions.level3_1 import level3_1
from solutions.level3_2 import level3_2


def test_level3_1():
    _num_houses = level3_1()
    assert _num_houses == 2


def test_level3_2():
    _num_houses = level3_2()
    assert _num_houses == 11
