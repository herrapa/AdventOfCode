with open("inputs/input2.txt", encoding="utf8") as infile:
    score = 0
    # A = Rock, B = Paper, C = Scissors
    # X = Rock, Y = Paper, Z = Scissors
    winMap = {"X": "C", "Z": "B", "Y": "A"}
    loseMap = {"A": "Z", "C": "Y", "B": "X"}
    scoreMap = {"X": 1, "Y": 2, "Z": 3}
    for line in infile:
        line = line.strip()
        theirHand, myHand = line.split()
        score += scoreMap[myHand]
        if winMap[myHand] == theirHand:
            score += 6
        elif loseMap[theirHand] != myHand:
            score += 3
    print(score)
