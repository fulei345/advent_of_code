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
        all_totals = []
        count = 0
        for i in range(len(liste[0])):
            x_maps.append([])
        for y, line in enumerate(liste):
            temp = []
            if len(line) == 0:
                # Do the thing
                result = find_reflection(maps, x_maps) 
                total += result
                all_totals.append(total)
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
        result = find_reflection(maps, x_maps)
        total += result
        all_totals.append(total)
        return total


def find_reflection(maps, x_maps):
    total = 0
    found_real_refl = False
    for y, line in enumerate(maps):
        max_dir = min(y,len(maps)-y)
        num_diff = -1
        for i in range(1, max_dir+1):
            num_diff = compare_two(maps, (y+i)-1,y-i)
            if num_diff == 1:
                found_real_refl = True
            if num_diff == -1:
                break
        if num_diff > -1 and found_real_refl:
            total += (y)*100
            break
        found_real_refl = False
    #found_real_refl = False
    if found_real_refl:
        return total
    for x, line in enumerate(x_maps):
        max_dir = min(x,len(x_maps)-x)
        num_diff = -1
        for i in range(1,max_dir+1):
            num_diff = compare_two(x_maps, (x+i)-1,x-i)
            if num_diff == 1:
                found_real_refl = True
            if num_diff == -1:
                break
        if num_diff > -1 and found_real_refl:
            total += (x)
            break
        found_real_refl = False
        
    return total

def compare_two(maps, index_1, index_2):
    diffs = 0
    if index_1 < 0 or index_1 == len(maps) or index_2 < 0 or index_2 == len(maps):
        return -1
    for i in range(len(maps[index_1])):
        if maps[index_1][i] != maps[index_2][i]:
            diffs += 1
        if diffs > 1:
            return -1
    return diffs



if __name__ == "__main__":
    
    start = time.time()
    result = main("test13.txt")
    end = time.time()
    expected = 400
    assert result == expected, f"Expected {expected} but got {result}"
    print(end - start)

    start = time.time()
    result = main("input13.txt")
    end = time.time()
    #assert result == 6717, f"Expected 6717 but got {result}"
    print(result)
    print(end - start)
    