import util

data = util.parseFileAs("./inputs/d6.txt", str)

st = data[0]
i = 4
chars = [st[j] for j in range(4)]
while len(set(chars)) != 4:
    for j in range(3):
        chars[j] = chars[j + 1]
    chars[3] = st[i]
    i += 1
print(i)

st = data[0]
i = 14
chars = [st[j] for j in range(14)]
while len(set(chars)) != 14:
    for j in range(13):
        chars[j] = chars[j + 1]
    chars[13] = st[i]
    i += 1
print(i)