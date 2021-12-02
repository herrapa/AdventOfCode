with open("inputs/input1a.txt", encoding="utf8") as infile:
    previousMeasurement = None
    increases = 0
    for line in infile:
        line = line.strip()
        num = int(line)
        if previousMeasurement != None and num > previousMeasurement:
            increases += 1
        previousMeasurement = num
    print(increases)
