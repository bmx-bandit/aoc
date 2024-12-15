with open("input", "r") as f:
    stones = [int(stone) for stone in f.read().rstrip().split()]

def blink1(stone):
    if stone == 0:
        return [1]
    s = str(stone)
    n = len(s)
    if n % 2 == 0:
        h = n // 2
        return [int(s[:h]), int(s[h:])]
    return [stone * 2024]

for i in range(25):
    line = []
    for j in range(len(stones)):
        line.extend(blink1(stones[j]))
    stones = line

print(len(stones))

with open("input", "r") as f:
    stones = {int(stone):1 for stone in f.read().rstrip().split()}

def blink3(stones, stone, count):
    try:
        stones[stone] += count
    except:
        stones[stone] = count
    return stones

def blink2(stones, stone, count):
    if stone == 0:
        return blink3(stones, 1, count)
    s = str(stone)
    n = len(s)
    if n % 2 == 0:
        h = n // 2
        stones = blink3(stones, int(s[:h]), count)
        stones = blink3(stones, int(s[h:]), count)
        return stones
    return blink3(stones, stone * 2024, count)

for i in range(75):
    temp = {}
    for stone, count in stones.items():
        temp = blink2(temp, stone, count)
    stones = temp

total = 0

for count in stones.values():
    total += count

print(total)
