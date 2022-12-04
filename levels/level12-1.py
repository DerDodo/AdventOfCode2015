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


if __name__ == '__main__':
    document = read_input_file(12, 1)[0]
    print(f"Sum: {sum_numbers(document)}")
