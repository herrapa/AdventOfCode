with open("inputs/input6.txt", encoding="utf8") as infile:
    inp = [int(x) for x in infile.readline().strip().split(",")]
    buckets = [0 for _ in range(9)]
    for n in inp:
        buckets[n] += 1
    for _ in range(256):
        numZeros = buckets[0]
        for i in range(len(buckets) - 1):
            buckets[i] = buckets[i + 1]
        buckets[6] += numZeros
        buckets[8] = numZeros

    print(sum(buckets))
