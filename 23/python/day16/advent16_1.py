import time
import sys
sys.setrecursionlimit(10000000) 
# A 2D map with a lot of mirrors


def main(file: str) -> int:
    maps = []
    energy_map = []
    with open(file) as f:
        liste : list[str] = f.read().splitlines()
        for i in range(len(liste)):
            liste[i] = [*liste[i]]
            temp = []
            for i in range(len(liste[i])):
                temp.append(False)
            energy_map.append(temp)

        maps = liste
    iterative(maps, energy_map)
    print_energy(energy_map)
    total = count_energy(energy_map)
    return total

# Left 0, Down 1, Right 2, Up 3
def iterative(maps, energy_map):
    stack = [(2, (0,-1))]
    seen = []
    while len(stack) != 0:
        cur_pair = stack.pop()
        current = cur_pair[1]
        direction = cur_pair[0]
        cur_y = current[0]
        cur_x = current[1]
        #if cur_x < 0 or cur_y < 0 or cur_x == len(maps[0]) or cur_y == len(maps):
        #    continue
        if cur_x < 0 or cur_y < 0 or cur_x == len(maps[0]) or cur_y == len(maps):
           pass
        else:
            energy_map[cur_y][cur_x] = True
        if direction == 0:
            if cur_x -1 == -1:
                continue
            next_pos = (cur_y, cur_x-1)
            next_symb = maps[cur_y][cur_x-1]
            if next_symb == "/":
                next_dir = 1
            elif next_symb == "\\":
                next_dir = 3
            elif next_symb == "|":
                next_dir = 3
                if (1,next_pos) not in seen:
                    stack.append((1,next_pos))
                    seen.append((1,next_pos))
            elif next_symb == "-":
                next_dir = 0
            elif next_symb == ".":
                next_dir = 0
            if (next_dir,next_pos) not in seen:
                stack.append((next_dir,next_pos))
                seen.append((next_dir,next_pos))
        elif direction == 1:
            if cur_y + 1 == len(maps):
                continue
            next_pos = (cur_y+1, cur_x)
            next_symb = maps[cur_y+1][cur_x]
            if next_symb == "/":
                next_dir = 0
            elif next_symb == "\\":
                next_dir = 2
            elif next_symb == "|":
                next_dir = 1
            elif next_symb == "-":
                next_dir = 0
                if (2,next_pos) not in seen:
                    stack.append((2,next_pos))
                    seen.append((2,next_pos))
            elif next_symb == ".":
                next_dir = 1
            if (next_dir,next_pos) not in seen:
                stack.append((next_dir,next_pos))
                seen.append((next_dir,next_pos))
        elif direction == 2:
            if cur_x +1 == len(maps[0]):
                continue
            next_pos = (cur_y, cur_x+1)
            next_symb = maps[cur_y][cur_x+1]
            if next_symb == "/":
                next_dir = 3
            elif next_symb == "\\":
                next_dir = 1
            elif next_symb == "|":
                next_dir = 3
                if (1,next_pos) not in seen:
                    stack.append((1,next_pos))
                    seen.append((1,next_pos))
            elif next_symb == "-":
                next_dir = 2
            elif next_symb == ".":
                next_dir = 2
            if (next_dir,next_pos) not in seen:
                stack.append((next_dir,next_pos))
                seen.append((next_dir,next_pos))
        elif direction == 3:
            if cur_y -1 == -1:
                continue
            next_pos = (cur_y-1, cur_x)
            next_symb = maps[cur_y-1][cur_x]
            if next_symb == "/":
                next_dir = 2
            elif next_symb == "\\":
                next_dir = 0
            elif next_symb == "|":
                next_dir = 3
            elif next_symb == "-":
                next_dir = 2
                if (0,next_pos) not in seen:
                    stack.append((0,next_pos))
                    seen.append((0,next_pos))
            elif next_symb == ".":
                next_dir = 3
            if (next_dir,next_pos) not in seen:
                stack.append((next_dir,next_pos))
                seen.append((next_dir,next_pos))

def print_energy(energy):
    for y in energy:
        temp = ""
        for x in y:
            if x:
                temp += "#"
            else:
                temp += "."
        print(temp)

def count_energy(energy_map):
    count = 0
    for y in energy_map:
        for x in y:
            if x:
                count += 1
    return count


if __name__ == "__main__":
    
    start = time.time()
    result = main("test16.txt")
    end = time.time()
    expected = 46
    assert result == expected, f"Expected {expected} but got {result}"
    print(end - start)

    start = time.time()
    result = main("input16.txt")
    end = time.time()
    expected = 7798
    assert result == expected, f"Expected {expected} but got {result}"
    print(end - start)
    