import unittest
import time

# Lav rekursiv funktion der prøver alt

# index_n direkte før mængder af # (på den jeg er lige nu)
# check_preceding checker om der kan placeres en # der
# 

def main(file: str) -> int:
    with open(file) as f:
        liste : list[str] = f.read().splitlines()

        total = 0
        maps = []
        x_maps = []
        for i in range(len(liste[0])):
            x_maps.append([])
        for y, line in enumerate(liste):
            temp = []
            if len(line) == 0:
                # Do the thing
                total += find_reflection(maps, x_maps)
                x_maps = []
                maps = []
                if y + 1 != len(liste):
                    for i in range(len(liste[y+1])):
                        x_maps.append([])
            else:
                for x, char in enumerate(line):
                    temp.append(char)
                    x_maps[x].append(char)
                maps.append(temp)
        total += find_reflection(maps, x_maps)
        return total


def find_reflection(maps, x_maps):
    total = 0
    for y, line in enumerate(maps):
        max_dir = min(y,len(maps)-y)
        is_equal = False
        for i in range(1, max_dir+1):
            is_equal = compare_two(maps, (y+i)-1,y-i)
            if not is_equal:
                break
        if is_equal:
            total += (y)*100
            break

    for x, line in enumerate(x_maps):
        max_dir = min(x,len(x_maps)-x)
        is_equal = False
        for i in range(1,max_dir+1):
            is_equal = compare_two(x_maps, (x+i)-1,x-i)
            if not is_equal:
                break
        if is_equal:
            total += (x)
            break
        
    return total

def compare_two(maps, index_1, index_2):
    if index_1 < 0 or index_1 == len(maps) or index_2 < 0 or index_2 == len(maps):
        return False
    for i in range(len(maps[index_1])):
        if maps[index_1][i] != maps[index_2][i]:
            return False
    return True



if __name__ == "__main__":
    
    start = time.time()
    result = main("test13.txt")
    end = time.time()
    expected = 405
    assert result == expected, f"Expected {expected} but got {result}"
    print(end - start)

    start = time.time()
    result = main("input13.txt")
    end = time.time()
    #assert result == 6717, f"Expected 6717 but got {result}"
    print(result)
    print(end - start)
    