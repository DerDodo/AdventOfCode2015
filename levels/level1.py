from util.file_util import read_input_file


if __name__ == '__main__':
    description = read_input_file(1, 1)[0]
    count_opening = description.count("(")
    count_closing = description.count(")")

    print(f"Final floor: {count_opening - count_closing}")

    current_floor = 0
    i = 0
    for character in description:
        i += 1
        if character == "(":
            current_floor += 1
        else:
            current_floor -= 1

        if current_floor == -1:
            print(f"Entering basement at: {i}")
            break
