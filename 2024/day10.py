
with open("input10.txt", "r") as file:
    puzzle_input = file.readlines()

matrix = []
for line in puzzle_input:
    matrix.append([int(char) for char in line.strip()])

from collections import defaultdict

def matrix_to_graph(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    graph = defaultdict(list)  # Dictionary to store the graph
    
    # Helper function to check if a position is valid and if the neighbor satisfies +1 condition
    def is_valid_neighbor(r1, c1, r2, c2):
        if 0 <= r2 < rows and 0 <= c2 < cols:
            return matrix[r2][c2] == matrix[r1][c1] + 1
        return False
    
    # Loop through each element of the matrix
    for r in range(rows):
        for c in range(cols):
            current_value = matrix[r][c]
            
            # Check horizontal neighbors.
            if is_valid_neighbor(r, c, r, c - 1):
                graph[(r, c)].append((r, c - 1))
            if is_valid_neighbor(r, c, r, c + 1):
                graph[(r, c)].append((r, c + 1))
            
            # Check vertical neighbors.
            if is_valid_neighbor(r, c, r - 1, c):
                graph[(r, c)].append((r - 1, c))
            if is_valid_neighbor(r, c, r + 1, c):
                graph[(r, c)].append((r + 1, c))
    
    return graph


def find_zero_and_nine_nodes(matrix):
    zero_nodes = []
    nine_nodes = []
    
    # Loop through each element of the matrix
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            value = matrix[r][c]
            
            # If the value is 0, add it to the zero_nodes list
            if value == 0:
                zero_nodes.append((r, c))
            
            # If the value is 9, add it to the nine_nodes list
            elif value == 9:
                nine_nodes.append((r, c))
    
    return zero_nodes, nine_nodes


graph = matrix_to_graph(matrix)

# Print the graph (adjacency list)
# for node, neighbors in graph.items():
#     print(f"Node {node}: {neighbors}")

# Get the nodes that are 0 and 9
zero_nodes, nine_nodes = find_zero_and_nine_nodes(matrix)

# # Print the results
# print("Nodes with 0:", zero_nodes)
# print("Nodes with 9:", nine_nodes)


from collections import deque

def bfs(graph, start, target):
    # Create a queue to manage the nodes to explore
    queue = deque([start])
    
    # Create a set to track visited nodes
    visited = set([start])
    
    # Dictionary to track the path from start to target
    parent = {start: None}
    
    while queue:
        # Dequeue the current node
        node = queue.popleft()
        
        # If we've found the target, reconstruct the path
        if node == target:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]  # Reverse the path to get from start to target
        
        # Explore all neighbors of the current node
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                parent[neighbor] = node
    
    # If we reach here, the target is not reachable from the start
    return None


trailhead_score_sum = 0
for trailhead in zero_nodes:
    score = 0
    for peak in nine_nodes:
        path = bfs(graph, trailhead, peak)
        if path:
            score += 1
    trailhead_score_sum += score

print(trailhead_score_sum) 

# Part 2
def bfs_count_distinct_paths(graph, start, target):
    # Queue stores (current_node, path_taken_to_current_node)
    queue = deque([(start, [start])])
    
    # List to store all distinct paths from start to target
    all_paths = []
    
    while queue:
        current_node, path = queue.popleft()
        
        # If we've reached the target, store the path
        if current_node == target:
            all_paths.append(path)
        
        # Explore all neighbors of the current node
        for neighbor in graph[current_node]:
            # We avoid cycles within the same path by checking if the neighbor is already in the path
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))
    
    # Return the number of distinct paths and the actual paths
    return len(all_paths), all_paths


trailhead_score_sum = 0
for trailhead in zero_nodes:
    score = 0
    for peak in nine_nodes:
        num_paths, paths = bfs_count_distinct_paths(graph, trailhead, peak)
        score += num_paths 
    trailhead_score_sum += score

print(trailhead_score_sum)