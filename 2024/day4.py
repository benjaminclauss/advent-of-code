
with open("input4.txt", "r") as file:
    puzzle_input = file.readlines()

word_search = []
for line in puzzle_input:
    word_search.append(list(line.strip()))

# Part 1

def char_is(r, c, char):
    if r not in range(len(word_search)) or c not in range(len(word_search[r])):
        return False
    return word_search[r][c] == char

def upper_left_xmas(r, c):
    return char_is(r, c, 'X') and char_is(r-1, c-1, 'M') and char_is(r-2, c-2, 'A') and char_is(r-3, c-3, 'S')

def up_xmas(r, c):
    return char_is(r, c, 'X') and char_is(r-1, c, 'M') and char_is(r-2, c, 'A') and char_is(r-3, c, 'S')

def upper_right_xmas(r, c):
    return char_is(r, c, 'X') and char_is(r-1, c+1, 'M') and char_is(r-2, c+2, 'A') and char_is(r-3, c+3, 'S')

def left_xmas(r, c):
    return char_is(r, c, 'X') and char_is(r, c-1, 'M') and char_is(r, c-2, 'A') and char_is(r, c-3, 'S')

def right_xmas(r, c):
    return char_is(r, c, 'X') and char_is(r, c+1, 'M') and char_is(r, c+2, 'A') and char_is(r, c+3, 'S')

def lower_left_xmas(r, c):
    return char_is(r, c, 'X') and char_is(r+1, c-1, 'M') and char_is(r+2, c-2, 'A') and char_is(r+3, c-3, 'S')

def down_xmas(r, c):
    return char_is(r, c, 'X') and char_is(r+1, c, 'M') and char_is(r+2, c, 'A') and char_is(r+3, c, 'S')

def lower_right_xmas(r, c):
    return char_is(r, c, 'X') and char_is(r+1, c+1, 'M') and char_is(r+2, c+2, 'A') and char_is(r+3, c+3, 'S')

total = 0
for r in range(len(word_search)):
    for c in range(len(word_search[r])):
        if upper_left_xmas(r, c):
            total += 1
        if up_xmas(r, c):
            total += 1
        if upper_right_xmas(r, c):
            total += 1
        if left_xmas(r, c):
            total += 1
        if right_xmas(r, c):
            total += 1
        if lower_left_xmas(r, c):
            total += 1
        if down_xmas(r, c):
            total += 1
        if lower_right_xmas(r, c):
            total += 1

print(total)

# Part 2

def upper_left_mas(r, c):
    return char_is(r-1, c-1, 'M') and char_is(r, c, 'A') and char_is(r+1, c+1, 'S')

# def up_mas(r, c):
#     return char_is(r-1, c, 'M') and char_is(r, c, 'A') and char_is(r+1, c, 'S')

def upper_right_mas(r, c):
    return char_is(r-1, c+1, 'M') and char_is(r, c, 'A') and char_is(r+1, c-1, 'S')

# def left_mas(r, c):
#     return char_is(r, c-1, 'M') and char_is(r, c, 'A') and char_is(r, c+1, 'S')

# def right_mas(r, c):
#     return char_is(r, c+1, 'M') and char_is(r, c, 'A') and char_is(r, c-1, 'S')

def lower_left_mas(r, c):
    return char_is(r+1, c-1, 'M') and char_is(r, c, 'A') and char_is(r-1, c+1, 'S')

# def down_mas(r, c):
#     return char_is(r+1, c, 'M') and char_is(r, c, 'A') and char_is(r-1, c, 'S')

def lower_right_mas(r, c):
    return char_is(r+1, c+1, 'M') and char_is(r, c, 'A') and char_is(r-1, c-1, 'S')

total = 0
for r in range(len(word_search)):
    for c in range(len(word_search[r])):
        total_for_position = 0 
        if upper_left_mas(r, c):
            total_for_position += 1
        # if up_mas(r, c):
        #     total_for_position += 1
        if upper_right_mas(r, c):
            total_for_position += 1
        # if left_mas(r, c):
        #     total_for_position += 1
        # if right_mas(r, c):
        #     total_for_position += 1
        if lower_left_mas(r, c):
            total_for_position += 1
        # if down_mas(r, c):
        #     total_for_position += 1
        if lower_right_mas(r, c):
            total_for_position += 1
        if total_for_position >= 2:
            total += 1

print(total)