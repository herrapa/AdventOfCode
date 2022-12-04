with open("inputs/input4.txt", encoding="utf8") as infile:
    sum = 0
    for line in infile:
        line = line.strip().replace("-", ",")
        a, b, x, y = [int(x) for x in line.split(",")]
        first_set = set(range(a, b + 1))
        second_set = set(range(x, y + 1))
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            sum += 1

    print(sum)
