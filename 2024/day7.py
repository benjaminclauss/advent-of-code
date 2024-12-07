with open("input7.txt", "r") as file:
    puzzle_input = file.readlines()

equations = []

for line in puzzle_input:
    test_value, numbers = line.split(': ')
    equations.append((int(test_value), list(map(int, numbers.split(' ')))))

# Part 1

total_calibration_result = 0

for equation in equations:
    test_value, numbers = equation
    evaluations = []
    evaluations.append(numbers[0])
    for current_number in numbers[1:]:
        next_evaluations = []
        for previous_evaluation in evaluations:
            addition = previous_evaluation + current_number
            next_evaluations.append(addition)
            multiplication = previous_evaluation * current_number
            next_evaluations.append(multiplication)
        # Remove evaluations exceeding test value.
        # Any addition or multiplication would exceed test value.
        next_evaluations = [evaluation for evaluation in next_evaluations if evaluation <= test_value]
        evaluations = next_evaluations
    
    test_value_evaluation = any(number == test_value for number in evaluations)
    if test_value_evaluation:
        total_calibration_result += test_value

print(total_calibration_result)

# Part 2

total_calibration_result = 0

for equation in equations:
    test_value, numbers = equation
    evaluations = []
    evaluations.append(numbers[0])
    for current_number in numbers[1:]:
        next_evaluations = []
        for previous_evaluation in evaluations:
            addition = previous_evaluation + current_number
            next_evaluations.append(addition)
            multiplication = previous_evaluation * current_number
            next_evaluations.append(multiplication)
            concatenation = int(str(previous_evaluation) + str(current_number))
            next_evaluations.append(concatenation)
        # Remove evaluations exceeding test value.
        # Any addition or multiplication would exceed test value.
        next_evaluations = [evaluation for evaluation in next_evaluations if evaluation <= test_value]
        evaluations = next_evaluations
    
    test_value_evaluation = any(number == test_value for number in evaluations)
    if test_value_evaluation:
        total_calibration_result += test_value

print(total_calibration_result)
