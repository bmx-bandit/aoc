with open("input", "r") as f:
    data = f.read().split("\n\n")

wires = {k:int(v) for k,v in [w.split(": ") for w in data[0].split("\n")]}
links = [x.split() for x in data[1].split("\n")[:-1]]

def logic(link, wires):
    if link[1] == "AND":
        return wires[link[0]] & wires[link[2]]
    if link[1] == "OR":
        return wires[link[0]] | wires[link[2]]
    if link[1] == "XOR":
        return wires[link[0]] ^ wires[link[2]]
    return None

def device(wires, links):
    flag = 0
    for link in links:
        if link[0] not in wires:
            continue
        if link[2] not in wires:
            continue
        if link[4] in wires:
            continue
        wires[link[4]] = logic(link, wires)
        flag = 1
    return flag

while device(wires, links):
    pass

out = 0

for wire in sorted(wires.keys()):
    if wire[0] == "z" and wires[wire]:
        out |= 1 << int(wire[1:])

print(out)

def find_link(x, g, y, links):
    for l in links:
        if l[0] == x:
            if l[1] == g:
                if l[2] == y:
                    return l[4]
        if l[0] == y:
            if l[1] == g:
                if l[2] == x:
                    return l[4]
    return None

def swap_wires(a, b, links):
    x = []
    for l in links:
        if l[4] == a:
            x.append([l[0], l[1], l[2], l[3], b])
        elif l[4] == b:
            x.append([l[0], l[1], l[2], l[3], a])
        else:
            x.append(l)
    return x

swap = []
i = 0

while i < 45:
    x = "x"+"%02d"%i
    y = "y"+"%02d"%i
    z = "z"+"%02d"%i
    if i == 0:
        a = find_link(x, "AND", y, links)
    else:
        b = find_link(x, "XOR", y, links)
        c = find_link(x, "AND", y, links)
        d = find_link(b, "XOR", a, links)
        if d is None:
            swap.extend([b, c])
            links = swap_wires(b, c, links)
            i = 0
            continue
        if d != z:
            swap.extend([d, z])
            links = swap_wires(d, z, links)
            i = 0
            continue
        e = find_link(b, "AND", a, links)
        a = find_link(c, "OR", e, links)
    i += 1

print(",".join(sorted(swap)))
