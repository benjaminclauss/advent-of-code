import re

file_path = "input3.txt"

with open(file_path, "r") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    # Initialize the matrix dimensions
    rows = len(lines)
    columns = len(lines[0])
    # Create the matrix filled with False values
    matrix = [[False for _ in range(columns)] for _ in range(rows)]

    def infect(row, col):
        if row < 0 or row == rows:
            return
        if col < 0 or col == columns:
            return
        if matrix[row][col] == True:
            return
        if lines[row][col] == '.':
            return
        matrix[row][col] = True
        if lines[row][col].isdigit():
            infect(row, col - 1)
            infect(row, col + 1)
        else:
            infect(row -1, col -1)
            infect(row - 1, col)
            infect(row - 1, col + 1)
            infect(row, col -1)
            infect(row, col + 1)
            infect(row + 1, col -1)
            infect(row + 1, col)
            infect(row + 1, col + 1)

    for row in range(rows):
        for col in range(columns):
            if lines[row][col] != '.' and not lines[row][col].isdigit():
                infect(row, col)

    for row in range(rows):
        for col in range(columns):
            valid = matrix[row][col]
            if not valid or not lines[row][col].isdigit():
                matrix[row][col] = '.'
            else:
                matrix[row][col] = lines[row][col]
    
    part_sum = 0
    for line in matrix:
        joined = ''.join(line)
        split_text = re.split("\.+", joined)
        for part in split_text:
            if len(part) == 0:
                continue
            part_sum += int(part)
    
    print(part_sum)

with open(file_path, "r") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    rows = len(lines)
    columns = len(lines[0])

    def numbers_above(row, col):
        if row - 1 < 0:
            return 0
        left, middle, right = '.', '.', '.'
        if col - 1 >= 0:
            left = lines[row - 1][col - 1]
        middle = lines[row - 1][col]
        if col + 1 < columns:
            right = lines[row - 1][col + 1]
        if left.isdigit() and not middle.isdigit() and right.isdigit():
            return 2
        if left.isdigit() or middle.isdigit() or right.isdigit():
            return 1
        return 0

    def numbers_below(row, col):
        if row + 1 >= rows:
            return 0
        left, middle, right = '.', '.', '.'
        if col - 1 >= 0:
            left = lines[row + 1][col - 1]
        middle = lines[row + 1][col]
        if col + 1 < columns:
            right = lines[row + 1][col + 1]
        if left.isdigit() and not middle.isdigit() and right.isdigit():
            return 2
        if left.isdigit() or middle.isdigit() or right.isdigit():
            return 1
        return 0
    
    def numbers_left(row, col):
        if col - 1 < 0:
            return 0
        if lines[row][col - 1].isdigit():
            return 1
        return 0
    
    def numbers_right(row, col):
        if col + 1 >= columns:
            return 0
        if lines[row][col + 1].isdigit():
            return 1
        return 0
    
    def parse_number(row, col):
        if row < 0 or row >= rows:
            return None
        if col < 0 or col >= columns:
            return None
        if not lines[row][col].isdigit():
            return None
        
        start = col
        while start > 0 and lines[row][start -1].isdigit():
            start -= 1

        end = start + 1
        while end < columns and lines[row][end].isdigit():
            end += 1

        num = ''
        for i in range(start, end):
            num += lines[row][i]
        return int(num)

    total = 0

    for row in range(rows):
        for col in range(columns):
            if lines[row][col] == '*':
                above, below = numbers_above(row, col), numbers_below(row, col)
                left, right = numbers_left(row, col), numbers_right(row, col)
                if sum([above, below, left, right]) == 2:
                    nums = set()
                    nums.add(parse_number(row - 1, col - 1))
                    nums.add(parse_number(row - 1, col))
                    nums.add(parse_number(row - 1, col + 1))
                    nums.add(parse_number(row, col - 1))
                    nums.add(parse_number(row, col + 1))
                    nums.add(parse_number(row + 1, col - 1))
                    nums.add(parse_number(row + 1, col))
                    nums.add(parse_number(row + 1, col + 1))
                    nums.remove(None)
                    gear_ratio = list(nums)[0] * list(nums)[1]
                    total += gear_ratio
    
    print(total)

