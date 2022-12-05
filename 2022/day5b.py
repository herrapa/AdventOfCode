with open("inputs/input5.txt", encoding="utf8") as infile:
    stacks = dict()
    for line in infile:
        if "[" in line:
            for i, c in enumerate([line[idx] for idx in range(1, len(line), 4)]):
                if c == " ":
                    continue
                stack_id = str(i + 1)
                if stack_id not in stacks:
                    stacks[stack_id] = []
                stacks[stack_id].insert(0, c)
        if "move" in line:
            line = line.strip().replace("move ", "").replace("from ", "").replace("to ", "")
            nr, frm, to = line.split()
            nr = int(nr)
            tmp = []
            for _ in range(nr):
                tmp.insert(0, stacks[frm].pop())
            for c in tmp:
                stacks[to].append(c)
    keys = list(stacks.keys())
    keys.sort()
    print("".join([stacks[k][-1] for k in keys]))
