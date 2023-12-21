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


        # Change k range to opposite and last solid rock
        # Change y range

        # Could make a function which returns which should be deleted and added of the other,

        # Find the cycle

        for i in range(len(columns)):
            new_column = []
            columns[i].sort()
            last_solid_rock = -1
            num_rocks = 0
            for k in range(0, len(columns[i]), 1):
                current: rock = columns[i][k]
                if current.cube:
                    for y in range(last_solid_rock+1, last_solid_rock+num_rocks+1, 1):
                        new_column.append(rock((y,i), False, False))
                        total += len(rows)-y
                        rows[i].append(rock((y,i), False, True))

                    last_solid_rock = current.pos[0]
                    new_column.append(current)
                    num_rocks = 0
                else:
                    num_rocks += 1
                    row_num = current.pos[0]
                    rows[row_num].remove(rock((row_num,i), False, False))
            for y in range(last_solid_rock+1, last_solid_rock+num_rocks+1, 1):
                        new_column.append(rock((y,i), False, False))
                        total += len(rows)-y
                        rows[i].append(rock((y,i), False, True))
            columns[i] = new_column
        return total



if __name__ == "__main__":
    
    start = time.time()
    result = main("test14.txt")
    end = time.time()
    expected = 136
    assert result == expected, f"Expected {expected} but got {result}"
    print(end - start)

    start = time.time()
    result = main("input14.txt")
    end = time.time()
    expected = 106186
    assert result == expected, f"Expected {expected} but got {result}"
    print(result)
    print(end - start)
    