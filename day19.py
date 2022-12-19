import util
import functools

data = util.parseFileAs("./inputs/d19.txt", str)

out = 0

bps = []
for i, val in enumerate(data):
    v = val.split()
    data = (v[6], v[12], v[18], v[21], v[27], v[30])
    data = tuple([int(c) for c in data])
    maxOres = max(data[0], data[1], data[2], data[4])
    data = data + (maxOres,)
    bps.append(data)

def incrementIndexBy(tup, i, amount):
    return tuple(val if j != i else val + amount for j, val in enumerate(tup))

def sumTups(a, b):
    return tuple(a[i] + b[i] for i in range(len(a)))

@functools.lru_cache(maxsize=None)
def helper(bots, mats, decisionsLeft, bp):
    if decisionsLeft == 1:
        return bots[3]
    matsAfterGen = sumTups(bots, mats)
    options = []
    if mats[0] >= bp[4] and mats[2] >= bp[5]:
        matsAfterCost = sumTups(matsAfterGen, (-1 * bp[4], 0, -1 * bp[5], 0))
        options.append(bots[3] + helper(incrementIndexBy(bots, 3, 1), matsAfterCost, decisionsLeft - 1, bp))
    if mats[0] >= bp[2] and mats[1] >= bp[3] and bots[2] < bp[5]:
        matsAfterCost = sumTups(matsAfterGen, (-1 * bp[2], -1 * bp[3], 0, 0))
        options.append(bots[3] + helper(incrementIndexBy(bots, 2, 1), matsAfterCost, decisionsLeft - 1, bp))
    if mats[0] >= bp[1] and bots[1] < bp[3]:
        matsAfterCost = sumTups(matsAfterGen, (-1 * bp[1], 0, 0, 0))
        options.append(bots[3] + helper(incrementIndexBy(bots, 1, 1), matsAfterCost, decisionsLeft - 1, bp))
    if mats[0] >= bp[0] and bots[0] < bp[-1]:
        matsAfterCost = sumTups(matsAfterGen, (-1 * bp[0], 0, 0, 0))
        options.append(bots[3] + helper(incrementIndexBy(bots, 0, 1), matsAfterCost, decisionsLeft - 1, bp))
    # heuristic: if we have enough ores to make any of the bots, we probably shouldn't do nothing
    if mats[0] < bp[-1]:
        options.append(bots[3] + helper(bots, matsAfterGen, decisionsLeft - 1, bp))
    return max(options)

def getBestByBlueprint(bp, totalTime):
    return helper((1, 0, 0, 0), (0, 0, 0, 0), totalTime, bp)

def main():
    out = 0
    for i, bp in enumerate(bps):
        out += (i + 1) * getBestByBlueprint(bp, 24)
    print(out)

    out = 1
    for i in range(3):
        res = getBestByBlueprint(bps[i], 32)
        out *= res
    print(out)


if __name__ == "__main__":
    main()