import sys

sys.setrecursionlimit(10000)

with open("input", "r") as f:
    m = f.readlines()

m = [list(l) for l in m]
w = [list(l) for l in m]

def find(m):
    for y in range(len(m)):
        for x in range(len(m[0])-1):
            if m[y][x] == "^":
                return (y, x, 0, 0)
            if m[y][x] == ">":
                return (y, x, 1, 0)
            if m[y][x] == "v":
                return (y, x, 2, 0)
            if m[y][x] == "<":
                return (y, x, 3, 0)
    return None

def move(g):
    if m[g[0]][g[1]] != "x":
        g = (g[0], g[1], g[2], g[3]+1)
        m[g[0]][g[1]] = "x"
    if g[2] == 0:
        if g[0] == 0:
            return g
        if m[g[0]-1][g[1]] == "#":
            return move((g[0], g[1], (g[2]+1)%4, g[3]))
        return move((g[0]-1, g[1], g[2], g[3]))
    if g[2] == 1:
        if g[1] == len(m[0])-1:
            return g
        if m[g[0]][g[1]+1] == "#":
            return move((g[0], g[1], (g[2]+1)%4, g[3]))
        return move((g[0], g[1]+1, g[2], g[3]))
    if g[2] == 2:
        if g[0] == len(m)-1:
            return g
        if m[g[0]+1][g[1]] == "#":
            return move((g[0], g[1], (g[2]+1)%4, g[3]))
        return move((g[0]+1, g[1], g[2], g[3]))
    if g[2] == 3:
        if g[1] == 0:
            return g
        if m[g[0]][g[1]-1] == "#":
            return move((g[0], g[1], (g[2]+1)%4, g[3]))
        return move((g[0], g[1]-1, g[2], g[3]))
    return g

print(move(find(m))[-1])

def find2(m):
    for y in range(len(m)):
        for x in range(len(m[0])-1):
            if m[y][x] == "^":
                return (y, x, 0, 0, True)
            if m[y][x] == ">":
                return (y, x, 1, 0, True)
            if m[y][x] == "v":
                return (y, x, 2, 0, True)
            if m[y][x] == "<":
                return (y, x, 3, 0, True)
    return None

def move2(g, m):
    if g[2] == 0:
        if g[0] == 0:
            return (g[0], g[1], g[2], g[3], False)
        if m[g[0]-1][g[1]] == "#":
            return (g[0], g[1], (g[2]+1)%4, g[3], g[4])
        return (g[0]-1, g[1], g[2], g[3], g[4])
    if g[2] == 1:
        if g[1] == len(m[0])-1:
            return (g[0], g[1], g[2], g[3], False)
        if m[g[0]][g[1]+1] == "#":
            return (g[0], g[1], (g[2]+1)%4, g[3], g[4])
        return (g[0], g[1]+1, g[2], g[3], g[4])
    if g[2] == 2:
        if g[0] == len(m)-1:
            return (g[0], g[1], g[2], g[3], False)
        if m[g[0]+1][g[1]] == "#":
            return (g[0], g[1], (g[2]+1)%4, g[3], g[4])
        return (g[0]+1, g[1], g[2], g[3], g[4])
    if g[2] == 3:
        if g[1] == 0:
            return (g[0], g[1], g[2], g[3], False)
        if m[g[0]][g[1]-1] == "#":
            return (g[0], g[1], (g[2]+1)%4, g[3], g[4])
        return (g[0], g[1]-1, g[2], g[3], g[4])

c = 0

for y in range(len(w)):
    for x in range(len(w[0])-1):
        g = find2(w)
        if g[0] == y and g[1] == x:
            continue
        b = w[y][x]
        w[y][x] = "#"
        for i in range(100000):
            if g[4] == False:
                break
            g = move2(g, w)
        if i == 99999:
            c += 1
        w[y][x] = b

print(c)
