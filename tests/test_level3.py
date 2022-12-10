from solutions.level3_1 import level3_1
from solutions.level3_2 import level3_2


def test_level3_1():
    assert level3_1("^v") == 2
    assert level3_1("^>v<") == 4
    assert level3_1("^v^v^v^v^v") == 2


def test_level3_2():
    assert level3_2("^v") == 3
    assert level3_2("^>v<") == 3
    assert level3_2("^v^v^v^v^v") == 11
