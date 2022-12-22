import util

data = util.parseFileAs("./inputs/d22.txt", str)

# 0 is available, 1 is solid wall
out = 0
i = 0
tiles = []
while data[i] != "":
    line = data[i]
    for j, ch in enumerate(line):
        if ch != " ":
            tiles.append((j + 1, i + 1, 0 if ch == "." else 1))
    i += 1
i += 1
instr = data[i]

def rotRight(dir):
    if dir == (1, 0):
        return (0, 1)
    elif dir == (0, 1):
        return (-1, 0)
    elif dir == (-1, 0):
        return (0, -1)
    elif dir == (0, -1):
        return (1, 0)
    else:
        assert False

def rotLeft(dir):
    if dir == (1, 0):
        return (0, -1)
    elif dir == (0, -1):
        return (-1, 0)
    elif dir == (-1, 0):
        return (0, 1)
    elif dir == (0, 1):
        return (1, 0)
    else:
        assert False

def sum(a, b):
    return (a[0] + b[0], a[1] + b[1])

def nextStepCrossesEdge(tiles, pos, dir):
    s = sum(pos, dir)
    hack1 = (s[0], s[1], 0)
    hack2 = (s[0], s[1], 1)
    return hack1 not in tiles and hack2 not in tiles

def nextStep(tiles, pos, dir):
    if not nextStepCrossesEdge(tiles, pos, dir):
        tentdest = sum(pos, dir)
        hack1 = (tentdest[0], tentdest[1], 0)
        return [hack1, dir] if hack1 in tiles else [False, False]
    if 51 <= pos[0] <= 100 and pos[1] == 1 and dir == (0, -1):
        dest = (1, pos[0] + 100, 0)
        return [dest, (1, 0)] if dest in tiles else [False, False]
    if 101 <= pos[0] <= 150 and pos[1] == 1 and dir == (0, -1):
        dest = (pos[0] - 100, 200, 0)
        return [dest, (0, -1)] if dest in tiles else [False, False]
    if 1 <= pos[1] <= 50 and pos[0] == 51 and dir == (-1, 0):
        dest = (1, 151 - pos[1], 0)
        return [dest, (1, 0)] if dest in tiles else [False, False]
    if 1 <= pos[1] <= 50 and pos[0] == 150 and dir == (1, 0):
        dest = (100, 151 - pos[1], 0)
        return [dest, (-1, 0)] if dest in tiles else [False, False]
    if 101 <= pos[0] <= 150 and pos[1] == 50 and dir == (0, 1):
        dest = (100, pos[0] - 50, 0)
        return [dest, (-1, 0)] if dest in tiles else [False, False]
    if 51 <= pos[1] <= 100 and pos[0] == 51 and dir == (-1, 0):
        dest = (pos[1] - 50, 101, 0)
        return [dest, (0, 1)] if dest in tiles else [False, False]
    if 51 <= pos[1] <= 100 and pos[0] == 100 and dir == (1, 0):
        dest = (pos[1] + 50, 50, 0)
        return [dest, (0, -1)] if dest in tiles else [False, False]
    if 1 <= pos[0] <= 50 and pos[1] == 101 and dir == (0, -1):
        dest = (51, pos[0] + 50, 0)
        return [dest, (1, 0)] if dest in tiles else [False, False]
    if 101 <= pos[1] <= 150 and pos[0] == 1 and dir == (-1, 0):
        dest = (51, 151 - pos[1], 0)
        return [dest, (1, 0)] if dest in tiles else [False, False]
    if 101 <= pos[1] <= 150 and pos[0] == 100 and dir == (1, 0):
        dest = (150, 151 - pos[1], 0)
        return [dest, (-1, 0)] if dest in tiles else [False, False]
    if 51 <= pos[0] <= 100 and pos[1] == 150 and dir == (0, 1):
        dest = (50, 100 + pos[0], 0)
        return [dest, (-1, 0)] if dest in tiles else [False, False]
    if 151 <= pos[1] <= 200 and pos[0] == 1 and dir == (-1, 0):
        dest = (pos[1] - 100, 1, 0)
        return [dest, (0, 1)] if dest in tiles else [False, False]
    if 151 <= pos[1] <= 200 and pos[0] == 50 and dir == (1, 0):
        dest = (pos[1] - 100, 150, 0)
        return [dest, (0, -1)] if dest in tiles else [False, False]
    if 1 <= pos[0] <= 50 and pos[1] == 200 and dir == (0, 1):
        dest = (pos[0] + 100, 1, 0)
        return [dest, (0, 1)] if dest in tiles else [False, False]
    assert False
    
def getEnd(tiles, instr):
    topRow = [tile for tile in tiles if tile[1] == 1 and tile[2] == 0]
    firstTile = sorted(topRow)[0]
    pos = (firstTile[0], firstTile[1])
    dir = (1, 0)
    i = 0
    while i < len(instr):
        if instr[i] == "R":
            dir = rotRight(dir)
            i += 1
        elif instr[i] == "L":
            dir = rotLeft(dir)
            i += 1
        else:
            moveLength = ""
            while i < len(instr) and instr[i] != "R" and instr[i] != "L":
                moveLength = moveLength + instr[i]
                i += 1
            moveLength = int(moveLength)
            j = 0
            #print(f"(moved {moveLength})")
            while j < moveLength:
                res, resDir = nextStep(tiles, pos, dir)
                if res:
                    #print(f"lets move to {res}")
                    pos = (res[0], res[1])
                    dir = resDir
                else:
                    break
                j += 1
    #print(f"end at {pos}, {dir}")
    di = {(1, 0): 0, (0, 1): 1, (-1, 0): 2, (0, -1): 3}
    print(1000 * pos[1] + 4 * pos[0] + di[dir])

def getMapString(tiles):
    with open("./inputs/mapstring.txt") as mf:
        out = []
        for line in mf:
            for ch in line:
                out.append(ch)
        return out

def printMap(ms, pos, dir):
    if dir == (1, 0):
        ch = ">"
    elif dir == (0, 1):
        ch = "v"
    elif dir == (-1, 0):
        ch = "<"
    else:
        ch = "^"
    m = ms.copy()
    m[151 * (pos[1] - 1) + (pos[0] - 1)] = ch
    print("".join(m))

ms = getMapString(tiles)

getEnd(tiles, instr)