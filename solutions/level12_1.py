from util.file_util import read_input_file


def sum_numbers(text: str) -> int:
    current_number = ""
    current_sum = 0
    for character in text:
        if character == "-" and current_number == "":
            current_number += "-"
        elif character.isdecimal():
            current_number += character
        else:
            if current_number != "":
                current_sum += int(current_number)
                current_number = ""
    return current_sum


def level12_1() -> int:
    document = read_input_file(12)[0]
    return sum_numbers(document)


if __name__ == '__main__':
    print(f"Sum: {level12_1()}")
