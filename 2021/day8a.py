with open("inputs/input8.txt", encoding="utf8") as infile:
    res = 0
    for line in infile:
        inp, out = [l.split() for l in line.strip().split(" | ")]
        for n in out:
            l = len(n)
            if l == 2 or l == 3 or l == 4 or l == 7:
                res += 1
    print(res)
