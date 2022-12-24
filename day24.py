import util

# this solution runs pretty slow, run with pypy for it to complete in any decent time
data = util.parseFileAs("./inputs/d24.txt", str)

out = 0
blizz = set()
for y, val in enumerate(data):
    for x, ch in enumerate(val):
        if ch != "." and ch != "#":
            blizz.add((x, y, ch))

xMin, yMin = 0, 0
xMax = max(x for x, y, ch in blizz) + 1
yMax = max(y for x, y, ch in blizz) + 1

def getNaiveNext(bl):
    if bl[2] == ">":
        return util.tupsum(bl, (1, 0, ""))
    elif bl[2] == "<":
        return util.tupsum(bl, (-1, 0, ""))
    elif bl[2] == "^":
        return util.tupsum(bl, (0, -1, ""))
    elif bl[2] == "v":
        return util.tupsum(bl, (0, 1, ""))
    assert False

def iterateBlizz(blizz):
    newBlizz = set()
    for bl in blizz:
        ne = getNaiveNext(bl)
        if ne[0] == xMin:
            ne = (xMax - 1, ne[1], ne[2])
        elif ne[0] == xMax:
            ne = (xMin + 1, ne[1], ne[2])
        elif ne[1] == yMin:
            ne = (ne[0], yMax - 1, ne[2])
        elif ne[1] == yMax:
            ne = (ne[0], yMin + 1, ne[2])
        newBlizz.add(ne)
    return newBlizz

def getNeighbors(pos):
    opts = [(pos[0], pos[1]), (pos[0]+1, pos[1]), (pos[0]-1, pos[1]), (pos[0], pos[1]+1), (pos[0], pos[1]-1)]
    return [opt for opt in opts if (xMin < opt[0] < xMax and yMin < opt[1] < yMax) or (opt == (1, 0)) or (opt == (xMax - 1, yMax))]


def doStep(validPositions, blizz):
    nextValid = set()
    nextBlizz = iterateBlizz(blizz)
    for pos in validPositions:
        neighs = getNeighbors(pos)
        for neigh in neighs:
            if any([(bl[0], bl[1]) == neigh for bl in nextBlizz]):
                continue
            nextValid.add(neigh)
    return nextValid, nextBlizz

validPositions = set([(1, 0)])
counter = 0
segment = 0
while True:
    counter += 1
    validPositions, blizz = doStep(validPositions, blizz)
    if (xMax - 1, yMax) in validPositions and segment == 0:
        validPositions = set([(xMax - 1, yMax)])
        print(counter)
        segment += 1
    if (1, 0) in validPositions and segment == 1:
        validPositions = set([(1, 0)])
        segment += 1
    if (xMax - 1, yMax) in validPositions and segment == 2:
        print(counter)
        break