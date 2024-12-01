with open("input", "r") as f:
    lines = f.readlines()

a = []
b = []

for line in lines:
    x, y = line.split()
    a.append(int(x))
    b.append(int(y))

a = sorted(a)
b = sorted(b)

d = 0
for i in range(len(a)):
    d += abs(a[i] - b[i])
print(d)

s = 0
for n in a:
    s += n * (b.count(n))
print(s)
