from level17 import level17


def test_level17():
    _num_combinations, _num_options_with_min_containers = level17(25)
    assert _num_combinations == 4
    assert _num_options_with_min_containers == 3
