with open("input", "r") as f:
    m = [[int(x) for x in l.rstrip()] for l in f.readlines()]

def hike(x, y):
    trails = []
    if m[y][x] == 9:
        return [(x, y)]
    for d in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        i = x + d[0]
        j = y + d[1]
        if i < 0 or i >= len(m[0]):
            continue
        if j < 0 or j >= len(m):
            continue
        if m[j][i] - m[y][x] != 1:
            continue
        trails += [(x, y)] + hike(i, j)
    return trails

score1 = 0
score2 = 0

for y in range(len(m)):
    for x in range(len(m[0])):
        if m[y][x] == 0:
            l = []
            for i, j in hike(x, y):
                if m[j][i] == 9:
                    l.append((i, j))
            score1 += len(list(set(l)))
            score2 += len(list(l))

print(score1)
print(score2)
