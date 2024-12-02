file_path = "input6.txt"

import math

def determine_number_of_ways_to_win(times, distances):
    number_of_ways_to_win = list()
    for race_number in range(len(distances)):
        number_of_ways_to_win_race = 0

        time, distance_to_beat = times[race_number], distances[race_number]
        for hold_time in range(time + 1):
            velocity = hold_time
            distance_for_hold_time = (time - hold_time) * velocity
            if distance_for_hold_time > distance_to_beat:
                number_of_ways_to_win_race += 1
            
        number_of_ways_to_win.append(number_of_ways_to_win_race)
    return number_of_ways_to_win

with open(file_path, "r") as file:
    lines = [line.strip() for line in file.readlines()]
    times = [int(t) for t in lines[0].split(':')[1].split()]
    distances = [int(d) for d in lines[1].split(':')[1].split()]

    number_of_ways_to_win_multiple_races = determine_number_of_ways_to_win(times, distances)
    print(math.prod(number_of_ways_to_win_multiple_races))

    single_time = int(''.join([str(t) for t in times]))
    single_distance = int(''.join([str(d) for d in distances]))
    print(determine_number_of_ways_to_win([single_time], [single_distance])[0])