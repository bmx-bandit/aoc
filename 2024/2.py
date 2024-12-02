def test2(levels, direction):
    if len(levels) < 2:
        return True
    if abs(levels[0] - levels[1]) > 3:
        return False
    if direction == 1:
        if levels[0] > levels[1]:
            return test2(levels[1:], 1)
        return False
    if levels[0] < levels[1]:
        return test2(levels[1:], 0)
    return False

def test1(levels):
    if len(levels) < 2:
        return True
    if levels[0] > levels[1]:
        return test2(levels, 1)
    if levels[0] < levels[1]:
        return test2(levels, 0)
    return False

with open("input", "r") as f:
    reports = f.readlines()

safe = 0

for report in reports:
    levels = [int(l) for l in report.rstrip().split()]
    result = test1(levels)
    if result == True:
        safe += 1

print(safe)

safe = 0

for report in reports:
    levels = [int(l) for l in report.rstrip().split()]
    for i in range(len(levels)):
        result = test1(levels[:i] + levels[i+1:])
        if result == True:
            break
    if result == True:
        safe += 1

print(safe)
