import util

data = util.parseFileAs("./inputs/d5.txt", str)

# really nice, reusable code here lol 
stacks = [[] for _ in range(9)]
for i in reversed(range(8)):
    for j in range(9):
        if data[i][4 * j + 1] != " ":
            stacks[j].append(data[i][4 * j + 1])

for i, val in enumerate(data):
    if i > 9:
        instruction = val.split()
        amt, src, dest = int(instruction[1]), int(instruction[3]), int(instruction[5])
        mv = []
        for j in range(amt):
            mv.append(stacks[src - 1].pop())
        stacks[dest - 1].extend(mv)

out = [stack.pop() for stack in stacks]
print("".join(out))

data = util.parseFileAs("./inputs/input.txt", str)

stacks = [[] for _ in range(9)]
for i in reversed(range(8)):
    for j in range(9):
        if data[i][4 * j + 1] != " ":
            stacks[j].append(data[i][4 * j + 1])

for i, val in enumerate(data):
    if i > 9:
        instruction = val.split()
        amt, src, dest = int(instruction[1]), int(instruction[3]), int(instruction[5])
        mv = []
        for j in range(amt):
            mv.append(stacks[src - 1].pop())
        mv = reversed(mv)
        stacks[dest - 1].extend(mv)

out = [stack.pop() for stack in stacks]
print("".join(out))