import hashlib

if __name__ == '__main__':
    key = "yzbqklnj"

    i = 1

    while i < 10000000:
        if i % 10000 == 0:
            print(f"Checking {i}...")

        text = key + str(i)
        md5 = hashlib.md5(text.encode()).hexdigest()
        if md5[0:6] == "000000":
            print(f"Found id: {i}")
            break
        i += 1
