
with open("input16.txt", "r") as file:
    file_content = file.read()
lines = file_content.splitlines()

grid = []
for line in lines:
    characters = list(line)
    grid.append(characters)
    r = list()
    for i in range(len(characters)):
        r.append(set())


NUMBER_OF_ROWS = len(grid)
NUMBER_OF_COLUMNS = len(grid[0])

def caclulate_energized(initial_row, initial_column, direction):
    energized = []
    for r in range(NUMBER_OF_ROWS):
        r = list()
        for c in range(NUMBER_OF_COLUMNS):
            r.append(set())
        energized.append(r)

    stack = [((initial_row, initial_column), direction)]
    while len(stack) > 0:
        beam = stack.pop()
        row, column = beam[0]
        direction = beam[1]
        
        if row < 0 or row >= NUMBER_OF_ROWS:
            continue
        if column < 0 or column >= NUMBER_OF_COLUMNS:
            continue
        
        already_energized = energized[row][column]
        if direction in already_energized:
            continue
        energized[row][column].add(direction)

        space = grid[row][column]

        if direction == 'right':
            if space == '.':
                stack.append(((row, column + 1), 'right'))
            elif space == '/':
                stack.append(((row - 1, column), 'up'))
            elif space == '\\':
                stack.append(((row + 1, column), 'down'))
            elif space == '|':
                stack.append(((row - 1, column), 'up'))  
                stack.append(((row + 1, column), 'down'))
            elif space == '-':
                stack.append(((row, column + 1), 'right'))
        elif direction == 'left':
            if space == '.':
                stack.append(((row, column - 1), 'left'))
            elif space == '/':
                stack.append(((row + 1, column), 'down'))
            elif space == '\\':
                stack.append(((row - 1, column), 'up'))
            elif space == '|':
                stack.append(((row - 1, column), 'up'))  
                stack.append(((row + 1, column), 'down'))
            elif space == '-':
                stack.append(((row, column - 1), 'left'))
        elif direction == 'up':
            if space == '.':
                stack.append(((row - 1, column), 'up'))
            elif space == '/':
                stack.append(((row, column + 1), 'right'))
            elif space == '\\':
                stack.append(((row, column - 1), 'left'))
            elif space == '|':
                stack.append(((row - 1, column), 'up'))  
            elif space == '-':
                stack.append(((row, column - 1), 'left'))
                stack.append(((row, column + 1), 'right'))
        elif direction == 'down':
            if space == '.':
                stack.append(((row + 1, column), 'down'))
            elif space == '/':
                stack.append(((row, column - 1), 'left'))
            elif space == '\\':
                stack.append(((row, column + 1), 'right'))
            elif space == '|':
                stack.append(((row + 1, column), 'down'))  
            elif space == '-':
                stack.append(((row, column - 1), 'left'))
                stack.append(((row, column + 1), 'right'))
                
    total_energized = 0
    for row in range(NUMBER_OF_ROWS):
        for column in range(NUMBER_OF_COLUMNS):
            if len(energized[row][column]) > 0:
                total_energized += 1
    
    return total_energized

max_energized = 0
for column in range(NUMBER_OF_COLUMNS):
    max_energized = max(max_energized, caclulate_energized(0, column, 'down'))
for column in range(NUMBER_OF_COLUMNS):
    max_energized = max(max_energized, caclulate_energized(NUMBER_OF_ROWS - 1, column, 'up'))
for row in range(NUMBER_OF_ROWS):
    max_energized = max(max_energized, caclulate_energized(row, 0, 'right'))
for column in range(NUMBER_OF_COLUMNS):
    max_energized = max(max_energized, caclulate_energized(row, NUMBER_OF_COLUMNS - 1, 'left'))

print(max_energized)