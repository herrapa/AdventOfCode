res = dict()
with open("inputs/input5.txt", encoding="utf8") as infile:
    for line in infile:
        line = line.strip().split(" -> ")
        startx, starty = [int(n) for n in line[0].split(",")]
        endx, endy = [int(n) for n in line[1].split(",")]
        if startx == endx or starty == endy:
            for x in range(min(startx, endx), max(startx, endx) + 1):
                for y in range(min(starty, endy), max(starty, endy) + 1):
                    tup = (x, y)
                    if not tup in res:
                        res[tup] = 0
                    res[tup] += 1

print(sum(map(lambda x : x >= 2, res.values())))