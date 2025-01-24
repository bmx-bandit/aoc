def mix_prune(s, r):
    return (s ^ r) % 16777216

def evolve(s):
    s = mix_prune(s, s*64)
    s = mix_prune(s, int(s//32))
    s = mix_prune(s, s*2048)
    return s

def price(s):
    return int(str(s)[-1])

with open("input", "r") as f:
    secrets = [int(l.strip()) for l in f.readlines()]

t = 0

for s in secrets:
    for i in range(2000):
        s = evolve(s)
    t += s

print(t)

b = {}

for s in secrets:
    x = {}
    q = (0,0,0,0)
    for i in range(2000):
        p = price(s)
        s = evolve(s)
        n = price(s)
        q = (q[1],q[2],q[3],n-p)
        if i < 3:
            continue
        if q not in x:
            x[q] = n
    for q in x:
        try:
            b[q] += x[q]
        except:
            b[q] = x[q]

print(max(b.values()))
