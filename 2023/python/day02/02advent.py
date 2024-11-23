filename = "input/02_testinput.txt"
filename = "input/02_input.txt"

# Red 0, Green 1, Blue 2

import re as regex
bag = [12, 13, 14]


def check_valid_game(line) -> bool:
    sets = line.split(";")
    for set in sets:
        match = regex.findall(r"\d* red", set)
        if match and int(match[0].split(" ")[0]) > bag[0]:
                return False
        match = regex.findall(r"\d* green", set)
        if match and int(match[0].split(" ")[0]) > bag[1]:
                return False
        match = regex.findall(r"\d* blue", set)
        if match and int(match[0].split(" ")[0]) > bag[2]:
            return False
    return True

def lowest_timed(line) -> bool:
    sets = line.split(";")
    lowest_bag = [-1, -1, -1]
    for set in sets:
        match = regex.findall(r"\d* red", set)
        if match:
            red = int(match[0].split(" ")[0])
            if red > lowest_bag[0]:
                lowest_bag[0] = red
        match = regex.findall(r"\d* green", set)
        if match:
            green = int(match[0].split(" ")[0])
            if green > lowest_bag[1]:
                lowest_bag[1] = green
        match = regex.findall(r"\d* blue", set)
        if match:
            blue = int(match[0].split(" ")[0])
            if blue > lowest_bag[2]:
                lowest_bag[2] = blue
    return lowest_bag[0] * lowest_bag[1] * lowest_bag[2]

with open(filename) as f:
    liste = f.read().splitlines()
    result_sum = 0
    for index, line in enumerate(liste):
        # if(check_valid_game(line)):
        #     result_sum += index + 1
        result_sum += lowest_timed(line)

    print(result_sum)