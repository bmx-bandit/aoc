with open("input", "r") as f:
    d = f.readlines()

r = {k: [] for k in range(256)}
u = []

for l in d:
    l = l.rstrip()
    if "|" in l:
        a, b = l.split("|")
        r[int(a)].append(int(b))
    if "," in l:
        u.append([int(x) for x in l.split(",")])

def test(x):
    for i in range(len(x)-1):
        if x[i+1] not in r[x[i]]:
            return False
    return True

c = 0
z = []

for x in u:
    if test(x):
        c += x[len(x)//2]
    else:
        z.append(x)

print(c)

c = 0

def add(l, x):
    if l == []:
        l.append(x)
        return l
    for i in range(len(l)-1, -1, -1):
        if x in r[l[i]]:
            l.insert(i+1, x)
            return l
    l.insert(0, x)
    return l

for x in z:
    s = []
    for y in x:
        s = add(s, y)
    c += s[len(s)//2]

print(c)
