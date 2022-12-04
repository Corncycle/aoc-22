import util

data = util.parseFileAs("./inputs/d4.txt", str)

out = 0
for i, val in enumerate(data):
    ranges = val.split(",")
    for j in range(2):
        ranges[j] = ranges[j].split("-")
        for k in range(2):
            ranges[j][k] = int(ranges[j][k])
    if (ranges[0][0] <= ranges[1][0] and ranges[0][1] >= ranges[1][1]) or (ranges[1][0] <= ranges[0][0] and ranges[1][1] >= ranges[0][1]):
        out += 1
print(out)

data = util.parseFileAs("./inputs/d4.txt", str)

out = 0
for i, val in enumerate(data):
    ranges = val.split(",")
    for j in range(2):
        ranges[j] = ranges[j].split("-")
        for k in range(2):
            ranges[j][k] = int(ranges[j][k])
    if (ranges[0][0] < ranges[1][0] and ranges[0][1] >= ranges[1][0]) or (ranges[0][0] >= ranges[1][0] and ranges[0][0] <= ranges[1][1]):
        out += 1
print(out)