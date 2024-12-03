import re

def scan(m):
    p = re.findall(r"mul\((\d{,3}),(\d{,3})\)", m)
    c = 0
    for a, b in p:
        c += int(a) * int(b)
    return c

with open("input", "r") as f:
    m = f.read()

print(scan(m))

c = 0
i = 0

while 1:
    j = m.find("don't()", i)
    if j == -1:
        j = len(m)
    c += scan(m[i:j])
    if j == len(m):
        break
    i = m.find("do()", j)

print(c)
