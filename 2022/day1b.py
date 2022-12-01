with open("inputs/input1.txt", encoding="utf8") as infile:
    maxCals = []
    currentCal = 0
    for line in infile:
        line = line.strip()
        if len(line) == 0:
            maxCals.append(currentCal)
            currentCal = 0
            continue
        num = int(line)
        currentCal += num
    maxCals.sort()
    maxCals = maxCals[-3:]

    print(sum(maxCals))
