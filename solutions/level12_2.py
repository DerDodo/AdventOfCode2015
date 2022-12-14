import json

from util.file_util import read_input_file


def is_red(document) -> bool:
    if isinstance(document, dict):
        for key in document:
            value = document[key]
            if value == "red":
                return True
    return False


def sum_numbers(document) -> int:
    if is_red(document):
        return 0

    current_sum = 0
    for key in document:
        if isinstance(document, dict):
            value = document[key]
        elif isinstance(document, list):
            value = key
        else:
            raise ValueError(f"Cannot process type: {type(document)}")

        if isinstance(value, int):
            current_sum += value
        elif isinstance(value, dict) or isinstance(value, list):
            current_sum += sum_numbers(value)
        elif not isinstance(value, str):
            raise ValueError(f"Cannot process type: {type(value)}")

    return current_sum


def level12_2() -> int:
    json_document = json.loads(read_input_file(12)[0])
    return sum_numbers(json_document)


if __name__ == "__main__":
    print(f"Sum: {level12_2()}")
