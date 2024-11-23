FILENAME = "input/input13.txt"
FILENAME = "input/test13.txt"

def main():
    point_list, fold_list = load_data(FILENAME)

    maximum = 0
    for fold in fold_list:
        point_list, maximum = fold_one(point_list,fold)

    for i in range(maximum):
        line = ""
        for k in range(maximum):
            if (k, i) in point_list:
                line += '#'
            else:
                line += '.'
        print(line)
    print(len(point_list))

def fold_one(points: list, fold: tuple):
    temp_points = []
    line = fold[1]
    maximum = 0
    if fold[0] == 'y':
        points.sort(key=lambda dot: dot[1])
        for point in points:
            if point[1] > line:
                diff = point[1] - line
                temp_tuple = (point[0], line - diff)
                if temp_tuple not in temp_points:
                    temp_points.append(temp_tuple)
            else:
                temp_points.append(point)
            maximum = max(maximum, point[0])
    elif fold[0] == 'x':
        points.sort(key=lambda dot: dot[0])
        for point in points:
            if point[0] > line:
                diff = point[0] - line
                temp_tuple = (line - diff, point[1])
                if temp_tuple not in temp_points:
                    maximum = max(maximum, point[1])
                    temp_points.append(temp_tuple)
            else:
                maximum = max(maximum, point[1])
                temp_points.append(point)
    maximum = max(maximum, line)
    return temp_points, maximum


# Makes two list of tuples
def load_data(path):
    with open(path) as f:
        point_list = []
        fold_list = []
        liste = f.read().splitlines()
        for line in liste:
            temp_line = line.split(',')
            if len(temp_line) > 1:
                temp_tuple = (int(temp_line[0]),int(temp_line[1]))
                point_list.append(temp_tuple)
            else:
                temp_line = temp_line[0].split(' ')
                if len(temp_line) > 1:
                    temp_line = temp_line[2].split('=')
                    temp_tuple = (temp_line[0],int(temp_line[1]))
                    fold_list.append(temp_tuple)
    return point_list, fold_list

if __name__ == '__main__':
    main()