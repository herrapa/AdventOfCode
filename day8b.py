with open("inputs/input8.txt", encoding="utf8") as infile:
    res = 0
    for line in infile:
        inp, out = [l.split() for l in line.strip().split(" | ")]
        mapping = dict()
        for c in range(ord("a"), ord("h")):
            mapping[chr(c)] = set(list("abcdefg"))
        one = None
        seven = None
        four = None
        for n in inp:
            l = len(n)
            ls = set(list(n))
            if l == 2: # 1
                one = ls
            elif l == 3: # 7
                seven = ls
            elif l == 4: # 4
                four = ls
        s = ""
        for n in out:
            l = len(n)
            nSet = set(list(n))
            if l == 2:
                s += "1"
            elif l == 3:
                s += "7"
            elif l == 4:
                s += "4"
            elif l == 7:
                s += "8"
            elif l == 6:
                if nSet.issuperset(four):
                    s += "9"
                elif nSet.issuperset(one):
                    s += "0"
                else:
                    s += "6"
            elif l == 5:
                if nSet.issuperset(one):
                    s += "3"
                elif nSet.issuperset(four.difference(one)):
                    s += "5"
                else:
                    s += "2"
            else:
                    print("No")
        res += int(s)
    print(res)
