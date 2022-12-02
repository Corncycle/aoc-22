import util

data = util.parseFileAs("./inputs/d2.txt", str)

out = 0
for i, val in enumerate(data):
    spl = val.split()
    spl[1] = 1 if spl[1] == "X" else 2 if spl[1] == "Y" else 3
    spl[0] = 1 if spl[0] == "A" else 2 if spl[0] == "B" else 3
    if (spl[1] - spl[0] % 3) == 1:
        out += 6
    elif spl[1] == spl[0]:
        out += 3
    out += spl[1]

print(out)    

data = util.parseFileAs("./inputs/d2.txt", str)
out = 0
for i, val in enumerate(data):
    spl = val.split()
    spl[1] = 1 if spl[1] == "X" else 2 if spl[1] == "Y" else 3
    spl[0] = 1 if spl[0] == "A" else 2 if spl[0] == "B" else 3
    if spl[1] == 3:
        temp = spl[0] + 1
        temp = 1 if temp == 4 else temp
        out += temp
        out += 6
    elif spl[1] == 2:
        out += spl[0]
        out += 3
    else:
        temp = spl[0] - 1
        temp = 3 if temp == 0 else temp
        out += temp

print(out)