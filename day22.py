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

def leftmost(tiles, row):
    r = [tile for tile in tiles if tile[1] == row]
    return min(r, key = lambda tile: tile[0])

def rightmost(tiles, row):
    r = [tile for tile in tiles if tile[1] == row]
    return max(r, key = lambda tile: tile[0])

def topmost(tiles, col):
    c = [tile for tile in tiles if tile[0] == col]
    return min(c, key = lambda tile: tile[1])

def botmost(tiles, col):
    c = [tile for tile in tiles if tile[0] == col]
    return max(c, key = lambda tile: tile[1])

def sum(a, b):
    return (a[0] + b[0], a[1] + b[1])

def nextStep(tiles, pos, dir):
    tentdest = sum(pos, dir)
    hack1 = (tentdest[0], tentdest[1], 0)
    hack2 = (tentdest[0], tentdest[1], 1)
    if hack1 not in tiles and hack2 not in tiles:
        if dir == (1, 0):
            tentdest = leftmost(tiles, pos[1])
        elif dir == (0, 1):
            tentdest = topmost(tiles, pos[0])
        elif dir == (-1, 0):
            tentdest = rightmost(tiles, pos[1])
        elif dir == (0, -1):
            tentdest = botmost(tiles, pos[0])
        else:
            assert False
    else:
        tentdest = hack1 if hack1 in tiles else hack2
    return tentdest if tentdest[2] == 0 else False

def getEnd(tiles, instr):
    topRow = [tile for tile in tiles if tile[1] == 1 and tile[2] == 0]
    firstTile = sorted(topRow)[0]
    pos = (firstTile[0], firstTile[1])
    dir = (1, 0)
    i = 0
    while i < len(instr):
        #print(f"pos: {pos}, dir: {dir}")
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
            while j < moveLength:
                res = nextStep(tiles, pos, dir)
                if res:
                    #print(f"lets move to {res}")
                    pos = (res[0], res[1])
                else:
                    break
                j += 1
    di = {(1, 0): 0, (0, 1): 1, (-1, 0): 2, (0, -1): 3}
    print(1000 * pos[1] + 4 * pos[0] + di[dir])

getEnd(tiles, instr)