import unittest
import time
from enum import Enum

# Det her virker ikke
# Jeg har lavet alle de andre funktioner og de virker
# Men modulo matematikken virker ikke



class field(Enum):
    EMPTY = 0
    ROCK = 1
    SQUARE = 2
                            
def main(file: str) -> int:
    with open(file) as f:
        liste : list[str] = f.read().splitlines()


        rows = []
        columns = []

        for i in range(len(liste[0])):
            columns.append([])

        for y, line in enumerate(liste):
            temp = []
            for x, char in enumerate(line):
                if char == ".":
                    lol = field.EMPTY
                elif char == "O":
                    lol = field.ROCK
                elif char == "#":
                    lol = field.SQUARE
                columns[x].append(lol)
                temp.append(lol)
            rows.append(temp)
        
        all_lists = []
        all_loads = []
        done = False
        count = 0
        lol = 0

        while not done:
            one_dir(columns, rows, True)
            one_dir(rows, columns, True)
            one_dir(columns, rows, False)
            one_dir(rows, columns, False)
            count += 1
            temp = make_hex(rows)
            all_loads.append(calc_load(rows))
            for i in range(len(all_lists)):
                if all_lists[i] == temp:
                    done = True
                    lol = i+1
                    #count -= 1
                    break
            all_lists.append(temp)

        final_grid = all_loads[
            (1000000000 - lol) % (count + 1 - lol)+ lol]

        rest = 1000000000 - lol
        modulo = count-lol
        rest = rest % count-lol

        total = all_loads[rest+(lol-2)]
        return final_grid


# Forward is forward in the work list
# North column plus forward, West is row forward, South is column backwards, East is row backward
def one_dir(work_list, second_list, forward: bool):
    # Change k range to opposite and last solid rock

    # K range is forward or backwards on the column or row
    if forward:
        k_range = range(0, len(work_list[0]), 1)
    else:
        k_range = range(len(work_list[0])-1, -1, -1)
    # Last solid rock remeber
    cahched_rock = -1
    if not forward:
        cahched_rock = len(second_list) 
    
    for i in range(len(work_list)):
        #new_line = []
        last_solid_rock = cahched_rock
        num_rocks = 0
        for k in k_range:
            if forward:
                y_range = range(last_solid_rock+1, k, 1)
            else:
                y_range = range(last_solid_rock-1, k ,-1)
            
            if work_list[i][k] == field.SQUARE:
                for y in y_range:
                    if num_rocks > 0:
                        work_list[i][y] = field.ROCK
                        #new_line.append(field.ROCK)
                        second_list[y][i] = field.ROCK
                        num_rocks -= 1
                    else:
                        work_list[i][y] = field.EMPTY
                        #new_line.append(field.EMPTY)
                        second_list[y][i] = field.EMPTY
                last_solid_rock = k
                work_list[i][y_range.stop] = field.SQUARE
                #new_line.append(field.SQUARE)
                num_rocks = 0
            elif work_list[i][k] == field.ROCK:
                num_rocks += 1
                second_list[k][i] = field.EMPTY
                work_list[i][k] = field.EMPTY
            else:
                pass

        if forward:
            y_range = range(last_solid_rock+1, k+1, 1)
        else:
            y_range = range(last_solid_rock-1, k-1 ,-1)

        for y in y_range:
            if num_rocks > 0:
                #new_line.append(field.ROCK)
                work_list[i][y] = field.ROCK
                second_list[y][i] = field.ROCK
                num_rocks -= 1
            else:
                #new_line.append(field.EMPTY)
                work_list[i][y] = field.EMPTY
                second_list[y][i] = field.EMPTY
        #work_list[i] = new_line

def calc_load(rows):
    total_len = len(rows)
    load = 0
    for i in range(total_len):
        for k in range(total_len):
            if rows[i][k] == field.ROCK:
                load += total_len-i
    return load

def print_map(rows):
    for y in rows:
        temp = ""
        for x in y:
            if x == field.EMPTY:
                temp += "."
            elif x == field.ROCK:
                temp += "O"
            elif x == field.SQUARE:
                temp += "#"
        print(temp)
    print("-----------------------------")

def make_hex(rows):
    liste = []
    for y in rows:
        temp = ""
        for x in y:
            if x == field.EMPTY:
                temp += "0"
            elif x == field.ROCK:
                temp += "1"
            elif x == field.SQUARE:
                temp += "1"
        liste.append(hex(int(temp, 2)))
    return liste
    

if __name__ == "__main__":
    
    start = time.time()
    result = main("test14.txt")
    end = time.time()
    expected = 64
    assert result == expected, f"Expected {expected} but got {result}"
    print(end - start)

    start = time.time()
    result = main("input14.txt")
    end = time.time()
    expected = 106186
    assert result == expected, f"Expected {expected} but got {result}"
    print(result)
    print(end - start)
    