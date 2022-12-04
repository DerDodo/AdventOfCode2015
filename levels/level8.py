from util.file_util import read_input_file


def get_value1(line: str) -> int:
    value = 0
    count_next = False
    for character in line:
        if count_next:
            if character == "\"" or character == "\\":
                value += 1
            elif character == "x":
                value += 3
            else:
                raise ValueError(f"Forbidden character in line: character: {character}, line: {line}")
            count_next = False
        elif character == "\\":
            count_next = True
    return 2 + value


def get_value2(line: str) -> int:
    num_quotes = line.count("\"")
    num_backslashes = line.count("\\")
    return 2 + num_quotes + num_backslashes


if __name__ == '__main__':
    lines = read_input_file(8, 1)

    answer1 = sum(map(get_value1, lines))
    print(f"Answer 1: {answer1}")

    answer2 = sum(map(get_value2, lines))
    print(f"Answer 2: {answer2}")
