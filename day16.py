import util

'''The approach I used for part 2 is given by reddit user tymscar.
https://www.reddit.com/r/adventofcode/comments/zn6k1l/comment/j0gycs2/

Part 1 runs effectively instantly.
Part 2 takes about 2.5 minutes to run with pypy on my machine.
'''

data = util.parseFileAs("./inputs/d16.txt", str)

class Valve:
    def __init__(self, name, rate) -> None:
        self.name = name
        self.rate = rate
        self.neighbors = []
        self.allDistances = {}

valves = []

for i, val in enumerate(data):
    temp = val.split()
    name = temp[1]
    rate = temp[4][5:-1]
    valves.append(Valve(name, int(rate)))

lookupValves = {valve.name: valve for valve in valves}

for i, val in enumerate(data):
    temp = val.replace(",", "").split()
    name = temp[1]
    neighbors = temp[9:]
    v = lookupValves[name]
    for neigh in neighbors:
        v.neighbors.append((lookupValves[neigh], 1))

def fillOutDistances(valve):
    frontier = [valve]
    visited = [valve]
    dist = 0
    while frontier:
        dist += 1
        newFrontier = []
        for v in frontier:
            for neighborData in v.neighbors:
                if neighborData[0] not in visited and neighborData[0] not in newFrontier:
                    visited.append(neighborData[0])
                    newFrontier.append(neighborData[0])
                    valve.allDistances[neighborData[0].name] = dist
        frontier = newFrontier

def getDist(aName, bName):
    return lookupValves[aName].allDistances[bName]

nonzeros = []
for valve in valves:
    fillOutDistances(valve)
    if valve.rate != 0:
        nonzeros.append(valve)

def getAllPaths(curr, timeRemaining, visited):
    out = [[0]]
    for valve in nonzeros:
        v = valve.name
        if v != curr and v not in visited:
            dist = lookupValves[curr].allDistances[v]
            if dist + 1 < timeRemaining:
                smallerpaths = getAllPaths(v, timeRemaining - (dist + 1), [v] + visited)
                for path in smallerpaths:
                    out.append([v] + path)
    return out

def pathToPressure(path, totalTime):
    out = 0
    timeLeft = totalTime
    curr = "AA"
    for i in range(len(path)):
        next = path[i]
        timeLeft -= getDist(curr, next) + 1
        out += lookupValves[next].rate * timeLeft
        curr = next
    return out

totalTime = 30
paths = getAllPaths("AA", totalTime, [])
paths = [path[:-1] for path in paths]
pressures = [pathToPressure(path, totalTime) for path in paths]
print(max(pressures))

totalTime = 26
paths = getAllPaths("AA", totalTime, [])
paths = [path[:-1] for path in paths]
pressures = [pathToPressure(path, totalTime) for path in paths]
pathsPressures = zip(paths, pressures)

bestCombinedFound = 0
for path, pressure in zip(paths, pressures):
    # reasoning for if statement below:
    # its not possible for both you and the elephant to turn on more than half of the valves
    if len(path) <= len(nonzeros) / 2:
        for path2, pressure2 in zip(paths, pressures):
            if len(path2) <= len(nonzeros) - len(path):
                if set(path).isdisjoint(path2):
                    bestCombinedFound = max(bestCombinedFound, pressure + pressure2)
print(bestCombinedFound)