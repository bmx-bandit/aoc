with open("input", "r") as f:
    info = [l.rstrip().split(":")[-1] for l in f.readlines()]

a = int(info[0])
b = int(info[1])
c = int(info[2])
p = [int(o) for o in info[4].split(",")]

def run(p, a, b, c):
    out = []
    ip = 0
    while ip < len(p):
        opcode, operand = p[ip], p[ip+1]
        v = operand
        if operand == 4:
            v = a
        if operand == 5:
            v = b
        if operand == 6:
            v = c
        if opcode == 0:
            a = int(a // pow(2, v))
        if opcode == 1:
            b = b ^ operand
        if opcode == 2:
            b = v % 8
        if opcode == 3:
            if a != 0:
                ip = operand
                continue
        if opcode == 4:
            b = b ^ c
        if opcode == 5:
            out.append(v % 8)
        if opcode == 6:
            b = int(a // pow(2, v))
        if opcode == 7:
            c = int(a // pow(2, v))
        ip += 2
    return out

print(",".join([str(v) for v in run(p, a, b, c)]))

a = 0

for i in range(len(p)-1, -1, -1):
    a = a << 3
    while 1:
        out = run(p, a, b, c)
        if out == p[i:]:
            break
        a = a + 1

print(a)
