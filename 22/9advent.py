def check_neighbor(head: list, tail: list):
    x_tail = tail[0]
    y_tail = tail[1]
    x_head = head[0]
    y_head = head[1]
    return  x_head-1 <= x_tail <= x_head+1 and y_head-1 <= y_tail <= y_head+1

def move_next(first: list, last: list):
    if not check_neighbor(first, last):
        x_head, y_head = first[0],first[1]
        x_tail, y_tail = last[0],last[1]

        if x_tail == x_head:
            if y_tail > y_head:
                last[1] -= 1
            else:
                last[1] += 1
        elif y_tail == y_head:
            if x_tail > x_head:
                last[0] -= 1
            else:
                last[0] += 1
        elif x_tail <= x_head and y_tail <= y_head:
            last[0] += 1
            last[1] += 1
        elif x_tail <= x_head and y_tail >= y_head:
            last[0] += 1
            last[1] -= 1
        elif x_tail >= x_head and y_tail >= y_head:
            last[0] -= 1
            last[1] -= 1
        elif x_tail >= x_head and y_tail <= y_head:
            last[0] -= 1
            last[1] += 1

def main(filename, length):
    visited = set()
    visited.add((0,0))
    rope = []
    for _ in range(length):
        temp = [0,0]
        rope.append(temp)
    with open(filename) as f:
        for line in f:
            command = line[0:len(line)-1]
            command = command.split(" ")
            direction = command[0]
            length = int(command[1])
            for i in range(length):
                if direction == "R":
                    rope[0][0] += 1
                elif direction == "D":
                    rope[0][1] -= 1
                elif direction == "L":
                    rope[0][0] -= 1
                elif direction == "U":
                    rope[0][1] += 1

                for i in range(len(rope)-1):
                    move_next(rope[i], rope[i+1])
                
                visited.add((rope[-1][0],rope[-1][1]))

    print(len(visited))

if __name__ == "__main__":
    main("input/test9.txt", 2)
    main("input/input9.txt", 2)
    main("input/test9_2.txt", 10)
    main("input/input9.txt", 10)
