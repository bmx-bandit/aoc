from functools import cache

with open("input", "r") as f:
    lines = [line.rstrip() for line in f.readlines()]

patterns = lines[0].replace(" ", "").split(",")
designs = lines[2:]

@cache
def test(design):
    count = 0
    if len(design) == 0:
        return 1
    for pattern in patterns:
        if design.startswith(pattern):
            count += test(design[len(pattern):])
    return count

p1 = 0
p2 = 0

for design in designs:
    ret = test(design)
    if ret:
        p1 += 1
    p2 += ret

print(p1)
print(p2)
