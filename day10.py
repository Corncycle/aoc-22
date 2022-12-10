import util
from collections import deque

data = util.parseFileAs("./inputs/d10.txt", str)

def recentTwenty(x):
    return x - (x % 20)

def meetsCondition(x):
    if x <= 220:
        if x % 40 == 20:
            return True
    return False

out = 0
sigs = []
x = 1
cycles = 0
cycleCounter = 0
for i, val in enumerate(data):
    if " " in val:
        cycles += 2
        cycleCounter += 2
        if cycleCounter >= 20:
            cycleCounter = cycleCounter % 20
            if meetsCondition(recentTwenty(cycles)):
                sigs.append(x * recentTwenty(cycles))
        data[i] = val.split(" ")
        data[i][1] = int(data[i][1])
        x += data[i][1]
    else:
        cycles += 1
        cycleCounter += 1
        if cycleCounter >= 20:
            cycleCounter = cycleCounter % 20
            if meetsCondition(recentTwenty(cycles)):
                sigs.append(x * recentTwenty(cycles))

print(sum(sigs))
print()

crtPointer = 0
currScreen = []
screen = [currScreen]

d = deque(data)
mustWait = False
preparedMove = None
spriteX = 1

for i in range(240):
    if crtPointer - 1 <= spriteX <= 1 + crtPointer:
        screen[-1].append("#")
    else:
        screen[-1].append(".")
    crtPointer += 1
    if crtPointer == 40:
        screen.append([])
    crtPointer = crtPointer % 40
    if mustWait:
        mustWait = False
        spriteX += preparedMove
    else:
        op = d.popleft()
        if len(op) == 2:
            mustWait = True
            preparedMove = op[1]

for l in screen:
    print("".join(l))