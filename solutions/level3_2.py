from util.file_util import read_input_file

houses = {}


def deliver(destination_x: int, destination_y: int):
    destination_id = f"{destination_x}/{destination_y}"
    if destination_id in houses:
        houses[destination_id] += 1
    else:
        houses[destination_id] = 1


def level3_2() -> int:
    description = read_input_file(3)[0]

    santa_x = santa_y = 0
    robo_santa_x = robo_santa_y = 0
    deliver(santa_x, santa_y)
    deliver(robo_santa_x, robo_santa_y)
    santa_next = True

    for character in description:
        if character == "^":
            if santa_next:
                santa_y -= 1
            else:
                robo_santa_y -= 1
        elif character == "v":
            if santa_next:
                santa_y += 1
            else:
                robo_santa_y += 1
        elif character == "<":
            if santa_next:
                santa_x -= 1
            else:
                robo_santa_x -= 1
        elif character == ">":
            if santa_next:
                santa_x += 1
            else:
                robo_santa_x += 1
        if santa_next:
            deliver(santa_x, santa_y)
        else:
            deliver(robo_santa_x, robo_santa_y)
        santa_next = not santa_next

    return len(houses)


if __name__ == '__main__':
    _num_houses = level3_2()
    print(f"Num houses both santa's: {_num_houses}")
