import util
from collections import deque

data = util.parseFileAs("./inputs/d12.txt", str)

out = 0
heights = []
start, end = None, None

for i, val in enumerate(data):
    heights.append([])
    for j, c in enumerate(val):
        if c == "S":
            heights[i].append(0)
            start = (i, j)
        elif c == "E":
            heights[i].append(26)
            end = (i, j)
        else:
            heights[i].append(util.charToNum(c))

def isInBounds(i, j):
    return 0 <= i < len(heights) and 0 <= j < len(heights[0])

def sum(a, b):
    return (a[0] + b[0], a[1] + b[1])

frontier = deque([start])
visited = set([start])

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
steps = 0

while not (end in frontier):
    steps += 1
    newFrontier = []
    for pos in frontier:
        visited.add(pos)
        for dir in dirs:
            dest = sum(pos, dir)
            if isInBounds(*dest) and heights[dest[0]][dest[1]] <= heights[pos[0]][pos[1]] + 1:
                if not (dest in visited) and not (dest in newFrontier) and heights[dest[0]]:
                    newFrontier.append(dest)
    frontier = newFrontier

print(steps)