import util
import ast
import functools

data = util.parseFileAs("./inputs/d13.txt", str)

out = 0

def parse(s):
    return ast.literal_eval(s)

# 1 right order, -1 not
def compare(a, b):
    if a == [] and b == []:
        return 0
    if not a:
        return 1
    if not b:
        return -1
    if type(a[0]) == int and type(b[0]) == int:
        if a[0] < b[0]:
            return 1
        elif a[0] > b[0]:
            return -1
        else:
            ar = a[1:]
            br = b[1:]
            return compare(ar, br)
    if type(a[0]) == list and type(b[0]) == list:
        info = compare(a[0], b[0])
        if info != 0:
            return info
        else:
            ar = a[1:]
            br = b[1:]
            return compare(ar, br)
    if type(a[0]) == int:
        ar = a.copy()
        ar[0] = [ar[0]]
        return compare(ar, b)
    br = b.copy()
    br[0] = [br[0]]
    return compare(a, br)

for i, val in enumerate(data):
    if i % 3 == 0:
        index = (i // 3) + 1
        l1 = parse(data[i])
        l2 = parse(data[i + 1])
        if compare(l1, l2) == 1:
            out += index
print(out)

packets = [[[2]], [[6]]]
for i, val in enumerate(data):
    if val != "":
        packets.append(parse(val))

sor = sorted(packets, key=functools.cmp_to_key(lambda a, b: compare(a, b)), reverse=True)

out = 1
for i, val in enumerate(sor):
    if val == [[2]] or val == [[6]]:
        out *= (i + 1)

print(out)