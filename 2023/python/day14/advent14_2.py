import unittest
import time

# Lav et to 2d map hvor jeg bare finder det næste stop hvor den bliver stopped næste gang
# Dobbelt op med lister, (for rows og columns) Ville være lettere at iterere over 

class rock:
    def __init__(self, pos: tuple, cube: bool, is_row: bool):

        self.pos: tuple = pos
        self.cube: bool = cube
        self.is_row: bool = is_row # Is in the row list

    def __lt__(self, other):
        if self.is_row:
            return self.pos[1] < other.pos[1]
        else:
            return self.pos[0] < other.pos[0]

    def __eq__(self, other):
      if other is None:
          return False
      return self.pos[0] == other.pos[0] and self.pos[1] == other.pos[1]
                            

def main(file: str) -> int:
    with open(file) as f:
        liste : list[str] = f.read().splitlines()


        rows = []
        columns = []

        for i in range(len(liste[0])):
            columns.append([])

        # Remember the size of the OG
        y_len = len(liste)
        x_len = len(liste[0])

        for y, line in enumerate(liste):
            temp = []
            for x, char in enumerate(line):
                if char != ".":
                    if char == "O":
                        columns[x].append(rock((y,x), False, False))
                        temp.append(rock((y,x), False, True))
                    else:
                        columns[x].append(rock((y,x), True, False))
                        temp.append(rock((y,x), True, True))
            rows.append(temp)
        total = 0

        # Roll all north
        one_dir(columns, rows, True, True)
        one_dir(rows, columns, True, False)
        one_dir(columns, rows, False, True)
        one_dir(rows, columns, False, False)
        print(calc_load(rows))
        return total


# Forward is forward in the work list
# North column plus forward, West is row forward, South is column backwards, East is row backward
def one_dir(work_list, second_list, forward: bool, is_row: bool):
    # Change k range to opposite and last solid rock
    # Change y range
    for i in range(len(work_list)):
        new_column = []
        work_list[i].sort()
        last_solid_rock = -1
        if not forward:
            last_solid_rock = len(second_list)
        num_rocks = 0
        k_range = []
        if forward:
            k_range = range(0, len(work_list[i]), 1)
        else:
            k_range = range(len(work_list[i])-1, -1, -1)
        for k in k_range:
            y_range = []
            if forward:
                y_range = range(last_solid_rock+1, last_solid_rock+num_rocks+1, 1)
            else:
                y_range = range(last_solid_rock-1, (last_solid_rock+num_rocks)-1 ,-1)
            current: rock = work_list[i][k]
            if current.cube:
                if is_row:
                    update_rocks(y_range, new_column, second_list, i, True)
                    last_solid_rock = current.pos[0]
                else:
                    update_rocks(y_range, new_column, second_list, i, False)
                    last_solid_rock = current.pos[1]
                new_column.append(current)
                num_rocks = 0
            else:

                num_rocks += 1
                if is_row:
                    row_num = current.pos[0]
                    second_list[row_num].remove(rock((row_num,i), False, False))
                else:
                    row_num = current.pos[1]
                    second_list[row_num].remove(rock((i,row_num), False, False))
        y_range = []
        if forward:
            y_range = range(last_solid_rock+1, last_solid_rock+num_rocks+1, 1)
        else:
            y_range = range(last_solid_rock-1, (last_solid_rock+num_rocks)-1 ,-1)
        update_rocks(y_range, new_column, second_list, i, is_row)
        work_list[i] = new_column

def update_rocks(the_range, new_column, second_list, i, is_row: bool):
    if is_row:
        for y in the_range:
            new_column.append(rock((y,i), False, False))
            second_list[y].append(rock((y,i), False, True))
    else:# Update this code
        for y in the_range:
            new_column.append(rock((i,y), False, True))
            second_list[y].append(rock((i,y), False, False))

def calc_load(rows):
    total_len = len(rows)
    load = 0
    for y, row in enumerate(rows):
        for x, r in enumerate(row):
            if not r.cube:
                load += total_len-y
    return load

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
    #assert result == expected, f"Expected {expected} but got {result}"
    print(result)
    print(end - start)
    