from itertools import product

def permute(operators, count):
    return list(product(operators, repeat=count))

def evaluate(operands, operators):
    total = operands[0]
    for i in range(len(operators)):
        if operators[i] == "+":
            total += operands[i+1]
        elif operators[i] == "*":
            total *= operands[i+1]
        elif operators[i] == "|":
            total = int(str(total)+str(operands[i+1]))
    return total

def test(line, operators):
    total, data = line.strip().split(":")
    operands = [int(v) for v in data.strip().split(" ")]
    for operators in permute(operators, len(operands)-1):
        if evaluate(operands, operators) == int(total):
            return int(total)
    return 0

with open("input", "r") as f:
    d = f.readlines()

c = 0
for l in d:
    c += test(l, ["+", "*"])
print(c)

c = 0
for l in d:
    c += test(l, ["+", "*", "|"])
print(c)
