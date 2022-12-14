def clean_password(text: str) -> str:
    new_text = ""
    fill_a = False
    for character in text:
        if fill_a:
            new_text += "a"
        elif character == "i":
            new_text += "j"
            fill_a = True
        elif character == "o":
            new_text += "p"
            fill_a = True
        elif character == "l":
            new_text += "m"
            fill_a = True
        else:
            new_text += character

    return new_text


def increment(text: str) -> str:
    increment_i = len(text) - 1
    increment_next = True
    while increment_next and increment_i > 0:
        character = text[increment_i]
        if character == "z":
            text = text[0:increment_i] + "a" + text[(increment_i + 1) :]
            increment_i -= 1
        else:
            new_character = chr(ord(character) + 1)
            if new_character == "i" or new_character == "o" or new_character == "l":
                chr(ord(character) + 1)
            text = text[0:increment_i] + new_character + text[(increment_i + 1) :]
            increment_next = False
    return text


def is_correct_password(text: str) -> bool:
    has_three_following = False
    pairs = set()

    before_last_character = None
    last_character = None

    for character in text:
        if character == "i" or character == "o" or character == "l":
            return False

        if (
            not has_three_following
            and last_character is not None
            and before_last_character is not None
            and ord(character) - ord(last_character) == 1
            and ord(last_character) - ord(before_last_character) == 1
        ):
            has_three_following = True

        if character == last_character:
            pairs.add(character)

        before_last_character = last_character
        last_character = character

    return has_three_following and len(pairs) >= 2


def level11(password: str) -> str:
    password = clean_password(password)
    password = increment(password)
    while not is_correct_password(password):
        password = increment(password)
    return password


if __name__ == "__main__":
    _password = level11("vzbxkghb")
    print(f"New password: {_password}")
    _password = level11(_password)
    print(f"New new password: {_password}")
