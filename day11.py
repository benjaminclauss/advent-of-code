file_path = "input11.txt"

EXPANSION_FACTOR = 1000000

# Read input.
lines = list()
with open(file_path, "r") as file:
    image = [line.strip() for line in file.readlines()]

    # Expand rows.
    expanded_row_indices = list()
    row_index = 0
    while row_index < len(image):
        if image[row_index].count('#') == 0:
            expanded_row_indices.append(row_index)
        row_index += 1
    
    # Expand columns.
    expanded_column_indices = list()
    column_index = 0
    while column_index < len(image[0]):
        column = ''.join([row[column_index] for row in image])
        if column.count('#') == 0:
            expanded_column_indices.append(column_index)
        column_index += 1
    
    galaxies = list()
    for row_index in range(len(image)):
        for column_index in range(len(image[row_index])):
            if image[row_index][column_index] == '#':
                galaxies.append((row_index, column_index))
    
    sum_of_the_shortest_path = 0
    for galaxy_number in range(len(galaxies)):
        for other_galaxy_number in range(galaxy_number + 1, len(galaxies)):
            row_index, column_index = galaxies[galaxy_number]
            other_row_index, other_column_index = galaxies[other_galaxy_number]
            # print(str(galaxy_number + 1) + ' to ' + str(other_galaxy_number + 1))

            row_distance = max(row_index, other_row_index) - min(row_index, other_row_index)
            for expanded_row_index in expanded_row_indices:
                if expanded_row_index in range(min(row_index, other_row_index), max(row_index, other_row_index)):
                    row_distance += (EXPANSION_FACTOR - 1)
            
            column_distance = max(column_index, other_column_index) - min(column_index, other_column_index) 
            for expanded_column_index in expanded_column_indices:
                if expanded_column_index in range(min(column_index, other_column_index), max(column_index, other_column_index)):
                    column_distance += (EXPANSION_FACTOR - 1)
            
            distance = (row_distance + column_distance)
            # print(distance)
            sum_of_the_shortest_path += (row_distance + column_distance)

    print(sum_of_the_shortest_path)