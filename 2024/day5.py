
with open("input5.txt", "r") as file:
    puzzle_input = file.readlines()

page_ordering_rules = []
pages_to_produce_in_each_update = []

for line in puzzle_input:
    if '|' in line:        
        page_ordering_rule = tuple(int(page_number) for page_number in line.strip().split('|'))
        page_ordering_rules.append(page_ordering_rule)
    elif ',' in line:
        update = [int(page_number) for page_number in line.strip().split(',')]
        pages_to_produce_in_each_update.append(update)

# Part 1

page_ordering_violations = set()
for rule in page_ordering_rules:
    page_ordering_violations.add((rule[1], rule[0]))

def is_correctly_ordered(update):
    page_orders = []
    for x in range(len(update)):
        for y in range(x + 1, len(update)):
            page_orders.append((update[x], update[y]))
    
    for ordering in page_orders:
        if ordering in page_ordering_violations:
            return False
    return True

sum_of_middle_page_numbers = 0

for update in pages_to_produce_in_each_update:
    if is_correctly_ordered(update):
        middle_page_number = update[len(update) // 2]
        sum_of_middle_page_numbers += middle_page_number

print(sum_of_middle_page_numbers)

# Part 2

def correct(update):
    page_orders = []
    for x in range(len(update)):
        for y in range(x + 1, len(update)):
            page_orders.append((update[x], update[y]))
    
    for ordering in page_orders:
        if ordering in page_ordering_violations:
            idx1 = update.index(ordering[0])
            idx2 = update.index(ordering[1])
            update[idx1], update[idx2] = update[idx2], update[idx1]
            return correct(update)
    return update

sum_of_middle_page_numbers = 0

for update in pages_to_produce_in_each_update:
    if is_correctly_ordered(update):
        continue
    corrected = correct(update)
    middle_page_number = update[len(update) // 2]
    sum_of_middle_page_numbers += middle_page_number

print(sum_of_middle_page_numbers)
