file_path = "input10.txt"

# Read input.
lines = list()
with open(file_path, "r") as file:
    lines = [line.strip() for line in file.readlines()]

# Build grid.
grid = list()
for line in lines:
    grid.append(list(line))
num_rows, num_cols = len(grid), len(grid[0])

# Determine Start
start_row, start_col = 0, 0
for row in range(num_rows):
    for col in range(num_cols):
        if grid[row][col] == 'S':
            start_row, start_col = row, col


def connects_to(origin, destination):
    destination_row, destination_col = destination

    north, south = (destination_row - 1, destination_col), (destination_row + 1, destination_col)
    west, east = (destination_row, destination_col - 1), (destination_row, destination_col + 1)

    destination_pipe = grid[destination_row][destination_col]
    if destination_pipe == '|':
        # | is a vertical pipe connecting north and south.
        return origin in [north, south]
    if destination_pipe == '-':
        # - is a horizontal pipe connecting east and west.
        return origin in [east, west]
    if destination_pipe == 'L':
        # L is a 90-degree bend connecting north and east.
        return origin in [north, east]
    if destination_pipe == 'J':
        # J is a 90-degree bend connecting north and west.
        return origin in [north, west]
    if destination_pipe == '7':
        # 7 is a 90-degree bend connecting south and west.
        return origin in [south, west]
    if destination_pipe == 'F':
        # F is a 90-degree bend connecting south and east.
        return origin in [south, east]
    # . is ground; there is no pipe in this tile. 
    return False


start = (start_row, start_col)
north_start, south_start = (start_row - 1, start_col), (start_row + 1, start_col)
west_start, east_start = (start_row, start_col - 1), (start_row, start_col + 1)

# Find first connection.
next_point = None
for point in [north_start, south_start, west_start, east_start]:
    if connects_to(start, point):
        next_point = point
        break

def traverse(from_point, next_point):
    destination_row, destination_col = next_point

    north, south = (destination_row - 1, destination_col), (destination_row + 1, destination_col)
    west, east = (destination_row, destination_col - 1), (destination_row, destination_col + 1)

    destination_pipe = grid[destination_row][destination_col]
    if destination_pipe == '|':
        # | is a vertical pipe connecting north and south.
        if from_point == north:
            return south
        else:
            return north
    if destination_pipe == '-':
        # - is a horizontal pipe connecting east and west.
        if from_point == east:
            return west
        else:
            return east
    if destination_pipe == 'L':
        # L is a 90-degree bend connecting north and east.
        if from_point == north:
            return east
        else:
            return north
    if destination_pipe == 'J':
        # J is a 90-degree bend connecting north and west.
        if from_point == north:
            return west
        else:
            return north
    if destination_pipe == '7':
        # 7 is a 90-degree bend connecting south and west.
        if from_point == south:
            return west
        else:
            return south
    if destination_pipe == 'F':
        # F is a 90-degree bend connecting south and east.
        if from_point == south:
            return east
        else:
            return south
    # . is ground; there is no pipe in this tile. 
    return None

previous_point = start
distance = 0
while next_point != start:
    tmp = next_point
    next_point = traverse(previous_point, next_point)
    previous_point = tmp
    distance += 1

if distance % 2 == 1:
    distance += 1

print(distance / 2)

