with open("tmp.txt", "r") as file:
    puzzle_input = file.readlines()

left_list, right_list = list(), list()

for line in puzzle_input:
    left_number, right_number = [int(number) for number in line.split()]
    left_list.append(left_number)
    right_list.append(right_number)

# Part 1
left_list.sort()
right_list.sort()

distances = list()
for index in range(len(left_list)):
    smallest_number_in_left_list = left_list[index]
    smallest_number_in_right_list = right_list[index]
    distances.append(abs(smallest_number_in_left_list - smallest_number_in_right_list))

sum_of_distances = sum(distances)

print(sum_of_distances)

# Part 2

total_similarity_score = 0

# A good elf would probably use better data structures here.
for number_in_left_list in left_list:
    apperances_in_right_list = right_list.count(number_in_left_list)
    total_similarity_score += (number_in_left_list * apperances_in_right_list)

print(total_similarity_score)
