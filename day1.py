import util

data = util.parseFileAs("./inputs/input.txt", str)

currMax = 0
currHold = 0
for i, val in enumerate(data):
    if val == "":
        currMax = max(currMax, currHold)
        currHold = 0
    else:
        currHold += int(val)
print(currMax)

currHold = 0
holds = []
for i, val in enumerate(data):
    if val == "":
        holds.append(currHold)
        currHold = 0
    else:
        currHold += int(val)
holds = sorted(holds)
print(holds[-1] + holds[-2] + holds[-3])