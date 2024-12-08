with open("input", "r") as f:
    m = f.readlines()

m = [list(l.rstrip()) for l in m]

X = len(m[0])
Y = len(m)

def antinode(a, b, flag=0):
    y = a[0]
    if b[0] > a[0]:
        y -= b[0] - a[0]
    if b[0] < a[0]:
        y += a[0] - b[0]
    x = a[1]
    if b[1] > a[1]:
        x -= b[1] - a[1]
    if b[1] < a[1]:
        x += a[1] - b[1]
    if y < 0 or y >= Y:
        return []
    if x < 0 or x >= X:
        return []
    l = [(y, x)]
    if flag:
        l += antinode((y, x), a, flag)
    return l

def scan(a, flag=0):
    n = []
    for j in range(Y):
        for i in range(X):
            if j == a[0] and i == a[1]:
                continue
            if m[j][i] != m[a[0]][a[1]]:
                continue
            x = antinode(a, (j, i), flag)
            n += x
    return n

def survey(flag=0):
    p = {}
    for y in range(Y):
        for x in range(X):
            if m[y][x] == ".":
                continue
            if m[y][x] == "#":
                continue
            n = scan((y, x), flag)
            if m[y][x] in p.keys():
                p[m[y][x]].append(n)
            else:
                p[m[y][x]] = [n]
    return p

a = survey()

b = []
for k, v in a.items():
    for x in v:
        b += x

print(len(list(set(b))))

a = survey(1)

i = 0
b = []
for k, v in a.items():
    i += len(v)
    for y in v:
        for x in y:
           b.append(x)

b = list(set(b))

j = len(b)

for y, x in b:
    if m[y][x] == ".":
        m[y][x] = "#"
    else:
        m[y][x] = "?"
        j -= 1

print(i+j)
