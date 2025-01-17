def test_tile(w, y, x, d, t):
    if (y, x) in t:
        return True
    t.append((y, x))
    j = y + d[0]
    i = x + d[1]
    if w[j][i] == "#":
        return False
    if w[j][i] == "O":
        return test_tile(w, j, i, d, t)
    if w[j][i] == "[":
        if test_tile(w, j, i, d, t):
            return test_tile(w, j, i+1, d, t)
        return False
    if w[j][i] == "]":
        if test_tile(w, j, i-1, d, t):
            return test_tile(w, j, i, d, t)
        return False
    return True

def push_box(w, d, t):
    for y, x in t:
        j = y + d[0]
        i = x + d[1]
        if (j, i) in t:
            continue
        a = w[j][i]
        w[j][i] = w[y][x]
        w[y][x] = a
        t.remove((y, x))

def move_robot(w, y, x, d):
    j = y + d[0]
    i = x + d[1]
    if 0 > j >= len(w):
        return (y, x)
    if 0 > i >= len(w[0]): 
        return (y, x)
    if w[j][i] == "#":
        return (y, x)
    if w[j][i] in ["O", "[", "]"]:
        t = []
        if not test_tile(w, y, x, d, t):
            return (y, x)
        while len(t):
            push_box(w, d, t)
    return (j, i)

with open("input", "r") as f:
    f = [l.rstrip() for l in f.readlines()]

v = []
w = []
m = ""

for l in f:
    if len(l) == 0:
        continue
    if l.startswith("#"):
        v.append(list(l))
        continue
    m += l

for y in range(len(v)):
    l = []
    for x in range(len(v[0])):
        if v[y][x] == "#":
            l.append("#")
            l.append("#")
        if v[y][x] == "O":
            l.append("[")
            l.append("]")
        if v[y][x] == ".":
            l.append(".")
            l.append(".")
        if v[y][x] == "@":
            l.append("@")
            l.append(".")
    w.append(l)

def find_robot(w):
    for y in range(len(w)):
        for x in range(len(w[0])):
            if w[y][x] == "@":
                return (y, x)
    return None

def find_boxes(w, b):
    l = []
    for y in range(len(w)):
        for x in range(len(w[0])):
            if w[y][x] == b:
                l.append((y, x))
    return l

lookup = {"^":(-1,0),">":(0, 1),"v":(1, 0),"<": (0,-1)}

y, x = find_robot(v)

for d in m:
    y, x = move_robot(v, y, x, lookup[d])

b = find_boxes(v, "O")

print(sum(100 * y + x for (y, x) in b))

y, x = find_robot(w)

for d in m:
    y, x = move_robot(w, y, x, lookup[d])

b = find_boxes(w, "[")

print(sum(100 * y + x for (y, x) in b))
