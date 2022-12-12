from level18 import level18


def test_level18():
    assert level18(0, False) == 15
    assert level18(4, False) == 4
    assert level18(0, True) == 17
    assert level18(4, True) == 14
    assert level18(5, True) == 17
