from file_util import read_input_file_id
from level19_1 import level19_1
from level19_2 import level19_2


def test_level19():
    assert level19_1(read_input_file_id(19, 0)) == 4
    assert level19_1(read_input_file_id(19, 2)) == 7
    assert level19_2(read_input_file_id(19, 0)) == 3
    assert level19_2(read_input_file_id(19, 2)) == 6
