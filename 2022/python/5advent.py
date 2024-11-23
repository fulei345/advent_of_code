def main(filename):
    second_part = False
    lines = []
    stacks = []
    with open(filename) as f:
        for line in f:
            # First part
            if not second_part:
                if line != "\n":
                    lines.append(line[0:len(line)-1])
                else:
                    second_part = True
                    num_of_stacks = int(lines[-1][-2])
                    lines.pop()
                    for _ in range(num_of_stacks):
                        stacks.append([])
                    # For the number of cargo on the stack
                    for cargo_line in lines[::-1]:
                        for i in range(num_of_stacks):
                            if cargo_line[i*3+i+1] != " ":
                                stacks[i].append(cargo_line[i*3+i+1])
            else:
                # Second part lines
                all = line[0:len(line)-1]
                move_temp = all.split("from")
                move_var = int(move_temp[0].split("move")[1])
                from_temp = move_temp[1].split("to")
                from_var = int(from_temp[0])-1
                to_var = int(from_temp[1])-1

                part2_9001(stacks, move_var, from_var, to_var)
                # part1_9000(stacks, move_var, from_var, to_var)

    for stack in stacks:
        print(stack[-1],end = '')

def tail(xs, n):
    return xs[-n:]

                
def part1_9000(stacks, move_var, from_var, to_var):
    for _ in range(move_var):
        stacks[to_var].append(stacks[from_var].pop())

def part2_9001(stacks: list, move_var: int, from_var: int, to_var: int):
    stacks[to_var].extend(tail(stacks[from_var],move_var))
    stacks[from_var] = stacks[from_var][:-move_var]


if __name__ == "__main__":
    # main("input/test5.txt")
    main("input/input5.txt")
