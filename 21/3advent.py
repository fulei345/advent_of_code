filename = "input/input3.txt"

def most_common(index_liste, index, liste):
    count = [0, 0]

    and_num = index_liste[index]

    for num in liste:
        if bin(and_num&num) == bin(and_num):
            count[1] += 1
        else:
            count[0] += 1

    if count[0] < count[1]:
        return 1
    elif count[1] == count[0]:
        return 2
    else:
        return 0

with open(filename) as f:
    liste = f.read().splitlines()

    index = []

    for i, _ in enumerate(liste[0]):
        index.append(2 ** i)

    liste = [int(diagnostic, 2) for diagnostic in liste]

    # First answer
    gamma = 0
    epsilon = 0
    for i, binary in enumerate(index):
        temp = most_common(index, i, liste)
        if temp == 1:
            gamma += index[i]
        else:
            epsilon += index[i]

    print(gamma * epsilon)

    # Second answer

    oxygen_list = []
    co2_list = []
    i = len(index) - 1

    mc = most_common(index, i, liste)
    oxygen_list = [num for num in liste if (bin(num&index[i]) == bin(index[i]) and (mc == 1 or mc == 2)) or (not bin(num&index[i]) == bin(index[i]) and (mc == 0))]
    co2_list = [num for num in liste if (not bin(num&index[i]) == bin(index[i]) and (mc == 1 or mc == 2)) or (bin(num&index[i]) == bin(index[i]) and (mc == 0))]

    i -= 1

    while(len(oxygen_list)) > 1 and i >= 0:
        mc = most_common(index, i, oxygen_list)
        oxygen_list = [num for num in oxygen_list if (bin(num&index[i]) == bin(index[i]) and (mc == 1 or mc == 2)) or (not bin(num&index[i]) == bin(index[i]) and (mc == 0))]

        i -= 1

    i = len(index) - 2

    while(len(co2_list)) > 1 and i >= 0:
        mc = most_common(index, i, co2_list)
        co2_list = [num for num in co2_list if (not bin(num&index[i]) == bin(index[i]) and (mc == 1 or mc == 2)) or (bin(num&index[i]) == bin(index[i]) and (mc == 0))]

        i -= 1

    print(oxygen_list[0] * co2_list[0])