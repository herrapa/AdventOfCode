with open("inputs/input7.txt", encoding="utf8") as infile:
    inp = [int(x) for x in infile.readline().strip().split(",")]
    maxNum = max(inp)
    costs = [0 for _ in range(maxNum + 1)]
    for n in inp:
        for i in range(len(costs)):
            costs[i] += int(((abs(n - i) * (abs(n - i) + 1)) / 2))
    print(min(costs))