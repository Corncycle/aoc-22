import util

# this is the solution i wrote when the puzzle was released which solves part 1
#
# when trying to solve part 2, i realized my approach was too slow and i would
# have to try something different. then i watched jonathon paulson's solve
# video (https://www.youtube.com/watch?v=QXTBseFzkW4) and tried to recreate his
# approach on my own in d17p2.py

data = util.parseFileAs("./inputs/d17.txt", str)

out = 0
moveString = ""
for i, val in enumerate(data):
    moveString = val

rocks = []
rocks.append([[0, 0], [0, 1], [0, 2], [0, 3]])
rocks.append([[0, 1], [1, 0], [1, 1], [1, 2], [2, 1]])
rocks.append([[0, 0], [0, 1], [0, 2], [1, 2], [2, 2]])
rocks.append([[0, 0], [1, 0], [2, 0], [3, 0]])
rocks.append([[0, 0], [0, 1], [1, 0], [1, 1]])

def addOpenRow(li):
    li.append([0 for _ in range(7)])

def addPoints(a, b):
    return [a[0] + b[0], a[1] + b[1]]

def shouldStop(board, rock, BLpos):
    for coord in rock:
        rel = addPoints(coord, BLpos)
        if board[rel[0] - 1][rel[1]] == 1:
            return True
    return False

def getStackHeight(board):
    for i, level in enumerate(board):
        if 1 not in level:
            return i - 1

def isValid(board, pos):
    if pos[1] < 0 or pos[1] > 6:
        return False
    return board[pos[0]][pos[1]] == 0

def sidePush(board, rock, BLpos, dir):
    if dir == "<":
        offset = [0, -1]
    else:
        offset = [0, 1]
    for coord in rock:
        rel = addPoints(coord, BLpos)
        if not isValid(board, addPoints(rel, offset)):
            return BLpos
    return addPoints(BLpos, offset)

def dropRock(board, rock, moveString, startIndex):
    height = getStackHeight(board)
    if height == None or height > len(board) - 9:
        for _ in range(9):
            addOpenRow(board)
    BLpos = [height + 4, 2]
    currIndex = startIndex
    while True:
        BLpos = sidePush(board, rock, BLpos, moveString[currIndex])
        currIndex = (currIndex + 1) % len(moveString)
        if shouldStop(board, rock, BLpos):
            break
        BLpos[0] -= 1
    for coord in rock:
        rel = addPoints(coord, BLpos)
        board[rel[0]][rel[1]] = 1
    return currIndex

def printBoard(board):
    for level in reversed(board):
        print("".join(["#" if point == 1 else "." for point in level]))

# 0 free, 1 occupied
board = [[1, 1, 1, 1, 1, 1, 1]]

addOpenRow(board)
currIndex = 0
blockTracker = 0
for i in range(2022):
    currIndex = dropRock(board, rocks[blockTracker], moveString, currIndex)
    blockTracker = (blockTracker + 1) % 5
print(getStackHeight(board))