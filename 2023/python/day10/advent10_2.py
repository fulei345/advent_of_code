import unittest
import time

# Lister af differencer og find den næste med en lidt akavet metode men lad os da prøve

# Dict is for check and then diff in y and x from prev
# Bottom: |, 7, F
# Up: L, J
# Left: -
symb_dict = {"|": ((-1,0),(-2,0)),
             "7": ((-1,0),(-1,-1)),
             "F": ((-1,0),(-1,1)),
             "L": ((1,0),(1,1)),
             "J": ((1,0),(1,-1)),
             "-": ((0,1),(0,2))}
symbs = ["|", "7", "F", "L", "J", "-"]

def main(file: str) -> int:
    with open(file) as f:
        liste : list[str] = f.read().splitlines()


        maps = []
        for y, line in enumerate(liste):
            animal = line.find("S")
            if animal > -1:
                animal_location = (y, animal)
            maps.append([*line])

        # Check up, right, down and left
        stack = []

        cur = (animal_location[0], animal_location[1])
        cur_symb = maps[cur[0]][cur[1]]
        prev = (animal_location[0], animal_location[1])

        if cur[1]-1>-1 and maps[cur[0]+1][cur[1]] in ["|", "J", "L"]:
            cur = (cur[0]+1, cur[1])
        elif cur[0]+1<len(maps) and maps[cur[0]][cur[1]-1] in ["-", "F", "L"]:
            cur = (cur[0], cur[1]-1)
        
        stack.append(cur)
        cur_symb = maps[cur[0]][cur[1]]
        found_again = False

        outer = "#"

        while not found_again:
            if cur_symb in symbs:
                check, func = symb_dict[cur_symb]
                temp = cur
                if prev[0] + check[0] == cur[0] and prev[1] + check[1] == cur[1]:
                    cur = (prev[0]+func[0],prev[1]+func[1])
                    prev = temp
                else:
                    cur = (prev[0]-func[0],prev[1]-func[1])

                prev = temp

                cur_symb = maps[cur[0]][cur[1]]

                stack.append(cur)
                if cur_symb == "S":
                    found_again = True
                    start = stack[0]
                    prev = stack[-2]
                    is_set = False
                    for symb, tup in symb_dict.items():
                        _, func = tup
                        if prev[0] == start[0]+func[0] and prev[1] == start[1]+ func[1]:
                            maps[cur[0]][cur[1]] = symb
                            is_set = True
                            break
                    if not is_set:
                        for symb, tup in symb_dict.items():
                            _, func = tup
                            if prev[0] == start[0]- func[0] and prev[1] == start[1]-func[1]:
                                maps[cur[0]][cur[1]] = symb
                                break


        # Count len(stack)//2

        count = len(stack)//2

        ins_numb = 0
        for y, line in enumerate(maps):
            ins, outs = check_line(maps, line, stack, y)
            ins_numb += ins 
        
        #for y in maps:
        #    print("".join(y))
        return ins_numb

# Maybe more inputs ??
def check_line(maps, line, stack, line_index):
    ins = 0
    outs = 0
    count = 0
    is_line = False
    dir_came_from = -1 # 1 From down, 0 From up
    for x in range(len(line)):
        char = line[x]
        if (line_index,x) in stack:
            if char in ["F", "L"]:
                is_line = True
                if char == "F":
                    dir_came_from = 1
                else:
                    dir_came_from = 0
            elif char in ["7", "J"]:
                if is_line:
                    if (dir_came_from == 1 and char == "J") or (dir_came_from == 0 and char == "7"):
                        count += 1
                    is_line = False
            elif char == "-":
                continue
            else:
                count += 1
        else:
            if char != "O" and char != "I":
                if count % 2 == 0:
                    outs += fill(maps, (line_index,x), stack, "O")
                else:
                    ins += fill(maps, (line_index,x), stack, "I")
    return ins, outs
    
def fill(maps, point,pibe, c):
    count = 0
    stack = [point]
    while len(stack) > 0:
        lastest = stack.pop()
        maps[lastest[0]][lastest[1]] = c
        count += 1
        y, x = lastest
        symb_set = [(y-1,x),(y,x+1),(y+1,x),(y,x-1)]
        for symb in symb_set:
            if symb[0] < 0 or symb[0] > len(maps)-1 or symb[1] < 0 or symb[1] > len(maps[0])-1:
                continue
            if symb not in pibe and maps[symb[0]][symb[1]] not in ["O","I"] and symb not in stack:
                stack.append(symb)
    return count

    


if __name__ == "__main__":
    
    start = time.time()
    result = main("test10_1.txt")
    end = time.time()
    assert result == 4, f"Expected 4 but got {result}"
    print(end - start)

    start = time.time()
    #result = main("test10_2.txt")
    end = time.time()
    #assert result == 4, f"Expected 4 but got {result}"
    print(end - start)

    start = time.time()
    result = main("input10.txt")
    end = time.time()
    assert result == 381, f"Expected 381 but got {result}"
    print(result)
    print(end - start)
    