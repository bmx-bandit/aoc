with open("input", "r") as f:
    disk_map = [int(x) for x in f.read().rstrip()]

def checksum(file_system):
    csum = 0
    block_id = 0
    for file_id in file_system:
        if file_id != -1:
            csum += block_id * file_id
        block_id += 1
    return csum

file_system = []
file_list = []
free_list = []
file_id = 0

for block_id in range(len(disk_map)):
    block_list = []
    for i in range(disk_map[block_id]):
        block_list += [len(file_system)+i]
    if block_id % 2 == 0:
        file_system += [file_id] * disk_map[block_id]
        file_list += block_list
        file_id += 1
    else:
        file_system += [-1] * disk_map[block_id]
        free_list += block_list

while free_list[0] <= file_list[-1]:
    free_head = free_list.pop(0)
    file_tail = file_list.pop(-1)
    block_id = file_system[file_tail]
    file_system[file_tail] = file_system[free_head]
    file_system[free_head] = block_id

print(checksum(file_system))

file_system = []
file_list = []
free_list = []
file_id = 0

for block_id in range(len(disk_map)):
    block_list = (len(file_system), disk_map[block_id])
    if block_id % 2 == 0:
        file_system += [file_id] * disk_map[block_id]
        file_list += [block_list]
        file_id += 1
    else:
        file_system += [-1] * disk_map[block_id]
        free_list += [block_list]

for file_blocks in reversed(file_list):
    file_id = 0
    for free_blocks in free_list:
        if file_blocks[1] > free_blocks[1] or file_blocks[0] <= free_blocks[0]:
            file_id += 1
            continue
        for i in range(file_blocks[1]):
            block = file_system[free_blocks[0]+i]
            file_system[free_blocks[0]+i] = file_system[file_blocks[0]+i]
            file_system[file_blocks[0]+i] = block
        block_id = free_blocks[0] + file_blocks[1]
        block_count = free_blocks[1] - file_blocks[1]
        free_list[file_id] = (block_id, block_count)
        break

print(checksum(file_system))
