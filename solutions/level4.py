import hashlib


def level4(key: str, num_zeros: int) -> int:
    target_string = ''.join(["0" for _ in range(num_zeros)])
    for i in range(1, 10000000, 1):
        text = key + str(i)
        md5 = hashlib.md5(text.encode()).hexdigest()
        if md5[0:num_zeros] == target_string:
            return i

    raise ValueError("Couldn't find solution")


if __name__ == '__main__':
    _id_5 = level4("yzbqklnj", 5)
    _id_6 = level4("yzbqklnj", 6)
    print(f"Found id (5): {_id_5}")
    print(f"Found id (6): {_id_6}")
