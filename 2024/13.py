with open("input", "r") as f:
    l = [l.rstrip() for l in f.readlines()]

e = []

for i in range(0, len(l), 4):
    d = {}
    a = l[i].split()
    b = l[i+1].split()
    c = l[i+2].split()
    d["A"] = [int(a[2][2:-1]), int(a[3][2:])]
    d["B"] = [int(b[2][2:-1]), int(b[3][2:])]
    d["C"] = [int(c[1][2:-1]), int(c[2][2:])]
    e.append(d)

p = []

for d in e:
    a = d["A"]
    b = d["B"]
    c = d["C"]
    for x in range(100):
        for y in range(100):
            i = a[0]*x+b[0]*y
            j = a[1]*x+b[1]*y
            if i == c[0] and j == c[1]:
                p.append(3*x+y)

print(sum(p))

for d in e:
    d["C"][0] += 10000000000000
    d["C"][1] += 10000000000000


p = 0

for d in e:
    a = d["A"]
    b = d["B"]
    c = d["C"]
    x, m = divmod(c[0]*b[1]-c[1]*b[0], a[0]*b[1]-a[1]*b[0])
    y, n = divmod(c[1]*a[0]-c[0]*a[1], a[0]*b[1]-a[1]*b[0])
    if m == 0 and n == 0:
        p += 3*x+y

print(p)
