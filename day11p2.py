import util
from collections import deque

data = util.parseFileAs("./inputs/d11.txt", str)

megaMod = 1

for i, val in enumerate(data):
    if i % 7 == 0:
        test = int(data[i + 3].split(" ")[-1])
        megaMod *= test

class Item:
    def __init__(self, val) -> None:
        self.val = val

    def modify(self, op, opAmount):
        if op == "+":
            self.val += opAmount
        elif op == "*":
            self.val *= opAmount
        elif op == "**":
            self.val = self.val ** 2
        self.val = self.val % megaMod

    def __repr__(self) -> str:
        return f"Item: {self.val}"

class Monkey:
    def __init__(self, op, opAmount, test, tRec, fRec, items) -> None:
        self.test = test
        self.op = op
        self.opAmount = opAmount
        self.tRec = tRec
        self.fRec = fRec
        self.items = deque()
        for item in items:
            self.items.append(Item(item))
        self.numInspections = 0

monkeys = []
for i, val in enumerate(data):
    if i % 7 == 0:
        items = data[i + 1].split()
        items = items[2:]
        items = [int(item.replace(",", "")) for item in items]
        op = "*" if "*" in data[i + 2] else "+"
        op = "**" if "old * old" in data[i + 2] else op
        opAmount = 2 if op == "**" else int(data[i + 2].split(" ")[-1])
        test = int(data[i + 3].split(" ")[-1])
        tRec = int(data[i + 4].split(" ")[-1])
        fRec = int(data[i + 5].split(" ")[-1])
        monkeys.append(Monkey(op, opAmount, test, tRec, fRec, items))

def doTurn(i, m):
    while m.items:
        m.numInspections += 1
        item = m.items.popleft()
        item.modify(m.op, m.opAmount)
        if item.val % m.test == 0:
            monkeys[m.tRec].items.append(item)
        else:
            monkeys[m.fRec].items.append(item)

def doRound():
    for i, m in enumerate(monkeys):
        doTurn(i, m)

for _ in range(10000):
    doRound()

counts = [m.numInspections for m in monkeys]
c = sorted(counts)
print(c[-1] * c[-2])