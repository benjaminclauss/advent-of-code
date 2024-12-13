def calculate_price(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    # Direction vectors for moving up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Function to perform DFS and calculate area and perimeter for a region
    def dfs(x, y, plant_type, visited):
        stack = [(x, y)]
        visited[x][y] = True
        area = 0
        perimeter = 0
        
        while stack:
            cx, cy = stack.pop()
            area += 1
            # Check the four neighbors to calculate the perimeter
            local_perimeter = 0
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                    local_perimeter += 1  # Outside the grid
                elif grid[nx][ny] != plant_type:
                    local_perimeter += 1  # Edge with a different region
                elif not visited[nx][ny] and grid[nx][ny] == plant_type:
                    visited[nx][ny] = True
                    stack.append((nx, ny))
            
            perimeter += local_perimeter
        
        return area, perimeter
    
    visited = [[False] * cols for _ in range(rows)]
    total_price = 0
    
    # Iterate over all plots in the grid
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                plant_type = grid[i][j]
                area, perimeter = dfs(i, j, plant_type, visited)
                total_price += area * perimeter
    
    return total_price

def read_input(filename):
    """Reads the grid from the given file and returns it as a list of lists of characters."""
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file.readlines()]
    return grid


# Example usage:
filename = 'input12.txt'  # Change this to the path of your input file
grid = read_input(filename)

# Calculate the total price of fencing all regions
total_price = calculate_price(grid)
print(f"Total price of fencing: {total_price}")
