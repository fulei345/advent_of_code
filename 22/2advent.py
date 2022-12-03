# filename = "input/test2.txt"
filename = "input/input2.txt"

total_sum_1 = 0
total_sum_2 = 0
# Score list
score = {"X":1, "Y":2, "Z":3}
win_1 = {"A X":3, "A Y": 6, "A Z": 0, "B X": 0, "B Y": 3, "B Z": 6, "C X": 6, "C Y": 0, "C Z": 3}

win_2 = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5,  "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}
with open(filename) as f:
    for line in f:
        me = line[2]
        lineline = line[0:3]
        total_sum_1 += score[me]
        total_sum_1 += win_1[lineline]
        total_sum_2 += win_2[lineline]

    print(total_sum_1)
    print(total_sum_2)
