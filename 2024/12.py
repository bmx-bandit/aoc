with open("input", "r") as f:
    m = [[x for x in l.rstrip()] for l in f.readlines()]

def plot(x, y, r):
    if (x, y) in r:
        return [r]
    if len(r) == 0:
        r += [0]
    r += [(x, y)]
    for d in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        i = x + d[0]
        j = y + d[1]
        if i < 0 or i >= len(m[0]):
            r[0] += 1
            continue
        if j < 0 or j >= len(m):
            r[0] += 1
            continue
        if m[j][i] != m[y][x]:
            r[0] += 1
            continue
        if (i, j) in r:
            continue
        r = plot(i, j, r)
    return r

def check(g, r):
    for x in g:
        if sorted(r[1:]) == sorted(x[1:]):
            return True
    return False

g = []

for y in range(len(m)):
    for x in range(len(m[0])):
        r = plot(x, y, [])
        if check(g, r) is False:
            g += [r]

def corners(r):
    s = []
    for p in r:
        for d in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
            i = p[0]
            j = p[1]
            if (p[0]+d[1], p[1]+d[0]) in r:
                continue
            while 1:
                if (i+d[1], j+d[0]) in r:
                    break
                if (i+d[0], j+d[1]) not in r:
                    break
                i += d[0]
                j += d[1]
            s += [(i, j, d[0], d[1])]
    return len(set(s))

p1 = 0
p2 = 0

for r in g:
    p1 += (len(r[1:]))*r[0]
    p2 += (len(r[1:]))*corners(r[1:])

print(p1)
print(p2)
