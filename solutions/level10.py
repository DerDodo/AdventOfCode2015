def look_and_say(text: str) -> str:
    current = None
    num = 0
    output = ""
    for character in text:
        if character == current:
            num += 1
        else:
            if num > 0:
                output += f"{num}{current}"
            current = character
            num = 1
    output += f"{num}{current}"
    return output


def level10(repetitions: int) -> int:
    start = "3113322113"
    for _ in range(repetitions):
        start = look_and_say(start)
    return len(start)


if __name__ == '__main__':
    _answer40 = level10(40)
    print(f"Answer: {_answer40}")
    _answer50 = level10(50)
    print(f"Answer: {_answer50}")
