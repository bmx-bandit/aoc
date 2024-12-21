with open("input", "r") as f:
    d = [l.rstrip().split() for l in f.readlines()]

r = []

for p, v in d:
    p = p.split("=")[1].split(",")
    v = v.split("=")[1].split(",")
    p = [int(p[0]), int(p[1])]
    v = [int(v[0]), int(v[1])]
    r.append((p, v))

w = 101
h = 103

t = []

for i in range(h):
    t.append([0]*w)

for i in range(len(r)):
    for j in range(100):
        r[i][0][0] += r[i][1][0]
        r[i][0][0] %= w
        r[i][0][1] += r[i][1][1]
        r[i][0][1] %= h

for (x, y), v in r:
    t[y][x] += 1

a = 0
b = 0
c = 0
d = 0

for (x, y), v in r:
    if x == len(t[0]) // 2:
        continue
    if y == len(t) // 2:
        continue
    if x < len(t[0]) // 2:
        if y < len(t) // 2:
            a += 1
        else:
            b += 1
    else:
        if y < len(t) // 2:
            c += 1
        else:
            d += 1

print(a*b*c*d)

with open("input", "r") as f:
    d = [l.rstrip().split() for l in f.readlines()]

r = []

for p, v in d:
    p = p.split("=")[1].split(",")
    v = v.split("=")[1].split(",")
    p = [int(p[0]), int(p[1])]
    v = [int(v[0]), int(v[1])]
    r.append((p, v))

j = 0

while 1:

    for i in range(len(r)):
        r[i][0][0] += r[i][1][0]
        r[i][0][0] %= w
        r[i][0][1] += r[i][1][1]
        r[i][0][1] %= h
    
    j += 1

    if len(set([(x, y) for (x, y), v in r])) == len(r):
        break
    
t = []

for i in range(h):
    t.append([0]*w)
    
for (x, y), v in r:
    t[y][x] += 1

for l in t:
    print("".join(str("x" if x else ".") for x in l))

print(j)
