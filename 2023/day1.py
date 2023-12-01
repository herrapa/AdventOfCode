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
        if len(nums) > 0:
            sum += int(nums[0] + nums[-1])
    print(sum)

import re

words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
with open("inputs/input1.txt", encoding="utf8") as infile:
    sum = 0
    for line in infile:
        line = line.strip()
        nums = [None] * len(line)
        for i, char in enumerate(line):
            try:
                val = int(char)
                nums[i] = char
            except:
                continue
        for i, word in enumerate(words):
            indexes = [m.start() for m in re.finditer(word, line)]
            for index in indexes:
                nums[index] = str(i + 1)
        nums = [x for x in nums if x is not None]
        sum += int(nums[0] + nums[-1])
    print(sum)
