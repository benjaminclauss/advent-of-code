file_path = "input8.txt"

import math

with open(file_path, "r") as file:
    lines = [line.strip() for line in file.readlines()]
    
    instructions = lines[0].replace('L', '0').replace('R', '1')

    nodes = {}
    for line in lines[2:]:
        node, paths = line.split(' = ')
        nodes[node] = paths.lstrip('(').rstrip(')').split(', ')
    
    # Part 1
    if 'AAA' in nodes:
        step = 0
        current_node = 'AAA'
        while True:
            if current_node == 'ZZZ':
                break
            paths_for_node = nodes[current_node]
            move = int(instructions[step % len(instructions)])
            current_node = paths_for_node[move]
            step += 1
        
        print(step)
   
    # Part 2
    a_nodes = list(filter(lambda n: n.endswith('A'), nodes))
    steps = list()
    for a_node in a_nodes:
        step = 0
        current_node = a_node
        while True:
            if current_node.endswith('Z'):
                break
            paths_for_node = nodes[current_node]
            move = int(instructions[step % len(instructions)])
            current_node = paths_for_node[move]
            step += 1
        steps.append(step)
    
    print(math.lcm(*steps))
    
    
    
        