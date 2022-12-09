from solutions.level9 import level9


def test_level9():
    _shortest_route, _longest_route = level9()
    assert _shortest_route == 605
    assert _longest_route == 982
