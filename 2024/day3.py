
with open("input3.txt", "r") as file:
    puzzle_input = file.readlines()

corrupted_memory = ''
for line in puzzle_input:
    corrupted_memory += line

# Part 1

import re

instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)", corrupted_memory)

sum_of_multiplications = 0

for instruction in instructions:
    numbers = [int(number) for number in re.findall(r"\d+", instruction)]
    sum_of_multiplications += (numbers[0] * numbers[1])

print(sum_of_multiplications)

# Part 2

instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", corrupted_memory)

sum_of_multiplications = 0

enabled = True
for instruction in instructions:
    print(instruction)
    if instruction == "do()":
        enabled = True
    elif instruction == "don't()":
        enabled = False
    else:
        numbers = [int(number) for number in re.findall(r"\d+", instruction)]
        if enabled:
            sum_of_multiplications += (numbers[0] * numbers[1])

print(sum_of_multiplications)