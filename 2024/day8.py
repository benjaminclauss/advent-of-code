with open("input8.txt", "r") as file:
    puzzle_input = file.readlines()
puzzle_input = [line.strip() for line in puzzle_input]

from collections import defaultdict
antennas = defaultdict(list)

y = 0
for line in reversed(puzzle_input):
    x = 0
    for character in line:
        if character != '.':
            antennas[character].append((x, y))
        x += 1
    y += 1

MAX_X = len(puzzle_input[0])
MAX_Y = len(puzzle_input)

def calculate_vector(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return (x2 - x1, y2 - y1)

def calculate_next_point(point, vector):
    x, y = point
    vx, vy = vector
    return (x + vx, y + vy)

import itertools
antinodes = set()

for antenna, antenna_locations in antennas.items():
    antenna_location_pairs = list(itertools.combinations(antenna_locations, 2))
    for pair in antenna_location_pairs:
        point1, point2 = pair
        # Get next point for first antenna.
        v = calculate_vector(point1, point2)
        p = calculate_next_point(point2, v)
        antinodes.add(p)
        # Get next point for second antenna.
        v = calculate_vector(point2, point1)
        p = calculate_next_point(point1, v)
        antinodes.add(p)

points_in_map = [point for point in antinodes if point[0] in range(0, MAX_X) and point[1] in range(0, MAX_Y)]
print(len(points_in_map))