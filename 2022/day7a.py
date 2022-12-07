

def lookupSize(dir, dirs):
    sum = 0
    for item in dirs[dir]:
        if item.isdecimal():
            sum += int(item)
        else:
            sum += lookupSize(dir + item, dirs)
    return sum


with open("inputs/input7.txt", encoding="utf8") as infile:
    dirs = dict()
    currentDir = []
    for line in infile:
        line = line.strip()
        spl = line.split()
        if spl[0] == "$" and spl[1] == "cd":
            if spl[2] == "..":
                currentDir.pop()
            else:
                currentDir.append(spl[2])
            continue
        if spl[0] == "$" and spl[1] == "ls":
            continue
        fullDir = "".join(currentDir)
        if fullDir not in dirs:
            dirs[fullDir] = []
        if spl[0] == "dir":
            dirs[fullDir].append(spl[1])
        else:
            dirs[fullDir].append(spl[0])
    dirSizes = dict()
    for item in dirs.keys():
        dirSizes[item] = lookupSize(item, dirs)

    print(dirSizes)
    sum = 0
    for size in dirSizes.values():
        if size <= 100000:
            sum += size
    print(sum)