file_path = 'input13.txt'

patterns = list()
with open(file_path, 'r') as file:
    lines = [line.strip() for line in file.readlines()]
    current_pattern = list()
    for line in lines:
        if line.strip() == '':
            patterns.append(current_pattern)
            current_pattern = list()
        else:
            current_pattern.append(line)
    patterns.append(current_pattern)

def column(pattern, index):
    c = ''
    for row in range(len(pattern)):
        c += pattern[row][index]
    return c

def find_vertical_reflection(pattern):
    for middle_of_pattern in range(1, len(pattern[0])):
        left = middle_of_pattern - 1
        right = middle_of_pattern
        
        pattern_found = True
        while left > -1 and right < len(pattern[0]):
            left_column = column(pattern, left)
            right_column = column(pattern, right)
            if left_column != right_column:
                pattern_found = False
                break
            left -= 1
            right += 1
        if pattern_found:
            return middle_of_pattern

    return None

def find_horizontal_reflection(pattern):
    for middle_of_pattern in range(1, len(pattern)):
        above = middle_of_pattern - 1
        below = middle_of_pattern
        
        pattern_found = True
        while above > -1 and below < len(pattern):
            above_row = pattern[above]
            below_row = pattern[below]
            if above_row != below_row:
                pattern_found = False
                break
            above -= 1
            below += 1
        if pattern_found:
            return middle_of_pattern

    return None

original_patterns = list()
for pattern in patterns:
    original_patterns.append((find_vertical_reflection(pattern), find_horizontal_reflection(pattern)))

sum_of_lines = 0
for pattern in original_patterns:
    vertical, horizontal = pattern
    if vertical is not None:
        sum_of_lines += vertical
    else:
        sum_of_lines += (100 * horizontal)

print(sum_of_lines)
print()

def smudge_factor(a, b):
    smudge = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            smudge += 1
    return smudge

def find_vertical_reflection_with_smudge(pattern):
    patterns = list()
    for middle_of_pattern in range(1, len(pattern[0])):
        left = middle_of_pattern - 1
        right = middle_of_pattern
        
        pattern_found = True
        already_smudged = False
        while left > -1 and right < len(pattern[0]):
            left_column = column(pattern, left)
            right_column = column(pattern, right)
            if left_column != right_column:
                if already_smudged:
                    pattern_found = False
                    break
                elif smudge_factor(left_column, right_column) == 1:
                    already_smudged = True
                else:
                    pattern_found = False
                    break
            left -= 1
            right += 1
        if pattern_found:
            patterns.append((middle_of_pattern, already_smudged))

    return patterns

def find_horizontal_reflection_with_smudge(pattern):
    patterns = list()
    for middle_of_pattern in range(1, len(pattern)):
        above = middle_of_pattern - 1
        below = middle_of_pattern
        
        pattern_found = True
        already_smudged = False
        while above > -1 and below < len(pattern):
            above_row = pattern[above]
            below_row = pattern[below]
            if above_row != below_row:
                if already_smudged:
                    pattern_found = False
                    break
                elif smudge_factor(above_row, below_row) == 1:
                    already_smudged = True
                else:
                    pattern_found = False
                    break
            above -= 1
            below += 1
        if pattern_found:
            patterns.append((middle_of_pattern, already_smudged))

    return patterns
 
new_sum = 0 
for i in range(len(patterns)):
    pattern = patterns[i]
    vertical_patterns = find_vertical_reflection_with_smudge(pattern)
    horizontal_patterns = find_horizontal_reflection_with_smudge(pattern)
    for v in vertical_patterns:
        val, smudged = v
        if smudged:
            new_sum += val
    for h in horizontal_patterns:
        val, smudged = h
        if smudged:
            new_sum += (100 * val)

print(new_sum)