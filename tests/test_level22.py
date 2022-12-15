from level22 import level22


def test_level22():
    _min_mana_to_win_easy = level22(50, 500, 1, False)
    assert _min_mana_to_win_easy == 226
    _min_mana_to_win_hard = level22(50, 500, 1, True)
    assert _min_mana_to_win_hard == 226
