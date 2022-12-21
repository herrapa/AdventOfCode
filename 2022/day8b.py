with open("inputs/input8.txt", encoding="utf8") as infile:
    grid = []
    maxScore = 0
    for line in infile:
        line = line.strip()
        grid.append([])
        for d in line:
            grid[-1].append(int(d))
    for i, row in enumerate(grid):
        for j, column in enumerate(row):
            treeId = str(i) + "," + str(j)
            if i == 0 or j == 0 or i == len(row) -1 or j == len(grid) -1:
                continue
            toLeft = row[0:j]
            toLeft.reverse()
            toRight = row[j + 1:]
            toTop = [grid[x][j] for x in range(i)]
            toTop.reverse()
            toBottom = [grid[x][j] for x in range(i + 1, len(grid))]
            leftScore = len(toLeft)
            for ix, x in enumerate(toLeft):
                if x >= column:
                    leftScore = ix +1
                    break
            rightScore = len(toRight)
            for ix, x in enumerate(toRight):
                if x >= column:
                    rightScore = ix +1
                    break
            topScore = len(toTop)
            for ix, x in enumerate(toTop):
                if x >= column:
                    topScore = ix +1
                    break
            bottomScore = len(toBottom)
            for ix, x in enumerate(toBottom):
                if x >= column:
                    bottomScore = ix +1
                    break
            maxScore = max(maxScore, leftScore * rightScore * topScore * bottomScore)


    print(maxScore)
