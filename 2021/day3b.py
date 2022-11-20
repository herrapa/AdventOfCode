import operator

def bitArrayToDec(bitArr):
    i = 0
    for bit in bitArr:
        i = (i << 1) | bit
    return i

def bitMask(inputList):
    totalLength = 0
    bitCount = []
    for line in inputList:
        line = line.strip()
        if len(bitCount) == 0:
            bitCount = [0] * len(line)
        for i, bit in enumerate(line):
            bit = int(bit)
            bitCount[i] += bit
        totalLength +=1
    return [int(bit >= totalLength / 2) for bit in bitCount]

def findMatch(startInput, op):
    currentMatches = startInput
    toKeep = []
    lineLength = len(currentMatches[0])
    for idx in range(lineLength):
        bitField = bitMask(currentMatches)
        for line in currentMatches:
            if op(bitField[idx], int(line[idx])):
                toKeep.append(line)
        if len(toKeep) == 1:
            return toKeep[0]
        currentMatches = toKeep
        toKeep = []
    return None

with open("inputs/input3.txt", encoding="utf8") as infile:
    lines = []
    for line in infile:
        line = line.strip()
        lines.append(line)
    
    toKeep = []
    ogrMatch = findMatch(lines, operator.eq)
    csrMatch = findMatch(lines, operator.ne)
    
    print(bitArrayToDec([int(b) for b in ogrMatch]) * bitArrayToDec([int(b) for b in csrMatch]))
