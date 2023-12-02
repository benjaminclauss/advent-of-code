file_path = "input.txt"

with open(file_path, "r") as file:
    lines = file.readlines()
    calibration_value_sum = 0

    for line in lines:
        digits = ""
        for character in line.strip():
            if character.isdigit():
                digits += character

        first_digit = digits[0]
        last_digit = digits[len(digits) - 1]
        calibration_value = 10 * int(first_digit) + int(last_digit)
        calibration_value_sum += calibration_value

    print(calibration_value_sum)

    file.seek(0)

    calibration_value_sum = 0
    number_map = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    for line in lines:
        new_line = ""

        left_digit = -1
        for i in range(len(line.strip())):
            substr = line.strip()[i:]
            for key, val in number_map.items():
                if substr.startswith(key):
                    left_digit = val
                    break
            if left_digit > 0:
                break
            if line[i].isdigit():
                left_digit = int(line[i])
                break

        right_digit = -1
        for i in range(len(line.strip()) - 1, -1, -1):
            substr = line.strip()[:(i+1)]
            for key, val in number_map.items():
                if substr.endswith(key):
                    right_digit = val
                    break
            if right_digit > 0:
                break
            if line[i].isdigit():
                right_digit = int(line[i])
                break

        calibration_value_sum += (10 * left_digit + right_digit)

    print(calibration_value_sum)
