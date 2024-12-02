with open("input2.txt", "r") as file:
    puzzle_input = file.readlines()

reports = list()
for line in puzzle_input:
    report = [int(number) for number in line.split()]
    reports.append(report)

# Part 1

def is_ascending_or_descending(report):
    ascending = all(report[i] <= report[i+1] for i in range(len(report)-1))
    descending = all(report[i] >= report[i+1] for i in range(len(report)-1))
    return ascending or descending

def difference_between_levels_within(report, min, max):
    return all(abs(report[i+1] - report[i]) in range(min, max+1) for i in range(len(report)-1))


number_of_safe_reports = 0

for report in reports:
    if is_ascending_or_descending(report) and difference_between_levels_within(report, 1, 3):
        number_of_safe_reports += 1

print(number_of_safe_reports)

# Part 2

number_of_safe_reports = 0

def remove_level(lst, index=None):
    if index is None:
        for i in range(len(lst)):
            yield lst[:i] + lst[i+1:]
    else:
        return lst[:index] + lst[index+1:]

for report in reports:
    if is_ascending_or_descending(report) and difference_between_levels_within(report, 1, 3):
        number_of_safe_reports += 1
        continue
    # This could probably be more efficient.
    for report_with_level_removed in remove_level(report):
        if is_ascending_or_descending(report_with_level_removed) and difference_between_levels_within(report_with_level_removed, 1, 3):
            number_of_safe_reports += 1
            break 

print(number_of_safe_reports)
