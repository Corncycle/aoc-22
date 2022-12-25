import util

data = util.parseFileAs("./inputs/d25.txt", str)

def toDecimal(s):
    out = 0
    for i in reversed(range(len(s))):
        pow = len(s) - 1 - i
        if s[i] == "-":
            out += -1 * (5 ** pow)
        elif s[i] == "=":
            out += -2 * (5 ** pow)
        else:
            out += int(s[i]) * (5 ** pow)
    return out

def toSnafu(n):
    out = ""
    curr = n
    while curr:
        last = curr % 5
        if last <= 2:
            out = str(last) + out
        elif last == 3:
            out = "=" + out
            curr += 2
        else:
            out = "-" + out
            curr += 1
        curr = curr // 5
    return out

out = 0
for i, val in enumerate(data):
    out += toDecimal(val)

print(toSnafu(out))