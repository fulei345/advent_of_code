#filename = "input/test1_2.txt"
# filename = "input/test1.txt"
filename = "input/input1.txt"

import re as regex

dictionary : dict = {"one": "1","two": "2",
                     "three": "3","four": "4",
                     "five": "5","six": "6",
                     "seven": "7", "eight": "8",
                     "nine": "9"}

def main(file: str) -> int:
    liste : list[str] = f.read().splitlines()
    result_sum : int = 0
    for line in liste:
        first = ""
        first_index = 99
        last = ""
        last_index = -1
    for index, char in enumerate(line):
        if char.isdigit():
            if index < first_index:
                first = char
                first_index = index
            if index > last_index:
                last = char
                last_index = index
        result_sum += int(first + last)
    return result_sum

with open(filename) as f:
    liste = f.read().splitlines()
    result_sum = 0
    for line in liste:
        first = ""
        first_index = 99
        last = ""
        last_index = -1
        for num in dictionary.keys():
            for match in regex.finditer(num, line):
                index = match.start()
                if index < first_index:
                    first = dictionary[num]
                    first_index = index
                if index > last_index:
                    last = dictionary[num]
                    last_index = index
        for index, char in enumerate(line):
            if char.isdigit():
                if index < first_index:
                    first = char
                    first_index = index
                if index > last_index:
                    last = char
                    last_index = index
        result_sum += int(first + last)
        print(line + " " + first + " " + last)

if __name__ == "__main__":
    main("test01.txt")
    main("test01_2.txt")
    main("input01_txt")