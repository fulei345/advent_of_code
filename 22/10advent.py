def check_cycle(cycle):
    if cycle > 21:
        return (cycle+20) % 40 == 0
    else:
        return cycle == 20

def main(filename):
    x_value = 1
    result = []
    cycle = 0
    with open(filename) as f:
        for line in f:
            command = line[0:len(line)-1]
            command = command.split(" ")
            instruction = command[0]
            
            
            if instruction == "noop":
                cycle += 1
                if check_cycle(cycle):
                    result.append(x_value * cycle)
            elif instruction == "addx":
                int_value = int(command[1])
                for i in range(2):
                    cycle += 1
                    if check_cycle(cycle):
                        result.append(x_value * cycle)
                x_value += int_value

    print(sum(result))

def check_sprite(cycle, x_value):
    return x_value-1 <=  (cycle % 40) -1  <= x_value+1

def make_cycle(cycle, x_value, result, index):
    index_r = index
    if check_sprite(cycle,x_value):
        result[index].append("#")
    else:
        result[index].append(".")
    if len(result[index]) % 40 == 0:
        result.append([])
        index_r += 1
    return index_r

def main2(filename):
    x_value = 1
    result = []
    cycle = 0
    with open(filename) as f:
        index = 0
        result.append([])
        for line in f:
            command = line[0:len(line)-1]
            command = command.split(" ")
            instruction = command[0]
            
            
            if instruction == "noop":
                cycle += 1
                index = make_cycle(cycle, x_value, result, index)
            elif instruction == "addx":
                int_value = int(command[1])
                for i in range(2):
                    cycle += 1
                    index = make_cycle(cycle, x_value, result, index)
                x_value += int_value

    for line in result:
        for s in line:
            print(s,end="")
        print("")




if __name__ == "__main__":
    main("input/input10.txt")
    main("input/input10.txt")
    main2("input/test10.txt")
    main2("input/input10.txt")
