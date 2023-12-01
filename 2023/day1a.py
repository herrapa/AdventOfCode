with open("inputs/input1.txt", encoding="utf8") as infile:
    sum = 0
    for line in infile:
        line = line.strip()
        nums = []
        for char in line:
            try:
                i = int(char)
                if i is not None:
                    nums.append(char)
            except:
                continue
        sum += int(nums[0] + nums[-1])
    print(sum)
