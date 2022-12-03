import util

data = util.parseFileAs("./inputs/d3.txt", str)

out = 0
for i, val in enumerate(data):
    l = len(val) // 2
    s1 = set(val[:l])
    s2 = set(val[l:])
    letter = s1.intersection(s2).pop()
    if letter.islower():
        out += ord(letter) - 96
    else:
        out += ord(letter) - 64 + 26

print(out)

out = 0
for i, val in enumerate(data):
    if i % 3 == 0:
        s1 = set(data[i])
        s2 = set(data[i + 1])
        s3 = set(data[i + 2])
        letter = s1.intersection(s2).intersection(s3).pop()
        if letter.islower():
            out += ord(letter) - 96
        else:
            out += ord(letter) - 64 + 26

print(out)