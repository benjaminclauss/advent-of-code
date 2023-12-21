file_path = 'input12.txt'

import re

lines = list()
with open(file_path, 'r') as file:
    lines = [line.strip() for line in file.readlines()]

records = [(line.split(' ')[0], [int(g) for g in line.split(' ')[1].split(',')]) for line in lines]

def calculate_combinations_alt(row, spring_counts, previous_pounds, cache):
    if (row, spring_counts, previous_pounds) in cache:
        return cache[(row, spring_counts, previous_pounds)]
    # print(row + ' ' + str(spring_counts))
    if len(row) == 0:
        # We have exhausted the row and all springs.
        if len(spring_counts) == 0:
            return 1
        elif len(spring_counts) == 1 and spring_counts[0] == 0:
            return 1
        else: 
            # This makes the assumption that spring counts is cleared before we arrive here.
            return 0
    
    current_character = row[0]

    if current_character == '.':
        if len(spring_counts) > 0:
            count = spring_counts[0]
            if count == 0:
                # We ended a group.
                # We can proceed and remove this group.
                next_spring_counts = spring_counts.copy()
                next_spring_counts.remove(0)
                return calculate_combinations_alt(row[1:], next_spring_counts, 0)
            else:
                if previous_pounds > 0:
                    # This is bad. We encountered a period after previous #'s but didn't finish
                    return 0
                else:
                    # We might be starting on a '.' so continue.
                    next_spring_counts = spring_counts.copy()
                    return calculate_combinations_alt(row[1:], next_spring_counts, 0) 
        else:
            # We are out of spring groups. The rest of the string has to be all '.' or '?'.
            if '#' in row:
                return 0
            else:
                return 1
    elif current_character == '#':
        if len(spring_counts) > 0:
            # We have remaining springs to be counted and we just came across one.
            # Let's decrement this group's count and continue.
            count = spring_counts[0]
            next_spring_counts = spring_counts.copy()
            next_spring_counts[0] = next_spring_counts[0] - 1
            return calculate_combinations_alt(row[1:], next_spring_counts, previous_pounds + 1)
        else:
            # This is unexpected! We should not encounter a spring when none are left to be counted.
            return 0
    elif current_character == '?':
        if len(spring_counts) == 0:
            # This and everything else must be a '.'.
            if '#' in row[1:]:
                return 0
            return 1
            # next_spring_counts = spring_counts.copy() 
            # return calculate_combinations_alt(row[1:], next_spring_counts, 0)
        else:
            count = spring_counts[0]
            if count == 0:
                # print('ending group')
                # We must end the previous group here.
                next_spring_counts = spring_counts.copy()
                next_spring_counts.remove(0)
                return calculate_combinations_alt(row[1:], next_spring_counts, 0) 
            if previous_pounds > 0:
                # print('continuing group')
                # We are in a group and have to continue the group.
                next_spring_counts = spring_counts.copy()
                next_spring_counts[0] = next_spring_counts[0] - 1 
                return calculate_combinations_alt(row[1:], next_spring_counts, previous_pounds + 1)
            else:
                # print('option')
                # We are NOT in a group and have the choice whether or not to start a group.
                next_spring_counts_starting_group = spring_counts.copy()
                next_spring_counts_starting_group[0] = next_spring_counts_starting_group[0] - 1 
                with_start = calculate_combinations_alt(row[1:], next_spring_counts_starting_group, 1) 

                next_spring_counts_not_starting_group = spring_counts.copy()
                without_start = calculate_combinations_alt(row[1:], next_spring_counts_not_starting_group, 0)  
                return with_start + without_start


# records = [records[1]]
# sum_of_valid_combinations = 0
# for record in records:
#     print(record)
#     com = calculate_combinations_alt(record[0], record[1], 0)
#     sum_of_valid_combinations += com
#     print(com)
#     print()

# print(sum_of_valid_combinations)


unfolded_records = list()
for record in records:
    new_str = '?'.join([record[0] for i in range(5)]) 
    unfolded_records.append((new_str, record[1] * 5))
# print(unfolded_records)

sum_of_valid_combinations = 0
for record in unfolded_records:
    print(record)
    com = calculate_combinations_alt(record[0], record[1], 0)
    sum_of_valid_combinations += com
    print(com)
    print()

print(sum_of_valid_combinations)