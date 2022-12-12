from cmath import sqrt


with open("inputs/input9.txt", encoding="utf8") as infile:
    visited = set()
    headX = 0
    headY = 0
    tailX = 0
    tailY = 0
    for line in infile:
        line = line.strip()
        dir, step = line.split()
        step = int(step)
        dirX = 0
        dirY = 0
        if dir == "R":
            dirX = 1
        if dir == "L":
            dirX = -1
        if dir == "U":
            dirY = 1
        if dir == "D":
            dirY = -1
        for i in range(step):
            headX += dirX
            headY += dirY
            dist = (headX - tailX) ** 2 + (headY - tailY) ** 2
            if dist == 4:
                tailX += dirX
                tailY += dirY
            elif dist > 4.0:
                tailX += max(-1, min(1, headX - tailX))
                tailY += max(-1, min(1, headY - tailY))
            visited.add(str(tailX) + "," + str(tailY))
    print(len(visited))


