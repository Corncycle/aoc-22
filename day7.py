import util

data = util.parseFileAs("./inputs/d7.txt", str)

class Direc:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.contents = []
    
    def getSize(self):
        out = 0
        for i, item in enumerate(self.contents):
            if type(item) == Direc:
                out += item.getSize()
            else:
                out += item.size
        return out

    def getSubdirec(self, name):
        for item in self.contents:
            if item.name == name:
                return item
        print("lets hope this doesnt happen")

    def contains(self, name):
        return any([item.name == name for item in self.contents])

    def __repr__(self) -> str:
        return self.name + ": " + str(self.contents)

class Fil:
    def __init__(self, name, parent, size):
        self.name = name
        self.parent = parent
        self.size = size

    def __repr__(self) -> str:
        return self.name

out = 0
pointer = Direc("/", None)
root = pointer
streamMode = False
for i, val in enumerate(data):
    if i > 0:
        if val[0] == "$":
            if val[2] == "c":
                _, __, cmddir = val.split()
                if cmddir == "..":
                    pointer = pointer.parent
                elif cmddir == "/":
                    pointer = root
                else:
                    pointer = pointer.getSubdirec(cmddir)
        else:
            if val[0] == "d":
                dirname = val.split()[1]
                if not pointer.contains(dirname):
                    pointer.contents.append(Direc(dirname, pointer))
            else:
                size, filename = val.split()
                size = int(size)
                if not pointer.contains(filename):
                    pointer.contents.append(Fil(filename, pointer, size))


out = 0

def getContributors(dir):
    global out
    if dir.getSize() <= 100000:
        out += dir.getSize()
    for item in dir.contents:
        if type(item) == Direc:
            getContributors(item)

getContributors(root)
print(out)

removeAmt = root.getSize() - 40000000

bestFound = 70000000
def findRemoves(dir):
    global bestFound
    if removeAmt <= dir.getSize() <= bestFound:
        bestFound = dir.getSize()
    for item in dir.contents:
        if type(item) == Direc:
            findRemoves(item)

findRemoves(root)
print(bestFound)