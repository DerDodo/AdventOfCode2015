from solutions.level1 import level1


def test_level1():
    _final_floor, _entering_basement = level1()
    assert _final_floor == -1
    assert _entering_basement == 5
