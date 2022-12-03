def parseFileAs(filePath, dataType):
    with open(filePath) as f:
        data = [dataType(line.strip()) for line in f]
        return data

def charToNum(c):
    '''returns 1 for a and A. 
    returns 2 for b and B, etc
    '''
    if c.isLower():
        return ord(c) - 96
    else:
        return ord(c) - 64