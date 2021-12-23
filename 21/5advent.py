filename = "input/input5.txt"

def count_overlapping(input, should_diagonal):
     # Iniatilses the array
    rows, cols = (1000, 1000)
    arr = [[0 for i in range(cols)] for j in range(rows)]

    for line in input:

        x1 = line[0][0]
        x2 = line[1][0]
        y1 = line[0][1]
        y2 = line[1][1]

        # If the x is equal
        if x1 == x2:
            if y1 > y2:
                for i in range(y2, y1 + 1):
                    arr[x1][i] += 1
            else:
                for i in range(y1, y2 + 1):
                    arr[x1][i] += 1
        elif y1 == y2:
            if x1 > x2:
                for i in range(x2, x1 + 1):
                    arr[i][y1] += 1
            else:
                for i in range(x1, x2 + 1):
                    arr[i][y1] += 1
        elif y1 != y2 and x1 != x2 and should_diagonal:
            # If it is rising
            if x1 < x2 and y1 < y2:
                for i in range(x2-x1 + 1):
                    arr[x1 + i][y1 + i] += 1
            # If it is rising but opposite direction
            elif x1 > x2 and y1 > y2:
                for i in range(x1-x2 + 1):
                    arr[x2 + i][y2 + i] += 1
            # Rising backwards
            elif x1 > x2 and y1 < y2:
                for i in range(x1-x2 + 1):
                    arr[x1 - i][y1 + i] += 1
            # forward falling
            elif x1 < x2 and y1 > y2:
                for i in range(x2-x1 + 1):
                    arr[x1 + i][y1 - i] += 1


    count = 0

    for i in range(len(arr)):
        for k in range(len(arr[i])):
            if arr[i][k] > 1:
                count += 1

    return count

with open(filename) as f:
    liste = f.read().splitlines()

    liste = [line.split('->') for line in liste]

    # makes a line into a list with two tuples, one for each point
    liste = [list(
        (tuple((int(line[0].split(',')[0]),int(line[0].split(',')[1]))),
        tuple((int(line[1].split(',')[0]),int(line[1].split(',')[1]))))
        ) for line in liste]

    straight = [line for line in liste if line[0][0] == line[1][0] or line[0][1] == line[1][1]]

    result = count_overlapping(straight, False)
    print(result)

    result= count_overlapping(liste, True)
    print(result)