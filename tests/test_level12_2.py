import json

from level12_2 import sum_numbers


def test_level12_2():
    assert sum_numbers(json.loads("[1,2,3]")) == 6
    assert sum_numbers(json.loads('[1,{"c":"red","b":2},3]')) == 4
    assert sum_numbers(json.loads('{"d":"red","e":[1,2,3,4],"f":5}')) == 0
    assert sum_numbers(json.loads('[1,"red",5]')) == 6
