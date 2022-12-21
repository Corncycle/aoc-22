import util
from copy import deepcopy

data = util.parseFileAs("./inputs/d21.txt", str)

def getDefaultHumnValue():
    for i, val in enumerate(data):
        spl = val.split()
        if spl[0] == "humn:":
            return int(spl[1])
    assert False

def setupWithHumnValue(value):
    monks = {}
    for i, val in enumerate(data):
        spl = val.split()
        if spl[0] == "humn:":
            monks[spl[0][:-1]] = value
        elif len(spl) == 2:
            monks[spl[0][:-1]] = int(spl[1])
        else:
            monks[spl[0][:-1]] = spl[1:]
    return monks

def minimizeInitial(monks):
    for i in range(1000):
        doNoHumnFilter(monks)

def doNoHumnFilter(monks):
    for monk in monks:
        if type(monks[monk]) == list and "humn" not in monks[monk]:
            data = monks[monk]
            if type(monks[data[0]]) != list and type(monks[data[2]]) != list:
                if data[1] == "+":
                    val = monks[data[0]] + monks[data[2]]
                elif data[1] == "-":
                    val = monks[data[0]] - monks[data[2]]
                elif data[1] == "*":
                    val = monks[data[0]] * monks[data[2]]
                elif data[1] == "/":
                    val = monks[data[0]] / monks[data[2]]
                monks[monk] = val
    return "bleh"

def doFilter(monks):
    for monk in monks:
        if type(monks[monk]) == list:
            data = monks[monk]
            if type(monks[data[0]]) != list and type(monks[data[2]]) != list:
                if monk == "root":
                    return [monks[data[0]], monks[data[2]]]
                if data[1] == "+":
                    val = monks[data[0]] + monks[data[2]]
                elif data[1] == "-":
                    val = monks[data[0]] - monks[data[2]]
                elif data[1] == "*":
                    val = monks[data[0]] * monks[data[2]]
                elif data[1] == "/":
                    val = monks[data[0]] / monks[data[2]]
                monks[monk] = val
    return "bleh"

def testWithValAndList(value, monks):
    out = 0
    while True:
        status = doFilter(monks)
        if status != "bleh":
            out = status
            break
    return out

initial = setupWithHumnValue(getDefaultHumnValue())
minimizeInitial(initial)

def getMinimized():
    return deepcopy(initial)

m = getMinimized()
a, b = testWithValAndList(getDefaultHumnValue(), m)
print(int(a + b))

# incredible, incredible jank that will almost certainly only work for my input
val = (107992431115518 - 52282191702834) // 18.044444445
while True:
    monks = getMinimized()
    monks["humn"] = val
    a, b = testWithValAndList(val, monks)
    if (a == b):
        print(int(val))
        break
    val += 1
