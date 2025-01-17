with open("input", "r") as f:
    d = [l.rstrip() for l in f.readlines()]

maze = {}

i = 0
for l in d:
    j = 0
    for t in l:
        maze[(i, j)] = t
        if t == "S":
            start_tile = (i, j)
        if t == "E":
            end_tile = (i, j)
        j += 1
    i += 1

moves = {}
paths = []

states = [[0, (0, 1), start_tile]]

while states:
    x = []
    for s in states:
        for d in [(0,1),(1,0),(0,-1),(-1,0)]:
            i = s[-1][0] + d[0]
            j = s[-1][1] + d[1]
            tile = (i, j)
            if tile not in maze:
                continue
            if maze[tile] == "#":
                continue
            if (tile, d) in moves:
                if moves[(tile, d)] < s[0]:
                    continue
            state = [x for x in s]
            state[0] += 1
            if s[1] != d:
                state[0] += 1000
            state[1] = d
            state.append(tile)
            x.append(state)
            moves[(tile, d)] = state[0]
            if tile == end_tile:
                paths.append(state)
    states = x

scores = []

for (tile, d), score in moves.items():
    if tile == end_tile:
        scores.append(score)

score = sorted(scores)[0]

print(score)

tiles = []

for best in paths:
    if best[0] != score:
        continue
    for tile in best[2:]:
        if tile in tiles:
            continue
        tiles.append(tile)

print(len(tiles))
