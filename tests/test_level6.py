from solutions.level6_1 import level6_1
from solutions.level6_2 import level6_2


def test_level6_1():
    _num_lit = level6_1()
    assert _num_lit == 1000000
    _num_lit = level6_2()
    assert _num_lit == 2000000
