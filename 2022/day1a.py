with open("inputs/input1.txt", encoding="utf8") as infile:
    maxCal = 0
    currentCal = 0
    for line in infile:
        line = line.strip()
        if len(line) == 0:
            currentCal = 0
            continue
        num = int(line)
        currentCal += num
        maxCal = max(currentCal, maxCal)
    print(maxCal)
