def parseFileAs(filePath, dataType):
    with open(filePath) as f:
        data = [dataType(line.strip("\n")) for line in f]
        return data

def charToNum(c):
    '''returns 1 for a and A. 
    returns 2 for b and B, etc
    '''
    if c.islower():
        return ord(c) - 96
    else:
        return ord(c) - 64

def tupsum(a, b):
    if len(a) != len(b):
        assert False
    return tuple([a[i] + b[i] for i in range(len(a))])