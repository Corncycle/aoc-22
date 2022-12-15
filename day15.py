import util

data = util.parseFileAs("./inputs/d15.txt", str)

sensors = set()
beacons = set()

out = 0
vals = []
for i, val in enumerate(data):
    newVal = []
    for ind in [2, 3, 8, 9]:
        newVal.append(int(val.split()[ind][2:].replace(",","").replace(":", "")))
    vals.append(newVal)
    sensors.add((newVal[0],newVal[1]))
    beacons.add((newVal[2], newVal[3]))

def dist(a):
    return abs(a[0] - a[2]) + abs(a[1] - a[3])

for val in vals:
    val.append(dist(val))

row = 2000000

forbids = set()
for val in vals:
    rad = val[4]
    dis = abs(val[1] - row)
    r = rad - dis if rad > dis else 0
    if r > 0:
        forbids.add(val[0])
        for i in range(r):
            if (val[0] + i + 1, row) not in beacons:
                forbids.add(val[0] + i + 1)
            if (val[0] - i - 1, row) not in beacons:
                forbids.add(val[0] - i - 1)

print(len(forbids))

bound = 4000000

def getBounds(val, x):
    rad = val[4]
    dis = abs(val[1] - x)
    r = rad - dis if rad > dis else -1
    if r >= 0:
        return (val[1] - r, val[1] + r)
    return None

def dista(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def part2():
    x = 0
    y = 0
    while x < bound + 1:
        while y < bound + 1:
            failed = False
            for val in vals:
                badrad = dista((val[0], val[1]), (x, y))
                if badrad <= val[4]:
                    failed = True
                    badrad = val[4] - badrad
                    break
            if not failed:
                print(x * 4000000 + y)
                return
            else:
                y += badrad + 1
        x += 1
        y = 0

part2()