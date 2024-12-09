txt = '2333133121414131402'
# txt = '12345'

with open("input9.txt", "r") as file:
    puzzle_input = file.readlines()[0].strip()

# puzzle_input = txt

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
        break
    checksum += position * int(character)

print(checksum)
