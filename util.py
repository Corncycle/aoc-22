def parseFileAs(filePath, dataType):
    with open(filePath) as f:
        data = [dataType(line.strip()) for line in f]
        return data