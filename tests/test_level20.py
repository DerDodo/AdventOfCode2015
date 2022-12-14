from level20 import level20_1, level20_2


def test_level20():
    assert level20_1(60) == 4
    assert level20_1(70) == 4
    assert level20_1(120) == 6
    assert level20_1(150) == 8
    assert level20_2(60) == 4
    assert level20_2(70) == 4
    assert level20_2(120) == 6
    assert level20_2(150) == 8
