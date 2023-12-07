file_path = "input4.txt"

with open(file_path, "r") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    points = 0

    for line in lines:
        card, numbers = line.split(': ')
        left_numbers, right_numbers = numbers.split(' | ')
        winning_numbers = set(map(int, left_numbers.split()))
        numbers_you_have = set(map(int, right_numbers.split()))
        matching_numbers = numbers_you_have.intersection(winning_numbers)
        winning_card = len(matching_numbers) > 0 
        if winning_card:
            card_points = 2 ** (len(matching_numbers) - 1)
            points += card_points
    
    print(points)


import queue
from collections import defaultdict

with open(file_path, "r") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    points = 0
    number_of_original_cards = len(lines)

    cards_to_number_of_matching_cards = defaultdict(int)
    for l in lines:
        card, numbers = l.split(': ')
        card_number = int(card.split()[1])
        left_numbers, right_numbers = numbers.split(' | ')
        winning_numbers = set(map(int, left_numbers.split()))
        numbers_you_have = set(map(int, right_numbers.split()))
        number_of_matching_numbers = len(numbers_you_have.intersection(winning_numbers))
        cards_to_number_of_matching_cards[card_number] = number_of_matching_numbers
    
    card_queue = queue.Queue()

    for card_number in range(1, number_of_original_cards + 1):
        card_queue.put(card_number)
    
    total_scratchcards = 0
    while not card_queue.empty():
        card_number = card_queue.get()
        total_scratchcards += 1
        number_of_matching_numbers_for_card = cards_to_number_of_matching_cards[card_number]
        if number_of_matching_numbers_for_card == 0:
            continue
        else:
            for copy_card_number in range(card_number + 1, card_number + number_of_matching_numbers_for_card + 1):
                card_queue.put(copy_card_number)

    # This is not very quick!
    print(total_scratchcards)
