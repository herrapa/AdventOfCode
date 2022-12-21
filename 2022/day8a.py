with open("inputs/input8.txt", encoding="utf8") as infile:
    grid = []
    highTrees = set()
    for line in infile:
        line = line.strip()
        grid.append([])
        for d in line:
            grid[-1].append(int(d))
    for i, row in enumerate(grid):
        for j, column in enumerate(row):
            treeId = str(i) + "," + str(j)
            if i == 0 or j == 0 or i == len(row) -1 or j == len(grid) -1:
                highTrees.add(treeId)
                continue
            toLeft = row[0:j]
            toRight = row[j + 1:]
            toTop = [grid[x][j] for x in range(i)]
            toBottom = [grid[x][j] for x in range(i + 1, len(grid))]
            if max(toLeft) < column or max(toRight) < column or max(toTop) < column or max(toBottom) < column:
                highTrees.add(treeId)

    print(len(highTrees))
