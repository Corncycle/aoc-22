import util

data = util.parseFileAs("./inputs/d8.txt", str)

out = 0
grid = []
for i, val in enumerate(data):
    grid.append([])
    for c in val:
        grid[i].append(int(c))

def access(l, i):
    if i < 0 or i >= len(l):
        return 0
    else:
        return l[i]

def isVisible(grid, i, j):
    left = [grid[i][jj] < grid[i][j] for jj in range(0, j)]
    right = [grid[i][jj] < grid[i][j] for jj in range(j + 1, len(grid[0]))]
    up = [grid[ii][j] < grid[i][j] for ii in range(0, i)]
    down = [grid[ii][j] < grid[i][j] for ii in range(i + 1, len(grid))]
    return (all(left) or all(right) or all(up) or all(down)) or (not left or not right or not up or not down)

out = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if isVisible(grid, i, j):
            out += 1

print(out)

def getScenicScore(grid, i, j):
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    scores = []
    for dir in dirs:
        curri, currj, count = i + dir[0], j + dir[1], 0
        while 0 <= curri < len(grid) and 0 <= currj < len(grid[0]):
            count += 1
            if grid[i][j] <= grid[curri][currj]:
                break
            curri, currj = curri + dir[0], currj + dir[1]
        scores.append(count)
    prod = 1
    for val in scores:
        prod *= val
    return prod

scores = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        scores.append(getScenicScore(grid, i, j))
        
print(max(scores))