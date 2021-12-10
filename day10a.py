with open("inputs/input10.txt", encoding="utf8") as infile:
    
    brackets = {"(" : ")", "[" : "]", "{" : "}", "<" : ">"}
    points = {")" : 3, "]" : 57, "}" : 1197, ">" : 25137}
    sum = 0
    for line in infile:
        stack = []
        line = line.strip()
        for char in list(line):
            if char in brackets.keys():
                stack.append(char)
            elif char in brackets.values():
                popped = stack.pop()
                if brackets[popped] != char:
                    print("Expected: ", brackets[popped], "found: ", char)
                    sum += points[char]
                    break
    print(sum)