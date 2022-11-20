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

with open("inputs/input9.txt", encoding="utf8") as infile:

    lines = [x.strip() for x in infile.readlines()]
    s = 0
    for line_i, line in enumerate(lines):
        for n_i, n in enumerate(line):
            n = int(n)
            if isColMin(line, n_i, n) and isRowMin(lines, n_i, line_i, n):
                s += (1 + n)
    print(s)
