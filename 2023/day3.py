import re
import copy

with open("inputs/input3.txt", encoding="utf8") as infile:
    sum = 0
    matrix = []
    lines = []
    for line in infile:
        line = line.strip()
        lines += [line]
        numIndexes = [(m.start(), m.end()) for m in re.finditer(r"\d+", line)]
        symbolIndexes = [m.start() for m in re.finditer(r"[^\d\.]", line)]
        matrix.append([numIndexes, symbolIndexes])
    
    for i, indexes in enumerate(matrix):
        numIndexes, symbolIndexes = indexes
        numIndexes = copy.copy(numIndexes)
        symbolIndexes = copy.copy(symbolIndexes)
        if i > 0:
            symbolIndexes += matrix[i - 1][1]
        if i < len(matrix) - 1:
            symbolIndexes += matrix[i + 1][1]
        for numIndex in numIndexes:
            found = False
            for symbolIndex in symbolIndexes:
                if not found and numIndex[0] - 1 <= symbolIndex <= numIndex[1]:
                    num = int(lines[i][numIndex[0]:numIndex[1]])
                    sum += num
                    found = True
    print(sum)

with open("inputs/input3.txt", encoding="utf8") as infile:
    sum = 0
    matrix = []
    lines = []
    for line in infile:
        line = line.strip()
        lines += [line]
        numIndexes = [(m.start(), m.end()) for m in re.finditer(r"\d+", line)]
        symbolIndexes = [m.start() for m in re.finditer(r"\*", line)]
        matrix.append([numIndexes, symbolIndexes])
    
    for i, indexes in enumerate(matrix):
        numIndexes, symbolIndexes = indexes
        numIndexes = copy.copy(numIndexes)
        symbolIndexes = copy.copy(symbolIndexes)
        numIndexes = [(x, int(lines[i][x[0]:x[1]])) for x in numIndexes]
        if i > 0:
            lineNumIndexes = matrix[i - 1][0]
            numIndexes += [(x, int(lines[i - 1][x[0]:x[1]])) for x in lineNumIndexes]
        if i < len(matrix) - 1:
            lineNumIndexes = matrix[i + 1][0]
            numIndexes += [(x, int(lines[i + 1][x[0]:x[1]])) for x in lineNumIndexes]
        for symbolIndex in symbolIndexes:
            found = []
            for numIndex, num in numIndexes:
                if numIndex[0] - 1 <= symbolIndex <= numIndex[1]:
                    found.append(num)
            if len(found) == 2:
                sum += found[0] * found[1]

    print(sum)