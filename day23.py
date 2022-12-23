import util
from collections import defaultdict

data = util.parseFileAs("./inputs/d23.txt", str)

out = 0

elves = set()
for i, val in enumerate(data):
    for j, c in enumerate(val):
        if c == "#":
            elves.add((i, j))

def proposeStep(elves, dir, pos):
    init = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    initCheck = set([util.tupsum(pos, offset) for offset in init])
    if not elves & initCheck:
        return pos
    if dir == "N":
        offsets = [(-1, 0), (-1, -1), (-1, 1)]
    elif dir == "S":
        offsets = [(1, 0), (1, -1), (1, 1)]
    elif dir == "W":
        offsets = [(0, -1), (-1, -1), (1, -1)]
    elif dir == "E":
        offsets = [(0, 1), (-1, 1), (1, 1)]
    else:
        assert False
    check = set([util.tupsum(pos, offset) for offset in offsets])
    if not elves & check:
        if dir == "N":
            return util.tupsum(pos, (-1, 0))
        elif dir == "S":
            return util.tupsum(pos, (1, 0))
        elif dir == "W":
            return util.tupsum(pos, (0, -1))
        else:
            return util.tupsum(pos, (0, 1))
    return pos

def printElves(elves):
    minX = min([x for x, y in elves])
    maxX = max([x for x, y in elves])
    minY = min([y for x, y in elves])
    maxY = max([y for x, y in elves])
    for i in range(minX, maxX + 1):
        line = []
        for j in range(minY, maxY + 1):
            if (i, j) in elves:
                line.append("#")
            else:
                line.append(".")
        print("".join(line))
    print()

def iterate(elves, order):
    proposed = defaultdict(list)
    for pos in elves:
        foundMove = False
        for dir in order:
            prop = proposeStep(elves, dir, pos)
            if prop != pos:
                proposed[prop].append(pos)
                foundMove = True
                break
        if not foundMove:
            proposed[pos].append(pos)

    nextElves = set()
    for pos in proposed:
        if len(proposed[pos]) == 1:
            nextElves.add(pos)
        else:
            for elf in proposed[pos]:
                nextElves.add(elf)
    return nextElves

dirs = ["N", "S", "W", "E"]
i = 0
while True:
    if i == 10:
        # this is cringe, coords are stored in i, j not x, y (i vertical)
        minX = min([x for x, y in elves])
        maxX = max([x for x, y in elves])
        minY = min([y for x, y in elves])
        maxY = max([y for x, y in elves])
        print((maxX - minX + 1) * (maxY - minY + 1) - len(elves))
    prevRound = elves
    elves = iterate(elves, dirs)
    if (prevRound == elves):
        print(i + 1)
        break
    a = dirs.pop(0)
    dirs.append(a)
    i += 1