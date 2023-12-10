import unittest
import time

# Lister af differencer og find den næste med en lidt akavet metode men lad os da prøve

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

        #if cur[1]+1<len(maps[0]) and maps[cur[0]][cur[1]+1] in ["-", "J", "7"]:
        #    stack.append(maps[cur[0]][cur[1]+1])
        #    cur_symb = maps[cur[0]][cur[1]+1]
        #    cur = (cur[0], cur[1]+1)
        if cur[1]-1>-1 and maps[cur[0]+1][cur[1]] in ["|", "J", "L"]:
            stack.append(maps[cur[0]+1][cur[1]])
            cur_symb = maps[cur[0]+1][cur[1]]
            cur = (cur[0]+1, cur[1])
        elif cur[0]+1<len(maps) and maps[cur[0]][cur[1]-1] in ["-", "F", "L"]:
            stack.append(maps[cur[0]][cur[1]-1])
            cur_symb = maps[cur[0]][cur[1]-1]
            cur = (cur[0], cur[1]-1)
        found_again = False

        pipes = " "
        outer = "#"

        while not found_again:
            if cur_symb == "|":
                if prev[0]+1 == cur[0]:
                    prev = cur
                    cur = (cur  [0]+1,cur[1])
                else:
                    prev = cur
                    cur = (cur[0]-1,cur[1])
            elif cur_symb == "-":
                if prev[1]-1 == cur[1]:
                    prev = cur
                    cur = (cur[0],cur[1]-1)
                else:
                    prev = cur
                    cur = (cur[0],cur[1]+1)
            elif cur_symb == "L":
                if prev[0]+1 == cur[0]:
                    prev = cur
                    cur = (cur[0],cur[1]+1)
                else:
                    prev = cur
                    cur = (cur[0]-1,cur[1])
            elif cur_symb == "J":
                if prev[0]+1 == cur[0]:
                    prev = cur
                    cur = (cur[0],cur[1]-1)
                else:
                    prev = cur
                    cur = (cur[0]-1,cur[1])
            elif cur_symb == "7":
                if prev[1]+1 == cur[1]:
                    prev = cur
                    cur = (cur[0]+1,cur[1])
                else:
                    prev = cur
                    cur = (cur[0],cur[1]-1)
            elif cur_symb == "F":
                if prev[0]-1 == cur[0]:
                    prev = cur
                    cur = (cur[0],cur[1]+1)
                else:
                    prev = cur
                    cur = (cur[0]+1,cur[1])
            cur_symb = maps[cur[0]][cur[1]]
            maps[prev[0]][prev[1]] = pipes

            stack.append(cur_symb)
            if cur_symb == "S":
                maps[cur[0]][cur[1]] = pipes
                found_again = True


        # If odd amounts of consequencyly wall then in else outside
        # Count len(stack)//2

        count = len(stack)//2
        for y, line in enumerate(maps):
            for x, c in enumerate(line):
                if c != pipes:
                    maps[y][x] = outer
                    count += 1
                else:
                    break
        
        for x in range(len(maps[0])):
            for y in range(len(maps)):
                if maps[y][x] != pipes:
                    maps[y][x] = outer
                    count += 1
                else:
                    break
        
        for y in range(len(maps)):
            for x in range(len(maps[0])-1, -1, -1):
                if maps[y][x] != pipes:
                    maps[y][x] = outer
                    count += 1
                else:
                    break
        
        for x in range(len(maps[0])-1,-1,-1):
            for y in range(len(maps)-1,-1,-1):
                if maps[y][x] != pipes:
                    maps[y][x] = outer
                    count += 1
                else:
                    break
        
        count_before = count

        diff = False
        while not diff:
            for y, line in enumerate(maps):
                for x, c in enumerate(line):
                    if c != pipes and c != outer:
                        symb_set = [maps[y-1][x],maps[y][x+1],maps[y+1][x],maps[y][x-1]]
                        if outer in symb_set:
                            maps[y][x] = outer
                            count += 1
            if count_before == count:
                diff = True
            count_before = count
    
        for y in maps:
            print("".join(y))
        return (len(maps) * len(maps[0])) -count

if __name__ == "__main__":
    
    start = time.time()
    #result = main("test10.txt")
    end = time.time()
    #assert result == 8, f"Expected 8 but got {result}"
    print(end - start)

    start = time.time()
    result = main("input10.txt")
    end = time.time()
    #assert result == 6717, f"Expected 6717 but got {result}"
    print(result)
    print(end - start)
    