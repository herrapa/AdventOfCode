with open("inputs/input2.txt", encoding="utf8") as infile:
    score = 0
    # A = Rock, B = Paper, C = Scissors
    # X = Rock, Y = Paper, Z = Scissors
    winMap = {"A": "Y", "B": "Z", "C": "X"}
    loseMap = {"A": "Z", "C": "Y", "B": "X"}
    drawMap = {"A": "X", "B": "Y", "C": "Z"}
    handMap = {"X": loseMap, "Y": drawMap, "Z": winMap}
    scoreMap = {"X": 1, "Y": 2, "Z": 3}
    for line in infile:
        line = line.strip()
        theirHand, outCome = line.split()

        myHand = handMap[outCome][theirHand]

        score += scoreMap[myHand]
        if winMap[theirHand] == myHand:
            score += 6
        elif loseMap[theirHand] != myHand:
            score += 3
    print(score)
