with open("inputs/input2.txt", encoding="utf8") as infile:
    sum = 0
    maxColors = {"red" : 12, "green" : 13, "blue" : 14}
    for line in infile:
        line = line.strip()
        gameId, games = line.split(": ")
        gameId = int(gameId.split(" ")[1])
        games = games.split("; ")
        ok = True
        for game in games:
            draws = game.split(", ")
            for draw in draws:
                num, color = draw.split(" ")
                if int(num) > maxColors[color]:
                    ok = False
                    continue
        if ok:
            sum += gameId
    print(sum)

with open("inputs/input2.txt", encoding="utf8") as infile:
    sum = 0
    
    for line in infile:
        minColors = {"red" : 0, "green" : 0, "blue" : 0}
        line = line.strip()
        gameId, games = line.split(": ")
        games = games.split("; ")
        for game in games:
            draws = game.split(", ")
            for draw in draws:
                num, color = draw.split(" ")
                num = int(num)
                minColors[color] = max(minColors[color], num)
        power = 1
        for val in minColors.values():
            power *= val
        sum += power
    print(sum)