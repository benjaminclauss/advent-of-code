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
        number_of_steps = 0
        current_node = 'AAA'
        while not current_node == 'ZZZ':
            paths_for_node = nodes[current_node]
            move = int(instructions[number_of_steps % len(instructions)])
            current_node = paths_for_node[move]
            number_of_steps += 1
        
        print(number_of_steps)
   
    # Part 2
    a_nodes = list(filter(lambda n: n.endswith('A'), nodes))
    steps = list()
    for a_node in a_nodes:
        number_of_steps = 0
        current_node = a_node
        while not current_node.endswith('Z'):
            paths_for_node = nodes[current_node]
            move = int(instructions[number_of_steps % len(instructions)])
            current_node = paths_for_node[move]
            number_of_steps += 1
        steps.append(number_of_steps)
    
    print(math.lcm(*steps))
    
    
    
        