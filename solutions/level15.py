from typing import List, Dict, Tuple

from util.file_util import read_input_file


MAX_SPACE = 100


class Ingredient:
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int

    def __init__(self, line: str):
        parts = line.replace(",", "").split(" ")
        self.name = parts[0][:-1]
        self.capacity = int(parts[2])
        self.durability = int(parts[4])
        self.flavor = int(parts[6])
        self.texture = int(parts[8])
        self.calories = int(parts[10])


def parse_input_file() -> Dict[str, Ingredient]:
    lines = read_input_file(15)
    ingredients = map(Ingredient, lines)
    return {i.name: i for i in ingredients}


class Cookie:
    ingredients: Dict[str, int]

    def __init__(self, ingredients: Dict[str, int]):
        self.ingredients = {}
        self.ingredients.update(ingredients)

    def get_score(self, ingredient_definition: Dict[str, Ingredient]) -> int:
        capacity = durability = flavor = texture = 0

        for ingredient in self.ingredients:
            capacity += ingredient_definition[ingredient].capacity * self.ingredients[ingredient]
            durability += ingredient_definition[ingredient].durability * self.ingredients[ingredient]
            flavor += ingredient_definition[ingredient].flavor * self.ingredients[ingredient]
            texture += ingredient_definition[ingredient].texture * self.ingredients[ingredient]
        return max(0, capacity) * max(0, durability) * max(0, flavor) * max(0, texture)

    def get_calories(self, ingredient_definition: Dict[str, Ingredient]) -> int:
        return sum(map(lambda i: ingredient_definition[i].calories * self.ingredients[i], self.ingredients))

    def get_remaining_space(self) -> int:
        return MAX_SPACE - sum(self.ingredients.values())


def calc_all_pots(cookie: Cookie, ingredients: List[Ingredient]) -> List[Cookie]:
    if len(ingredients) == 0:
        return []

    if len(ingredients) == 1:
        new_cookie = Cookie(cookie.ingredients)
        new_cookie.ingredients[ingredients[0].name] = cookie.get_remaining_space()
        return [new_cookie]

    all_pots = []
    for i in range(cookie.get_remaining_space() + 1):
        new_cookie = Cookie(cookie.ingredients)
        new_cookie.ingredients[ingredients[0].name] = i
        all_pots.extend(calc_all_pots(new_cookie, ingredients[1:]))
    return all_pots


def level15() -> Tuple[int, int]:
    ingredient_definition = parse_input_file()
    cookies = calc_all_pots(Cookie({}), list(ingredient_definition.values()))
    scores = list(map(lambda c: c.get_score(ingredient_definition), cookies))
    filtered_cookies = filter(lambda c: c.get_calories(ingredient_definition) == 500, cookies)
    filtered_scores = list(map(lambda c: c.get_score(ingredient_definition), filtered_cookies))
    return max(scores), max(filtered_scores)


if __name__ == "__main__":
    _score_1, _score_2 = level15()
    print(f"Score: (1) {_score_1}")
    print(f"Score: (2) {_score_2}")
