from typing import Tuple

from file_util import read_input_file


def parse_input_file() -> Tuple[int, int]:
    line = read_input_file(25)[0]
    parts = line.split(" ")
    return int(parts[16][:-1]), int(parts[18][:-1])


def calc_triangle_number_at(row: int, col: int) -> float:
    side = row + col - 1
    return (side * (side + 1)) / 2 - row


def exp_mod(base: int, exp: float, mod: int) -> int:
    if exp == 0:
        return 1
    if exp % 2 == 0:
        return pow(exp_mod(base, exp / 2, mod), 2) % mod
    return (base * exp_mod(base, exp - 1, mod)) % mod


def level25(row: int, col: int) -> int:
    # https://eddmann.com/posts/advent-of-code-2015-day-25-let-it-snow/
    first_code = 20151125
    base = 252533
    exp = calc_triangle_number_at(row, col)
    mod = 33554393
    return (exp_mod(base, exp, mod) * first_code) % mod


if __name__ == "__main__":
    _row, _col = parse_input_file()
    print(f"Code: {level25(_row, _col)}")
