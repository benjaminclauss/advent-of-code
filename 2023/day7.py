file_path = "input7.txt"

from collections import Counter
from functools import cmp_to_key

cards = 'AKQJT98765432'[::-1]
card_ratings = {}
for i, char in enumerate(cards):
    card_ratings[char] = i

def compare_card_ratings(hand1, hand2):
    for card_index in range(5):
        card1_rating = card_ratings[hand1[0][card_index]]
        card2_rating = card_ratings[hand2[0][card_index]]
        if card1_rating > card2_rating:
            return 1
        elif card2_rating > card1_rating:
            return -1
    return 0

def hand_type(hand):
    counts = hand[2].most_common()
    if len(counts) == 1:
        # five of a kind
        return 7
    if len(counts) == 2 and counts[0][1] == 4:
        # four of a kind
        return 6
    if len(counts) == 2 and counts[0][1] == 3 and counts[1][1] == 2:
        # full house
        return 5
    if len(counts) == 3 and counts[0][1] == 3:
        # three of a kind
        return 4
    if len(counts) == 3 and counts[0][1] == 2 and counts[1][1] == 2:
        # two pair
        return 3
    if counts[0][1] == 2:
        # one pair
        return 2
    return 1

def compare(hand1, hand2):
    hand1_type_ranking = hand_type(hand1)
    hand2_type_ranking = hand_type(hand2)
    if hand1_type_ranking > hand2_type_ranking:
        return 1
    elif hand2_type_ranking > hand1_type_ranking:
        return -1
    else:
        return compare_card_ratings(hand1, hand2)

with open(file_path, "r") as file:
    lines = [line.strip() for line in file.readlines()]
    hands = [line.split() for line in lines]
   
    hands_with_counts = list()
    for hand in hands:
        c = Counter(list(hand[0]))
        hands_with_counts.append((hand[0], hand[1], c))
    
    # Sort hands from weakest to strongest.
    rank = 1
    total_winnings = 0
    for hand in sorted(hands_with_counts, key=cmp_to_key(compare)):
        bid = int(hand[1])
        total_winnings += (bid * rank)
        rank+=1
    print(total_winnings)

    # Again, but with new rules.
    # Move J to bottom.
    cards = 'AKQT98765432J'[::-1]
    card_ratings = {}
    for i, char in enumerate(cards):
        card_ratings[char] = i
    
    hands_with_counts = list()
    for hand in hands:
        c = Counter(list(hand[0]))
        if hand[0] != 'JJJJJ':
            number_of_jokers = c['J']
            c['J'] -= number_of_jokers
            del c['J']
            most_common_card = c.most_common(1)[0][0]
            c[most_common_card] += number_of_jokers
            hands_with_counts.append((hand[0], hand[1], c))
        else: 
            hands_with_counts.append((hand[0], hand[1], c))
        
    # Sort hands from weakest to strongest.
    rank = 1
    total_winnings = 0
    for hand in sorted(hands_with_counts, key=cmp_to_key(compare)):
        bid = int(hand[1])
        total_winnings += (bid * rank)
        rank+=1
    print(total_winnings)