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


if __name__ == '__main__':
    start = "3113322113"
    for i in range(50):
        start = look_and_say(start)
    print(f"Answer: {len(start)}")
