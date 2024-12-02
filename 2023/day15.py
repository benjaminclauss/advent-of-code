
def hash(s):
    current_value = 0
    for character in s:
        ascii_code = ord(character)
        current_value += ascii_code
        current_value *= 17
        current_value %= 256
    return current_value
        
line = ''
with open('input15.txt', 'r') as file:
    line = file.readline().strip()

print(sum(hash(s) for s in line.split(',')))

NUMBER_OF_BOXES = 256

from collections import defaultdict

boxes = defaultdict(list)
import re

steps = re.findall(r'((\w+)(=|-)(\d*)),{0,1}', line)

for step in steps:
    label, operation = step[1], step[2]
    box_number = hash(label)
    old_lenses = boxes[box_number]
    if operation == '-':
        new_lenses = [lens for lens in old_lenses if not lens[0] == label]
        boxes[box_number] = new_lenses
    else:
        focal_length = int(step[3])
        if any(lens[0] == label for lens in old_lenses):
            new_lenses = [(label, focal_length) if lens[0] == label else lens for lens in old_lenses]
            boxes[box_number] = new_lenses
        else:
            old_lenses.append((label, focal_length))
            boxes[box_number] = old_lenses

total_focusing_power = 0
for box_number in range(NUMBER_OF_BOXES):
    box = boxes[box_number]
    slots = len(box)
    if slots > 0:
        for slot_number in range(slots):
            lens = box[slot_number]
            focal_length = lens[1]
            focusing_power = (box_number + 1) * (slot_number + 1) * lens[1]
            total_focusing_power += focusing_power

print(total_focusing_power)
