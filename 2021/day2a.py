with open("inputs/input2.txt", encoding="utf8") as infile:
    depth = 0
    horizontal = 0
    for line in infile:
        line = line.strip()
        spl = line.split(" ")
        command = spl[0]
        value = int(spl[1])
        if command == "forward":
            horizontal += value
        elif command == "down":
            depth += value
        elif command == "up":
            depth -= value
    print(depth * horizontal)
