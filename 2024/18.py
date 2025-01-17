with open("input", "r") as f:
    d = [l.rstrip().split(",") for l in f.readlines()]

d = [(int(l[0]), int(l[1])) for l in d]

def simulate(b):
    p = [(0, 0, 0)]
    c = {(0, 0)}
    while p:
        x, y, n = p[0]
        p = p[1:]
        if x == 70 and y == 70:
            return n
        for d in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
            i = x + d[0]
            j = y + d[1]
            if i < 0 or i > 70:
                continue
            if j < 0 or j > 70:
                continue
            if (i, j) in b:
                continue
            if (i, j) in c:
                continue
            p.append((i, j, n+1))
            c.add((i, j))
    return 0

print(simulate(set(d[:1024])))

for i in range(1024, len(d)):
    if simulate(set(d[:i])) == 0:
        i = i -1
        break

print(f"{d[i][0]},{d[i][1]}")
