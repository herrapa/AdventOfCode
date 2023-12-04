import re

with open("inputs/input4.txt", encoding="utf8") as infile:
    sm = 0
    for line in infile:
        line = line.strip()
        left, right = line.split(" | ")
        left = left.split(": ")[1].strip()
        left = re.split(r"[ ]+", left)
        right = right.strip()
        right = re.split(r"[ ]+", right)
        left_set = set(left)
        right_set = set(right)
        cross = left_set.intersection(right_set)
        if len(cross) > 0:
            points = pow(2, len(cross) - 1)
            sm += points

    print(sm)

with open("inputs/input4.txt", encoding="utf8") as infile:
    idx = 0
    cards = dict()
    for line in infile:
        line = line.strip()
        left, right = line.split(" | ")
        left = left.split(": ")[1].strip()
        left = re.split(r"[ ]+", left)
        right = right.strip()
        right = re.split(r"[ ]+", right)
        left_set = set(left)
        right_set = set(right)
        cross = left_set.intersection(right_set)

        if len(cross) > 0:
            copies = cards.get(idx, 0)
            cards[idx] = cards.get(idx, 0) + 1
            for h in range(cards.get(idx, 0) + 0):
                for i in range(idx + 1, idx + len(cross) + 1):
                    cards[i] = cards.get(i, 0) + 1
        else:
            cards[idx] = cards.get(idx, 0) + 1
        idx += 1

    print(sum(cards.values()))