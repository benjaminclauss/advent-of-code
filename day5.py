file_path = "input5.txt"

from collections import defaultdict

with open(file_path, "r") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    seeds = [int(s) for s in lines[0].split(' ')[1:]]
    
    # Build maps.
    maps = defaultdict(list)
    current_map = None
    for line in lines[1:]:
        if len(line) == 0:
            continue
        elif 'map' in line:
            current_map = line.split('-')[0]
        else:
            numbers = [int(n) for n in line.split()]
            maps[current_map].append(numbers)
     
    # Determine minimum location.

    minimum_location = None
    
    for seed_number in seeds:
        current_number = seed_number
        for map_type in ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity']:
            # print(map_type)
            # print(current_number)

            map_ranges = maps[map_type]

            # Any source numbers that aren't mapped correspond to the same destination number.
            next_destination_number = current_number

            for map_range in map_ranges:
                # if in range, map and break
                destination_range_start, source_range_start, range_length = map_range
                if current_number >= source_range_start and current_number <= source_range_start + range_length:
                    difference = current_number - source_range_start
                    next_destination_number = destination_range_start + difference
                    break
            
            current_number = next_destination_number
        
        if minimum_location is None:
            minimum_location = current_number
        else:
            minimum_location = min(minimum_location, current_number)
        # print('location')
        # print(current_number)
        # print()
    
    print(minimum_location)

with open(file_path, "r") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    seeds = [int(s) for s in lines[0].split(' ')[1:]]
    seed_ranges = numbers = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]

    maps = defaultdict(list)
    current_map = None
    for line in lines[1:]:
        if len(line) == 0:
            continue
        elif 'map' in line:
            current_map = line.split('-')[2].rstrip(' map:')
        else:
            numbers = [int(n) for n in line.split()]
            maps[current_map].append(numbers)
    
    found_seed_number = False
    location_guess = 15290000
    
    while not found_seed_number:
        current_number = location_guess
        
        # Any source numbers that aren't mapped correspond to the same destination number.
        next_destination_number = current_number

        for map_type in ['location', 'humidity', 'temperature', 'light', 'water', 'fertilizer', 'soil']:
            map_ranges = maps[map_type]

            for map_range in map_ranges:
                destination_range_start, source_range_start, range_length = map_range
                # Now, we need to go in reverse!
                if current_number >= destination_range_start and current_number <= destination_range_start + range_length:
                    difference = current_number - destination_range_start
                    next_destination_number = source_range_start + difference
                    break

            current_number = next_destination_number

        # Check if number is in seed ranges.
        for seed_range in seed_ranges:
            seed_range_start, seed_range_size = seed_range
            if current_number >= seed_range_start and current_number < seed_range_start + seed_range_size:
                found_seed_number = True
                print('Location: ' + str(location_guess))
                print('Seed: ' + str(current_number))

        # We didn't find it! Increment.
        location_guess += 1
        if location_guess % 10000 == 0:
            print(location_guess)
