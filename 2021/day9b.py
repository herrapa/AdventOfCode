import math

def isColMin(line, i, n):
    s = 0
    if i == 0:
        return n < int(line[i + 1])
    elif i == (len(line) -1):
        return n < int(line[i - 1])
    else:
        return n < int(line[i + 1]) and n < int(line[i - 1])

def isRowMin(lines, ix, iy, n):
    s = 0
    if iy == 0:
        return n < int(lines[iy + 1][ix])
    elif iy == (len(lines) -1):
        return n < int(lines[iy - 1][ix])
    else:
        return n < int(lines[iy + 1][ix]) and n < int(lines[iy - 1][ix])

def basinSearch(lines, ix, iy, visited):
    tup = (ix, iy)
    if tup in visited:
        return 0
    if iy < 0 or iy >= len(lines):
        return 0
    if ix < 0 or ix >= len(lines[iy]):
        return 0
    if int(lines[iy][ix]) == 9:
        return 0
    visited.append(tup)
    return 1 + basinSearch(lines, ix + 1, iy, visited) + basinSearch(lines, ix, iy + 1, visited) + basinSearch(lines, ix - 1, iy, visited) + basinSearch(lines, ix, iy - 1, visited)

with open("inputs/input9.txt", encoding="utf8") as infile:

    lines = [x.strip() for x in infile.readlines()]
    basins = []
    for line_i, line in enumerate(lines):
        for n_i, n in enumerate(line):
            n = int(n)
            if isColMin(line, n_i, n) and isRowMin(lines, n_i, line_i, n):
                basinSize = basinSearch(lines, n_i, line_i, [])
                basins.append(basinSize)
    basins.sort()
    print(math.prod(basins[-3:]))
