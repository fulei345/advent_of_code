import re
filename = "input/input9.txt"
#filename = "test9.txt"

mapps = []

def check_basin(arret, mapped, i, k):

    num = mapped[i][k]
    total_higher = 1
    lowest_number = num

    if arret[i][k] == 0 and num != 9:
        arret[i][k] = 1
        your_lowest = True
        coordinate_list = []
        if k > 0 and mapped[i][k-1] != 9:
            coordinate_list.append((i,k-1))
        if k < len(mapped[0]) - 1 and mapped[i][k+1] != 9:
            coordinate_list.append((i,k+1))
        if i > 0 and mapped[i-1][k] != 9:
            coordinate_list.append((i-1,k))
        if i < len(mapped) - 1 and mapped[i+1][k] != 9:
            coordinate_list.append((i+1,k))

        for x, y in coordinate_list:
            if arret[x][y] == 0:
                arret, higher, number = check_basin(arret, mapped, x, y)
                total_higher += higher
                lowest_number = min(number, lowest_number)

        return arret, total_higher, lowest_number
    else:
        if mapped[i][k] == 9:
            arret[i][k] = 2
        else:
            arret[i][k] = 1
        return arret, 0, num


with open(filename) as f:
    liste = f.read().splitlines()

    for line in liste:

        res = re.findall('\d', line)
        res = list(map(int, res))
        mapps.append(res)

    low_points = []
    basins_size = []

    rows, cols = (len(mapps), len(mapps[0]))
    arr = [[0 for i in range(cols)] for j in range(rows)]

    for i, line in enumerate(mapps):
        for k, num in enumerate(line):
            if arr[i][k] == 0:
                arr, high, lowest =check_basin(arr, mapps, i, k)
                if high > 0:
                    low_points.append(lowest)
                    basins_size.append(high)

    multi = 1
    basins_size.sort(reverse=True)
    for index in range(3):
        multi *= basins_size[index]
    result1 = len(low_points) + sum(low_points)
    print(result1)
    print(multi)

