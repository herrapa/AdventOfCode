with open("inputs/input6.txt", encoding="utf8") as infile:
    for line in infile:
        line = line.strip()
        buffer = []
        for i, c in enumerate(line):
            if len(buffer) > 3:
                buffer.pop()
            buffer.insert(0, c)
            if len(set(buffer)) == 4:
                print(i + 1)
                break
