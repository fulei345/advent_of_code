def check_neighbor(head: list, tail: list):
    x_tail = tail[0]
    y_tail = tail[1]
    x_head = head[0]
    y_head = head[1]
    return  x_head-1 <= x_tail <= x_head+1 and y_head-1 <= y_tail <= y_head+1

def main(filename):
    head_point = [0,0]
    tail_point = [0,0]
    visited = set()
    visited.add((0,0))
    with open(filename) as f:
        for line in f:
            command = line[0:len(line)-1]
            command = command.split(" ")
            direction = command[0]
            length = int(command[1])

            for i in range(length):
                if direction == "R":
                    head_point[0] += 1
                elif direction == "D":
                    head_point[1] -= 1
                elif direction == "L":
                    head_point[0] -= 1
                elif direction == "U":
                    head_point[1] += 1

                if not check_neighbor(head_point, tail_point):
                        x_tail = tail_point[0]
                        y_tail = tail_point[1]
                        x_head = head_point[0]
                        y_head = head_point[1]

                        if x_tail == x_head:
                            if y_tail > y_head:
                                tail_point[1] -= 1
                            else:
                                tail_point[1] += 1
                        elif y_tail == y_head:
                            if x_tail > x_head:
                                tail_point[0] -= 1
                            else:
                                tail_point[0] += 1
                        elif x_tail <= x_head and y_tail <= y_head:
                            tail_point[0] += 1
                            tail_point[1] += 1
                        elif x_tail <= x_head and y_tail >= y_head:
                            tail_point[0] += 1
                            tail_point[1] -= 1
                        elif x_tail >= x_head and y_tail >= y_head:
                            tail_point[0] -= 1
                            tail_point[1] -= 1
                        elif x_tail >= x_head and y_tail <= y_head:
                            tail_point[0] -= 1
                            tail_point[1] += 1
                        visited.add((tail_point[0],tail_point[1]))

    print(visited)
    print(len(visited))



    #print(tree_score((3,2), forrest))
if __name__ == "__main__":
    main("input/test9.txt")
    main("input/input9.txt")
