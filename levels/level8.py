from util.file_util import read_input_file


def get_value(line: str) -> int:
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


if __name__ == '__main__':
    lines = read_input_file(8, 1)

    answer = sum(map(get_value, lines))
    print(f"Answer: {answer}")
