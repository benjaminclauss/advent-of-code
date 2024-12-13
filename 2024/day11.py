def transform_stones(stones):
    new_stones = []
    
    for stone in stones:
        # Rule 1: If stone is 0, it becomes 1
        if stone == 0:
            new_stones.append(1)
        # Rule 2: If stone has an even number of digits, split it
        elif len(str(stone)) % 2 == 0:
            str_stone = str(stone)
            mid = len(str_stone) // 2
            left = int(str_stone[:mid])
            right = int(str_stone[mid:])
            new_stones.append(left)
            new_stones.append(right)
        # Rule 3: Otherwise, multiply the stone by 2024
        else:
            new_stones.append(stone * 2024)
    
    return new_stones

def count_stones_after_blinks(initial_stones, blinks):
    stones = initial_stones
    for blink in range(blinks):
        # print(len(stones))
        # print(blink)
        stones = transform_stones(stones)
    return len(stones)

# Example usage:

initial_stones = [1117, 0, 8, 21078, 2389032, 142881, 93, 385]  # This would be your input list
# initial_stones = [125, 17]
blinks = 25
result = count_stones_after_blinks(initial_stones, blinks)
print(f"Number of stones after {blinks} blinks: {result}")

from collections import Counter

def blink_stones_count(stones_count):
    new_stones_count = Counter()
    
    for stone, count in stones_count.items():
        if stone == 0:
            # Rule 1: Stone with 0 becomes 1
            new_stones_count[1] += count
        else:
            stone_str = str(stone)
            if len(stone_str) % 2 == 0:
                # Rule 2: Stone with even number of digits splits
                mid = len(stone_str) // 2
                left = int(stone_str[:mid])
                right = int(stone_str[mid:])
                new_stones_count[left] += count
                new_stones_count[right] += count
            else:
                # Rule 3: Stone is multiplied by 2024
                new_stones_count[stone * 2024] += count
    
    return new_stones_count

def count_stones_after_blinks(initial_stones, blinks):
    # Convert the initial stones into a frequency count
    stones_count = Counter(initial_stones)
    
    for _ in range(blinks):
        stones_count = blink_stones_count(stones_count)
    
    # Return the total number of stones after the blinks
    return sum(stones_count.values())

# Get the result after 75 blinks
result = count_stones_after_blinks(initial_stones, blinks)
print("Number of stones after 75 blinks:", result)