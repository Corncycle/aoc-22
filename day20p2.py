import util

data = util.parseFileAs("./inputs/d20.txt", int)

class Node:
    def __init__(self, val) -> None:
        self.val = val

    def __repr__(self) -> str:
        return str(self.val)

out = 0
indices = []
vals = []
for i, val in enumerate(data):
    n = Node(val * 811589153)
    indices.append(n)
    vals.append(n)

l = len(vals)
for j in range(10):
    for i, node in enumerate(indices):
        newI = vals.index(node)
        n = vals.pop(newI)
        vals.insert((newI + n.val) % (l - 1), n)

for i, node in enumerate(vals):
    if node.val == 0:
        startI = i
        break

i = startI

out = 0
for j in range(3):
    i = (i + 1000) % len(vals)
    out += vals[i].val

print(out)