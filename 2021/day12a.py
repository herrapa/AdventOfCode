
from curses.ascii import islower

nodes = {}

numPaths = 0

def findPath(path, visited):
    global numPaths
    #print("visiting: " + path)

    if path.islower():
        visited.add(path)

    if path == "end":
        numPaths += 1
    else:
        for nextPath in nodes[path]:
            if nextPath not in visited:
                findPath(nextPath, visited)

    if path in visited:
        visited.remove(path)

with open("inputs/input12.txt", encoding="utf8") as infile:
    
    nodes = {}
    for line in infile:
        start, end = line.strip().split("-")
        if nodes.get(start) == None:
            nodes[start] = []
        nodes[start].append(end)
        if nodes.get(end) == None:
            nodes[end] = []
        nodes[end].append(start)
    print(nodes)
    
    findPath("start", set())
    print(numPaths)
