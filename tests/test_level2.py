from solutions.level2 import level2


def test_level2():
    _needed_paper, _needed_ribbon = level2()
    assert _needed_paper == 58
    assert _needed_ribbon == 34
