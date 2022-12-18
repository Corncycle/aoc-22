import util

data = util.parseFileAs("./inputs/d18.txt", str)

out = 0
drops = set()
for i, val in enumerate(data):
    v = [int(entry) for entry in val.split(",")]
    drops.add((v[0], v[1], v[2]))

def sum(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])

def getSides(drops, drop):
    disp = set([(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)])
    out = 0
    for d in disp:
        neigh = sum(d, drop)
        if neigh not in drops:
            out += 1
    return out

tout = 0
for drop in drops:
    tout += getSides(drops, drop)

print(tout)

minx = min(x for x, y, z in drops)
miny = min(y for x, y, z in drops)
minz = min(z for x, y, z in drops)
maxx = max(x for x, y, z in drops)
maxy = max(y for x, y, z in drops)
maxz = max(z for x, y, z in drops)

openAir = set([(minx-1, miny-1, minz-1)])
frontier = openAir.copy()

def getNeighbors(loc):
    disp = set([(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)])
    out = []
    for d in disp:
        neigh = sum(d, loc)
        if minx - 1 <= neigh[0] <= maxx + 1 and miny - 1 <= neigh[1] <= maxy + 1 and minz - 1 <= neigh[2] <= maxz + 1:
            out.append(neigh)
    return out

while frontier:
    newFrontier = []
    for loc in frontier:
        neighs = getNeighbors(loc)
        for neigh in neighs:
            if neigh not in drops and neigh not in openAir and neigh not in newFrontier and neigh not in frontier:
                openAir.add(neigh)
                newFrontier.append(neigh)
    frontier = newFrontier

tout = 0
for loc in openAir:
    tout += getSides(openAir, loc)

dx = maxx - minx + 3
dy = maxy - miny + 3
dz = maxz - minz + 3
print(tout - 2 * (dx * dy + dy * dz + dz * dx))