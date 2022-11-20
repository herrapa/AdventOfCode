with open("inputs/input2.txt", encoding="utf8") as infile:
    depth = 0
    horizontal = 0
    aim = 0
    for line in infile:
        line = line.strip()
        spl = line.split(" ")
        command = spl[0]
        value = int(spl[1])
        if command == "forward":
            horizontal += value
            depth += aim * value
        elif command == "down":
            aim += value
        elif command == "up":
            aim -= value
    print(depth * horizontal)
