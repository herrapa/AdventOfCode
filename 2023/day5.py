import re

with open("inputs/input5.txt", encoding="utf8") as infile:
    sm = 0
    f = ""
    t = ""
    mappings = dict()
    for line in infile:
        line = line.strip()
        if "seeds:" in line:
            seeds = line.split(":")[1].strip()
            seeds = re.split(r"[ ]+", seeds)
            continue

        if len(line) == 0:
            continue
        if "-to-" in line:
            f, t = line.split(" ")[0].split("-to-")
            mappings[t] = dict()
            mappings[t]["to"] = f
            continue
        
        first, second, r = [int(x) for x in re.split(r"[ ]+", line)]
        for i in range(r):
            mappings[t][i + second] = i + first


    print(sm)
