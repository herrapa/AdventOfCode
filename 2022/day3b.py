with open("inputs/input3.txt", encoding="utf8") as infile:
    sum = 0
    idx = 1
    intersects = set()
    for line in infile:
        line = line.strip()
        characters = list(line)
        char_set = set(characters)
        if len(intersects) == 0:
            intersects = char_set
        intersects = intersects.intersection(char_set)
        if idx % 3 == 0:
            shared = intersects.pop()
            val = ord(shared)
            if shared.islower():
                val -= 96
            else:
                val -= 38
            sum += val
            intersects = set()
        idx += 1

    print(sum)
