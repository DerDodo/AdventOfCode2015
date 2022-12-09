from level12_1 import sum_numbers


def test_level12_1():
    assert sum_numbers('[1,2,3]') == 6
    assert sum_numbers('[1,{"c":"red","b":2},3]') == 6
    assert sum_numbers('{"d":"red","e":[1,2,3,4],"f":5}') == 15
    assert sum_numbers('[1,"red",5]') == 6
