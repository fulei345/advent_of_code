def main(filename):
    maze = []
    with open(filename) as f:
        for line in f:
            l = line[0:len(line)-1]
            temp_line = []
            for i, square in enumerate(l):
                if square == "S":
                    start_point = (len(maze)-1,i)
                    temp_line.append(-1)
                elif square == "E":
                    end_point = (len(maze)-1,i)
                    temp_line.append(27)
                else:
                    temp_line.append(ord(square)-97)
            maze.append(temp_line)

    # Keep a list of visited
    # Do not visit again
    # Distance in x-x and y-y lowest take that
    # And then just iterate until we are there

    current_elevation = -1
    visited = [start_point]
    while current_elevation != 27:
        # Check north east and west
        # Choose one with lowest distance first
        # And just run the other
        
        pass


    for line in maze:
        print(line)



def distance(current, end):
    x_1, y_1 = current
    x_2, y_2 = end
    return abs(x_1 - x_2) +  abs(y_1 - y_2)
        

if __name__ == "__main__":
    main("input/test12.txt")
    # main("input/input12.txt")
