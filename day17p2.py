import util

data = util.parseFileAs("./inputs/d17.txt", str)

moveString = data[0]

def makePiece(blockTracker, height):
    if blockTracker == 0:
        return set([(2, height), (3, height), (4, height), (5, height)])
    elif blockTracker == 1:
        return set([(3, height), (2, height + 1), (3, height + 1), (4, height + 1), (3, height + 2)])
    elif blockTracker == 2:
        return set([(2, height), (3, height), (4, height), (4, height + 1), (4, height + 2)])
    elif blockTracker == 3:
        return set([(2, height), (2, height + 1), (2, height + 2), (2, height + 3)])
    elif blockTracker == 4:
        return set([(2, height), (3, height), (2, height + 1), (3, height + 1)])
    else:
        print("this shouldn't happen")
    
def moveLeft(piece):
    if any([x == 0 for (x, y) in piece]):
        return piece
    return set([(x - 1, y) for (x, y) in piece])

def moveRight(piece):
    if any([x == 6 for (x, y) in piece]):
        return piece
    return set([(x + 1, y) for (x, y) in piece])

def moveDown(piece):
    return set([(x, y - 1) for (x, y) in piece])

def moveUp(piece):
    return set([(x, y + 1) for (x, y) in piece])

def getMaxHeight(board):
    return max(board, key=lambda piece: piece[1])[1]

def printBoard(board):
    maxHeight = getMaxHeight(board)
    for y in reversed(range(maxHeight + 1)):
        print("".join(["#" if (x, y) in board else "." for x in range(7)]))

def signature(board):
    maxHeight = getMaxHeight(board)
    return frozenset([(x, maxHeight - y) for (x, y) in board if y >= maxHeight - 30])

board = set([(x, 0) for x in range(7)])

blockTracker = 0
strIndex = 0
visited = {}
limit = 1_000_000_000_000
simulated = 0
doneSimulation = False
while blockTracker < limit:
    piece = makePiece(blockTracker % 5, getMaxHeight(board) + 4)
    while True:
        if moveString[strIndex] == ">":
            newPiece = moveRight(piece)
        else:
            newPiece = moveLeft(piece)
        strIndex = (strIndex + 1) % len(moveString)
        if not board.intersection(newPiece):
            piece = newPiece
        piece = moveDown(piece)
        if board.intersection(piece):
            board.update(moveUp(piece))

            state = (strIndex, blockTracker % 5, signature(board))
            if state in visited and not doneSimulation:
                (oldBlockTracker, oldHeight) = visited[state]
                dHeight = getMaxHeight(board) - oldHeight
                dBlocks = blockTracker - oldBlockTracker
                numSimulatedCycles = (limit - blockTracker) // dBlocks
                simulated = numSimulatedCycles * dHeight
                blockTracker += numSimulatedCycles * dBlocks
                doneSimulation = True
            visited[state] = (blockTracker, getMaxHeight(board))
            break
    blockTracker += 1

print(getMaxHeight(board) + simulated)