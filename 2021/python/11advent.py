import re
filename = "input/input11.txt"
filename = "input/test11.txt"

dir = {
    "e":  [ 1, 0],
    "n":  [ 0, 1],
    "w":  [-1, 0],
    "s":  [ 0,-1],
    "sw": [-1,-1],
    "se": [ 1,-1],
    "nw": [-1, 1],
    "ne": [ 1, 1],
    }

def one_iteration(array):
    rows, cols = (len(array), len(array[0]))
    flash = [[0 for i in range(cols)] for j in range(rows)]
    total_count = 0
    for i, line in enumerate(array):
        for k, num in enumerate(line):
            array, flash, count = add_and_spread(array, flash, i, k)
            total_count += count

    count = 0
    for i, line in enumerate(array):
        for k, num in enumerate(line):
            if num > 9:
                count += 1
                array[i][k] = 0

    if count == rows * cols:
        return array, total_count, True
    return array, total_count, False

def add_and_spread(array, flash, x, y):
    array[x][y] += 1
    if array[x][y] > 9 and flash[x][y] == 0:
        total_count = 1
        flash[x][y] = 1
        for direction in dir.keys():
            temp = dir[direction]
            if -1 < x + temp[0] < len(array) and -1 < y + temp[1] < len(array[0]):
                if flash[x + temp[0]][y + temp[1]] == 0:
                    array, flash, count = add_and_spread(array, flash, x + temp[0], y + temp[1])
                    total_count += count
        return array, flash, total_count

    return array, flash, 0


with open(filename) as f:
    liste = f.read().splitlines()

    array = []

    for line in liste:

        res = re.findall('\d', line)
        res = list(map(int, res))
        array.append(res)

    total_count = 0
    while True:
        array, count, bally = one_iteration(array)
        total_count += 1
        if bally:
            break

    print(total_count)
