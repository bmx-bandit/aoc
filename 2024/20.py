with open("input", "r") as f:
    m = [l.strip() for l in f.readlines()]

for y in range(len(m)):
    for x in range(len(m[0])):
        if m[y][x] == 'S':
            h = {(y,x):0}
            l = [(y,x)]

for y, x in l:
    for d in [(1,0),(0,1),(-1,0),(0,-1)]:
        j = y + d[0]
        i = x + d[1]
        if m[j][i] == '#':
            continue
        if (j, i) in h:
            continue
        h[(j, i)] = h[(y, x)]+1
        l.append((j, i))

cheats = []

for a in h:
    for d in [(1,0),(0,1),(-1,0),(0,-1)]:
        b = (a[0]+2*d[0],a[1]+2*d[1])
        if b not in h:
            continue
        if h[b] > h[a]:
            continue
        c = h[a] - h[b] - 2
        cheats.append(c)

print(len([c for c in cheats if c >= 100]))

cheats = []
p = 20

for a in h:
    for i in range(-p, p+1):
        for j in range(-p, p+1):
            if abs(i) + abs(j) > p:
                continue
            b = (a[0]+i,a[1]+j)
            if b not in h:
                continue
            if h[b] > h[a]:
                continue
            c =  h[a] - h[b] - abs(i) - abs(j)
            cheats.append(c)

print(len([c for c in cheats if c >= 100]))
