with open("inputs/input6.txt", encoding="utf8") as infile:
    inp = [int(x) for x in infile.readline().strip().split(",")]
    toAppend = []
    for n in range(80):
        for i in range(len(inp)):
            if inp[i] == 0:
                toAppend.append(8)
                inp[i] = 6
            else:
                inp[i] = (inp[i] - 1)
        inp += toAppend
        toAppend = []
    print(len(inp))
