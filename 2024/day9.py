txt = '2333133121414131402'
# txt = '12345'

with open("input9.txt", "r") as file:
    puzzle_input = file.readlines()[0].strip()

# puzzle_input = txt

# Part 1

compaction = list()
for index, character in enumerate(puzzle_input):
    if index % 2 == 0:
        compaction += [str(index // 2)] * int(character)
    else:
        compaction += ['.'] * int(character)

left, right = 0, len(compaction) - 1

while left < right:
    if compaction[left] != '.':
        left += 1
        continue
    else:
        while compaction[right] == '.':
            right -= 1
        if left < right:
            compaction[left], compaction[right] = compaction[right], compaction[left]
            left += 1
            right -= 1

checksum = 0
for position, character in enumerate(compaction):
    if character == '.':
        continue
    checksum += position * int(character)

# print(compaction)
print(checksum)

# Part 2

class File:
    def __init__(self, length: int, id: int):
        self.length = length
        self.id = id
  
    def __str__(self):
        return str(self.id) * self.length

    def __repr__(self):
        return str(self)

class FreeSpace:
    def __init__(self, length: int):
        self.length = length

    def __str__(self):
        return "." * self.length

    def __repr__(self):
        return str(self)
    
disk_map = []

for index, character in enumerate(puzzle_input):
    if index % 2 == 0:
        f = File(int(character), index // 2)
        disk_map.append(f)
    else:
        disk_map.append(FreeSpace(int(character)))


right = len(disk_map) - 1
# Attempt to move each file exactly once in order of decreasing file ID number starting with the file with the highest file ID number.
latest_moved = None
while right >= 0:
    o = disk_map[right]
    if isinstance(o, FreeSpace):
        right -= 1
        continue

    if latest_moved is not None and o.id >= latest_moved:
        right -= 1
        continue
    # print(disk_map)

    # print('attempt to move ' + str(o))
    file_to_move = o
    
    for left in range(right):
        o = disk_map[left]
        if isinstance(o, File):
            left += 1
            continue
        free_space_length = o.length
        if file_to_move.length <= free_space_length:
            disk_map[left] = file_to_move
            disk_map[right] = FreeSpace(file_to_move.length)
            # Insert free space if necessary.
            remaining_free_space = free_space_length - file_to_move.length
            if remaining_free_space > 0:
                disk_map.insert(left + 1, FreeSpace(remaining_free_space))
                # Adjust pointer.
                right += 1
            break
    
    latest_moved = file_to_move.id
    right -= 1

compaction = []
for o in disk_map:
    if isinstance(o, File):
        compaction += [o.id] * int(o.length)
    else:
        compaction += ['.'] * int(o.length)

checksum = 0
for position, character in enumerate(compaction):
    if character == '.':
        continue
    checksum += position * int(character)

print(checksum)