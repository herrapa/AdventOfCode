
from curses.ascii import islower

with open("inputs/input13.txt", encoding="utf8") as infile:
    
    gridCoords = []
    maxX = 0
    maxY = 0
    cmds = []
    for line in infile:
        line = line.strip()
        if "," in line:
            x, y = [int(x) for x in line.split(",")]
            maxX = max(maxX, x)
            maxY = max(maxY, y)
            gridCoords.append([x, y])
        if "fold along" in line:
            dir, pos = line.split("=")
            dir = dir[-1:]
            cmds.append([dir, pos])

    grid = [] #[["."] * (maxX + 1)] * (maxY + 1)
    for y in range(maxY + 1):
        grid.append([0] * (maxX + 1))


    for x, y in gridCoords:
        grid[y][x] = 1
    
    for y in grid:
        print("".join(str(y)))
    print("")

    for axis, pos in cmds:
        pos = int(pos)
        if axis == "y":
            offset = 1
            while offset + pos < len(grid):
                for i in range(len(grid[0])):
                    grid[pos - offset][i] |= grid[pos + offset][i]
                offset += 1
            grid = grid[:pos]
        if axis == "x":
            offset = 1
            while offset + pos < len(grid[pos]):
                for i in range(len(grid)):
                    grid[i][pos - offset] |= grid[i][pos + offset]
                offset += 1
            for i in range(len(grid)):
                grid[i] = grid[i][:pos]
        
        
        for y in grid:
            print("".join(["." if x == 0 else "#" for x in y]))
        print("")

        # break for task a
        #break
    print(sum([sum(y) for y in grid]))
    
        


#print(1 & 1)

