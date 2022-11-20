with open("inputs/input1a.txt", encoding="utf8") as infile:
    previousMeasurement = None
    increases = 0
    slidingList = []
    for line in infile:
        line = line.strip()
        num = int(line)
        slidingList.append(num)
        totSum = None
        if len(slidingList) > 3:
            slidingList.pop(0)
        if len(slidingList) == 3:
            totSum = sum(slidingList)
        if previousMeasurement != None and totSum > previousMeasurement:
            increases += 1
        previousMeasurement = totSum
    print(increases)
