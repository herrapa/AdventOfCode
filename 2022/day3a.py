with open("inputs/input3.txt", encoding="utf8") as infile:
    sum = 0
    for line in infile:
        line = line.strip()
        characters = list(line)
        half = len(line) // 2
        first = characters[:half]
        second = characters[half:]
        first = set(first)
        second = set(second)
        shared = first.intersection(second).pop()
        val = ord(shared)
        if shared.islower():
            val -= 96
        else:
            val -= 38
        sum += val
    print(sum)
