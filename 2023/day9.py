file_path = "input9.txt"

def extrapolate(sequence):
    sequences = [sequence]
    while not all(number == 0 for number in sequences[-1]):
        current_sequence = sequences[-1]
        next_sequence = []
        for i in range(1, len(current_sequence)):
            next_sequence.append(current_sequence[i] - current_sequence[i - 1])
        sequences.append(next_sequence)
    
    return sequences

def extrapolate_forwards(sequence):
    sequences = extrapolate(sequence)
    
    previous_placeholder = 0
    for sequence in reversed(sequences[:-1]):
        value_to_left = sequence[-1]
        value_below = previous_placeholder
        previous_placeholder = (value_to_left + value_below)
    
    return previous_placeholder

def extrapolate_backwards(sequence):
    sequences = extrapolate(sequence)

    previous_placeholder = 0
    for sequence in reversed(sequences[:-1]):
        value_to_right = sequence[0]
        value_below = previous_placeholder
        previous_placeholder = (value_to_right - value_below)
    
    return previous_placeholder

with open(file_path, "r") as file:
    lines = [line.strip() for line in file.readlines()]
    
    sequences = list()
    for line in lines:
        sequences.append([int(n) for n in line.split()]) 
    
    print(sum(map(extrapolate_forwards, sequences)))
    print(sum(map(extrapolate_backwards, sequences)))