# holy cow this code is so bad

import util

data = util.parseFileAs("./inputs/d9.txt", str)

out = 0
for i, val in enumerate(data):
    data[i] = val.split()
    data[i][1] = int(data[i][1])

head = (0, 0)
tail = (0, 0)
visited = set()
dirs = {"D": (1, 0), "U": (-1, 0), "R": (0, 1), "L": (0, -1)}

def sum(a, b):
    return (a[0] + b[0], a[1] + b[1])

def moveHead(move):
    global head
    global tail
    global visited
    for _ in range(move[1]):
        moveHeadSingle(move[0])

def moveHeadSingle(dir):
    global head
    global tail
    global visited
    head = sum(head, dirs[dir])
    if dist(head, tail) > 1:
        delta = (head[0] - tail[0], head[1] - tail[1])
        newDelta = [0, 0]
        if abs(delta[0]) < 2:
            newDelta[0] = 0
        else:
            newDelta[0] = 1 if delta[0] == 2 else -1
        if abs(delta[1]) < 2:
            newDelta[1] = 0
        else:
            newDelta[1] = 1 if delta[1] == 2 else -1
        tail = (head[0] - newDelta[0], head[1] - newDelta[1])
        visited.add(tail)


def dist(h, t):
    return max(abs(h[0] - t[0]), abs(h[1] - t[1]))

def size(delta):
    return max(abs(delta[0]), abs(delta[1]))

visited.add(tail)
for i, val in enumerate(data):
    moveHead(val)

print(len(visited))

dirs = {"D": (1, 0), "U": (-1, 0), "R": (0, 1), "L": (0, -1), "DR": (1, 1), "DL": (1, -1), "UR": (-1, 1), "UL": (-1, -1)}
rdirs = {v:k for (k,v) in dirs.items()}

def newDir(head, tail):
    delta = (head[0] - tail[0], head[1] - tail[1])
    if size(delta) < 2:
        return (0, 0)
    xdel = delta[0]
    ydel = delta[1]
    if abs(delta[0]) == 2:
        xdel = 1 if delta[0] == 2 else -1
    if abs(delta[1]) == 2:
        ydel = 1 if delta[1] == 2 else -1
    return (xdel, ydel)

class Node:
    def __init__(self, loc, pos) -> None:
        self.loc = loc
        self.child = None
        self.visited = set()
        self.visited.add(loc)
        self.pos = pos

    def moveSingle(self, dir):
        self.loc = sum(self.loc, dirs[dir])
        self.visited.add(self.loc)
        if self.child:
            ndir = newDir(self.loc, self.child.loc)
            if ndir != (0, 0):
                self.child.moveSingle(rdirs[ndir])

    def move(self, move):
        for _ in range(move[1]):
            self.moveSingle(move[0])

chainHead = Node((0, 0), 0)
curr = chainHead
for i in range(9):
    next = Node((0, 0), i + 1)
    curr.child = next
    curr = next

for i, val in enumerate(data):
    chainHead.move(val)

curr = chainHead
while curr.child:
    curr = curr.child

print(len(curr.visited))