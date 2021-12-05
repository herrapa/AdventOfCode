
def isBingo(num, mat):
    for row in mat:
        for numTuple in row:
            if numTuple[0] == num:
                numTuple[1] = True
        if all([i[1] for i in row]):
            return True
    for i in range(5):
        if all([row[i][1] for row in mat]):
            return True

mats = []
with open("inputs/input4.txt", encoding="utf8") as infile:
    numbers = [int(a) for a in infile.readline().strip().split(",")]
    currentMat = []
    for line in infile:
        line = line.strip()
        if len(line) == 0:
            if len(currentMat) == 0:
                continue
            mats.append(currentMat)
            currentMat = []
            continue
        row = [[int(a), False] for a in line.split()]
        currentMat.append(row)

for n in numbers:
    for mat in mats:
        if isBingo(n, mat):
            s = 0
            for row in mat:
                for num in row:
                    if num[1] == False:
                        s += num[0]
            print(s * n)
            exit(0)
