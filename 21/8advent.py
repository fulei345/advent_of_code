filename = "input8.txt"

with open(filename) as f:
    liste = f.read().splitlines()
    liste = [line.split('|') for line in liste]

    number_list = [line[0] for line in liste]
    four_digit_list = [line[1] for line in liste]
    four_digit_list = [line.split() for line in four_digit_list]
    number_list = [line.split() for line in number_list]

    count = 0
    for line in four_digit_list:
        for num in line:
            if len(num) < 5 or len(num) == 7:
                count += 1

    print(count)


    number_list = [line.sort(key=len) for line in number_list]

