with open("input", "r") as f:
    p = f.readlines()

x = len(p[0])-1
y = len(p)

q = []

for l in p:
    q.append(l.rstrip())

def build(p, q):
    j = 0
    for i in range(x+y-1):
        a = int(i/x)*((i%x)+1)
        b = abs(abs(i-x+1)-x+1)+1
        l = ""
        for k in range(b):
            l += p[j-k][k+a]
        q.append(l)
        j = min(j+1, y-1)
    return q

q = build(list(reversed(q)), q)
q = build(p, q)

for i in range(x):
    l = ""
    for j in range(y):
        l += p[j][i]
    q.append(l)

def search(w):
    c = 0
    for l in q:
        c += l.count(w)
        c += l.count(w[::-1])
    return c

print(search("XMAS"))

c = 0
for i in range(1, y-1):
    for j in range(1, x-1):
        if p[i][j] == "A":
            if p[i-1][j-1] == "M" and p[i+1][j+1] == "S":
                if p[i+1][j-1] == "M" and p[i-1][j+1] == "S":
                    c += 1
            if p[i-1][j-1] == "S" and p[i+1][j+1] == "M":
                if p[i+1][j-1] == "S" and p[i-1][j+1] == "M":
                    c += 1
            if p[i-1][j-1] == "M" and p[i+1][j+1] == "S":
                if p[i+1][j-1] == "S" and p[i-1][j+1] == "M":
                    c += 1
            if p[i+1][j-1] == "M" and p[i-1][j+1] == "S":
                if p[i-1][j-1] == "S" and p[i+1][j+1] == "M":
                    c += 1
print(c)
