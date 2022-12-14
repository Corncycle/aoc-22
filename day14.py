import util

data = util.parseFileAs("./inputs/d14.txt", str)

out = 0
xBounds = [1000, 0]
yBounds = [0, 0]
for i, val in enumerate(data):
    data[i] = val.split(" -> ")
    for j, v in enumerate(data[i]):
        data[i][j] = v.split(",")
        for k in range(2):
            data[i][j][k] = int(data[i][j][k])
        xBounds[0] = min(data[i][j][0], xBounds[0])
        xBounds[1] = max(data[i][j][0], xBounds[1])
        yBounds[0] = min(data[i][j][1], yBounds[0])
        yBounds[1] = max(data[i][j][1], yBounds[1])

grid = []
for i in range(yBounds[1] + 1):
    grid.append([])
    for j in range(xBounds[1] + 1):
        grid[i].append(".")

for i, li in enumerate(data):
    for j in range(len(li) - 1):
        if li[j][0] == li[j + 1][0]:
            start = min(li[j][1], li[j+1][1])
            stop = max(li[j][1], li[j+1][1])
            for k in range(start, stop + 1):
                grid[k][li[j][0]] = "#"
        elif li[j][1] == li[j + 1][1]:
            start = min(li[j][0], li[j+1][0])
            stop = max(li[j][0], li[j+1][0])
            for k in range(start, stop + 1):
                grid[li[j][1]][k] = "#"
            pass
        else:
            print("this shouldnt happen")

def printGrid():
    for level in grid:
        print("".join(level[xBounds[0]:]))

def dropSand(grid):
    currX = 500
    currY = 0
    while True:
        if currX < xBounds[0] or currX > xBounds[1] or currY < yBounds[0] or currY >= yBounds[1]:
            return False
        if grid[currY + 1][currX] == ".":
            currY += 1
            continue
        if currX - 1 < xBounds[0]:
            return False
        if grid[currY + 1][currX - 1] == ".":
            currY += 1
            currX -= 1
            continue
        if currX + 1 > xBounds[1]:
            return False
        elif grid[currY + 1][currX + 1] == ".":
            currY += 1
            currX += 1
            continue
        grid[currY][currX] = "o"
        return True

def countSand():
    out = 0
    for line in grid:
        out += line.count("o")
    return out

while dropSand(grid):
    True

print(countSand())