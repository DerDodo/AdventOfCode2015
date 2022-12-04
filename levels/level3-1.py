from util.file_util import read_input_file

houses = {}


def deliver(destination_x: int, destination_y: int):
    destination_id = f"{destination_x}/{destination_y}"
    if destination_id in houses:
        houses[destination_id] += 1
    else:
        houses[destination_id] = 1


if __name__ == '__main__':
    description = read_input_file(3, 1)[0]

    x = 0
    y = 0
    deliver(x, y)

    for character in description:
        if character == "^":
            y -= 1
        elif character == "v":
            y += 1
        elif character == "<":
            x -= 1
        elif character == ">":
            x += 1
        deliver(x, y)

    print(f"Num houses only santa: {len(houses)}")
