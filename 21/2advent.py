filename = "input/input2.txt"

with open(filename) as f:
    liste = f.read().splitlines()
    liste = [tuple((tub.split()[0], int(tub.split()[1]))) for tub in liste]

    # 1
    vertical = 0
    horizontal = 0
    for dir, num in liste:
        if dir == "forward":
            horizontal = horizontal + num
        elif dir == "down":
            vertical = vertical + num
        else:
            vertical = vertical - num

    print(vertical * horizontal)

    # 2
    aim = 0
    horizontal = 0
    vertical = 0
    for dir, num in liste:
        if dir == "forward":
            horizontal = horizontal + num
            vertical = vertical + aim * num
        elif dir == "down":
            aim = aim + num
        else:
            aim = aim - num

    print(vertical * horizontal)