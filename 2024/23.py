with open("input", "r") as f:
    m = [l.strip().split("-") for l in f.readlines()]

x = {}

for a, b in m:
    try:
        x[a].append(b)
    except:
        x[a] = [b]
    try:
        x[b].append(a)
    except:
        x[b] = [a]

l = []

for a in x.keys():
    if a[0] != "t":
        continue
    for b in x[a]:
        for c in x[a]:
            if c not in x[b]:
                continue
            d = sorted((a, b, c))
            if d not in l:
                l.append(d)

print(len(l))

l = []

for a in x:
    ll = [a]
    for b in x:
        if a == b:
            continue
        ll.append(b)
        for c in ll[:-1]:
            if b in x[c]:
                continue
            ll.pop()
            break
    if len(ll) > len(l):
        l = ll

print(",".join(sorted(l)))
