def bitArrayToDec(bitArr):
    i = 0
    for bit in bitArr:
        i = (i << 1) | bit
    return i

with open("inputs/input3.txt", encoding="utf8") as infile:
    totalLength = 0
    bitCount = []
    for line in infile:
        line = line.strip()
        if len(bitCount) == 0:
            bitCount = [0] * len(line)
        for i, bit in enumerate(line):
            bit = int(bit)
            bitCount[i] += bit
        totalLength +=1
    bitResult = [int(bit > totalLength / 2) for bit in bitCount]
    bitResult2 = [1 - bit for bit in bitResult]
    print(bitArrayToDec(bitResult) * bitArrayToDec(bitResult2))
