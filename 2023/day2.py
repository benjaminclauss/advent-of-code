from collections import defaultdict
file_path = "input2.txt"


def parse_rounds(rounds):
    rounds = rounds.strip()
    individual_rounds = rounds.split("; ")
    parsed_rounds = list()
    for round in individual_rounds:
        marble_breakdown = round.split(", ")
        parsed_round = defaultdict(int)
        for marbles in marble_breakdown:
            marbles = marbles.strip()
            number, color = marbles.split(" ")
            parsed_round[color] = int(number)
        parsed_rounds.append(parsed_round)
    return parsed_rounds


with open(file_path, "r") as file:
    lines = file.readlines()

    sum_possible = 0
    for line in lines:
        line = line.strip()
        game, rounds = line.split(": ")
        game_id = int(game.split(" ")[1])
        parsed_rounds = parse_rounds(rounds)
        possible = True
        for round in parsed_rounds:
            if round["red"] > 12:
                possible = False
                break
            if round["green"] > 13:
                possible = False
                break
            if round["blue"] > 14:
                possible = False
                break
        if possible:
            sum_possible += game_id

    print(sum_possible)

with open(file_path, "r") as file:
    lines = file.readlines()

    sum_power_sets = 0
    for line in lines:
        line = line.strip()
        game, rounds = line.split(": ")
        game_id = int(game.split(" ")[1])
        parsed_rounds = parse_rounds(rounds)
        print(line)
        min_red, min_green, min_blue = 0, 0, 0
        for round in parsed_rounds:
            min_red = max(min_red, round["red"])
            min_green = max(min_green, round["green"])
            min_blue = max(min_blue, round["blue"])
        power = min_red * min_green * min_blue
        sum_power_sets += power
        print(min_red)
        print(min_green)
        print(min_blue)
    print(sum_power_sets)
