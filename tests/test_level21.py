from level21 import level21


def test_level21():
    _min_price_to_win, _max_price_to_lose = level21(8)
    assert _min_price_to_win == 65
    assert _max_price_to_lose == 188
