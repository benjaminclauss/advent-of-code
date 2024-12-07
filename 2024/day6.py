with open("input6.txt", "r") as file:
    puzzle_input = file.readlines()

initial_guard_map = []

for line in puzzle_input:
    initial_guard_map.append(list(line.strip()))

initial_guard_position = None

for row in range(len(initial_guard_map)):
    for col in range(len(initial_guard_map[row])):
        if initial_guard_map[row][col] == '^':
            initial_guard_position = (row, col)

# Part 1

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

rotate = {
    UP: RIGHT,
    RIGHT: DOWN,
    DOWN: LEFT,
    LEFT: UP
}

def in_map(position):
    row, col = position
    return row >= 0 and row < len(initial_guard_map) and col >= 0 and col < len(initial_guard_map[row])

def contains_obstacle(position, guard_map):
    if not in_map(position):
        return False
    return guard_map[position[0]][position[1]] == '#'

import copy

guard_position = initial_guard_position
current_direction = UP
guard_map = initial_guard_map
visited_guard_positions = set()

while in_map(guard_position):
    # Mark current position as visited.
    row, col = guard_position
    # guard_map[row][col] = 'X'
    visited_guard_positions.add((row, col))
    
    # Identify next position.
    next_position = (row + current_direction[0], col + current_direction[1])
    
    # If the next position contains an obstacle, the guard must rotate.
    if contains_obstacle(next_position, guard_map):
        current_direction = rotate[current_direction]
        continue
    
    # Otherwise, the guard can continue to move.
    guard_position = next_position


print(len(visited_guard_positions))

# Part 2

annotations = {
    (UP, '.'): '|',
    (UP, '-'): '+',
    (RIGHT, '.'): '-',
    (RIGHT, '|'): '+',
    (DOWN, '.'): '|',
    (DOWN, '-'): '+',
    (LEFT, '.'): '-',
    (LEFT, '|'): '+',
}

def stuck_in_a_loop(guard_map):
    guard_position = initial_guard_position
    current_direction = UP
    visited = set()
    
    while in_map(guard_position):
        row, col = guard_position
        
        # Has the guard been this direction in this position before?
        if (row, col, current_direction) in visited:
            return True
        
        # Mark current position as visited.
        visited.add((row, col, current_direction))
        
        # Identify next position.
        next_position = (row + current_direction[0], col + current_direction[1])

        # If the next position contains an obstacle, the guard must rotate.
        if contains_obstacle(next_position, guard_map):
            current_direction = rotate[current_direction]
            continue

        # Otherwise, the guard can continue to move.
        guard_position = next_position
    
    # The guard exited the map.
    return False 
    

map_with_obstruction = copy.deepcopy(initial_guard_map)

possible_obstructions = 0

# The new obstruction can't be placed at the guard's starting position.
# The guard is there right now and would notice.
visited_guard_positions.remove(initial_guard_position)

# If an obstruction is not in the guard's original path, it cannot create a loop.
for position in visited_guard_positions:
    row, col = position
    # Add obstruction at position.
    map_with_obstruction[row][col] = '#'
    if stuck_in_a_loop(map_with_obstruction):
        possible_obstructions += 1        
    # Remove obstruction.
    map_with_obstruction[row][col] = '.'

print(possible_obstructions)