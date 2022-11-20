with open("inputs/input10.txt", encoding="utf8") as infile:
    
    brackets = {"(" : ")", "[" : "]", "{" : "}", "<" : ">"}
    points = {")" : 1, "]" : 2, "}" : 3, ">" : 4}
    sums = []
    for line in infile:
        stack = []
        line = line.strip()
        broken = False
        for char in list(line):
            if char in brackets.keys():
                stack.append(char)
            elif char in brackets.values():
                popped = stack.pop()
                if brackets[popped] != char:
                    broken = True
                    break
        if not broken:
            lineSum = 0
            stack.reverse()
            for char in stack:
                lineSum *= 5
                lineSum += points[brackets[char]]
            sums.append(lineSum)
    sums.sort()
    middle = float(len(sums)) / 2
    print(sums[int(middle - .5)])
