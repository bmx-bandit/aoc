with open("input", "r") as f:
    data = [[y for y in x.split("\n") if len(y)] for x in f.read().split("\n\n")]

locks = []
keys = []

for x in data:
    h = [0] * len(x[0])
    for i in range(len(x)):
        for j in range(len(x[0])):
            if x[i][j] == "#":
                h[j] += 1
    h = [y-1 for y in h]
    if x[0][0] == "#":
        locks.append(h)
    else:
        keys.append(h)

count = 0

for lock in locks:
    for key in keys:
        flag = 1
        for i in range(len(key)):
            if lock[i] + key[i] >= len(data[0]) - 1:
                flag = 0
        count += flag

print(count)
