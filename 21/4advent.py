filename = "input/input4.txt"


def run_whole_board(board_list, bingo_board_list, role_call_list):
    finish_list = [0] * len(board_list)
    sum_list = []
    for num in role_call_list:
        for i in range(len(board_list)):
                    # loop for each row
                    for x in range(len(board_list[i])):
                        # loop for each column
                        for y in range(len(board_list[i][x])):

                        # For each num on board
                            if num == board_list[i][x][y]:
                                board_list[i][x][y] = 'X'

                                # update bingo board
                                bingo_board_list[i]["row"][x] += 1
                                bingo_board_list[i]["col"][y] += 1

                                # check bing board
                                if 5 in bingo_board_list[i]["row"] or 5 in  bingo_board_list[i]["col"]:
                                    if finish_list[i] < 1:
                                        finish_list[i] += 1

                                        summation = 0
                                        for row in board_list[i]:
                                            for col in row:
                                                if isinstance(col, int):
                                                    summation += col

                                        sum_list.append(tuple((i, summation * num)))

                                        if sum(finish_list) == len(board_list):
                                            return sum_list

    return -1

with open(filename) as f:
    liste = f.read().splitlines()

    role_call_list = liste[0].split(',')
    role_call_list = list(map(int, role_call_list))

    # Each board has a 2D board array, and a bingo board keeping track of winning.
    board_list = []
    bingo_board_list = []

    # For each bingo board
    for i in range(0, int(len(liste)/6)):
        # make board list
        board_list.append([])
        #print(len(board_list))
        for k in range(2, 7):
            index = i * 6 + k
            row = liste[index].split()
            row = list(map(int, row))
            board_list[i].append(row)
        # Make bingo dict
        bingo_board_list.append({
            "row": [0,0,0,0,0],
            "col": [0,0,0,0,0]
        })


    result_list = run_whole_board(board_list, bingo_board_list, role_call_list)

    print("First board finish:", result_list[0][0], " score:", result_list[0][1])
    print("Last board finish:", result_list[-1][0], " score:", result_list[-1][1])