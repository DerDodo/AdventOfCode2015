from time import time


def look_and_say(input: str) -> str:
    current = None
    num = 0
    output = ""
    for character in input:
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
    text = "3113322113"
    for i in range(50):
        text = look_and_say(text)
    print(f"Answer: {len(text)}")
