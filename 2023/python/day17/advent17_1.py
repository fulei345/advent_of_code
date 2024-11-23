import time
# Move crucible over map where we should minimize heat 
import heapq


class Node:
    def __init__(self, pos: tuple, g_value: int, h_value: int, parent: tuple, dir: int, prev_dir_num: int):

        self.pos: tuple = pos
        self.g_value: int = g_value
        self.h_value: int = h_value
        self.parent = parent
        self.dir: int = dir
        self.prev_dir_num : int = prev_dir_num
        self.f_value: int = g_value + h_value

    def __lt__(self, other):
        if self.h_value == other.h_value:
            if self.g_value == other.g_value:
                if self.pos[0] == other.pos[0]:
                    return self.pos[1] < other.pos[1]
            else:
                return self.g_value < other.g_value
        else:
            return self.h_value < other.h_value

    def __eq__(self, other):
        if other is None:
            return False
        pos_equal = self.pos[0] == other.pos[0] and self.pos[1] == other.pos[1]
        dir_and_prev = self.dir == other.dir and self.prev_dir_num == other.prev_dir_num 
        return pos_equal and dir_and_prev

def main(file: str) -> int:
    maps: list[list[int]] = None
    with open(file) as f:
        liste : list[str] = f.read().splitlines()
        for i in range(len(liste)):
            liste[i] = list(map(int, [*liste[i]]))
        maps = liste
    
    result = a_star(maps, (0,0), (len(maps)-1, len(maps[0])-1))
    return result
 
def a_star(maps: list, start_pos: tuple, end_pos: tuple):
    start = Node(start_pos, 0, 0, None, 2, 1)
    open_list = [start]
    heapq.heapify(open_list)
    closed_list = []
    while len(open_list) != 0:
        print(len(open_list))
        current = heapq.heappop(open_list)
        if current.pos[0] == end_pos[0] and current.pos[1] == end_pos[1]:
            break
        closed_list.append(current)
        neighbors: list[Node] = find_neighbors(current, maps, end_pos)
        for neighbor in neighbors:
            if check_liste(closed_list, neighbor):
                continue
            if check_liste(open_list, neighbor):
                continue
            else:
                heapq.heappush(open_list, neighbor)
                #open_list.append(neighbor)
    
    current = heapq.heappop(open_list)
    result = current.g_value
    dir_liste = ["<", "v", ">", "^"]
    while current.parent is not None:
        maps[current.pos[0]][current.pos[1]] = dir_liste[current.dir]
        current = current.parent
    for y in maps:
        temp = ""
        for x in y:
            temp += str(x)
        print(temp)
    return result

def check_liste(liste: list[Node], neighbor: Node):
    for i, prev_neighbor in enumerate(liste):
        if neighbor == prev_neighbor:
            if neighbor.g_value > prev_neighbor.g_value:
                return True
    return False

# Maybe it needs prev and the amount of times we did go in that direction
def find_neighbors(current: Node, maps: list, end_pos: tuple):
    legal_neighbors = []
    all_pos: list = [(0,-1), (1,0), (0,1), (-1,0)]
    opposite: list = [2, 3, 0, 1]
    for i, pos in enumerate(all_pos):
        new_y: int = current.pos[0] + pos[0]
        new_x: int = current.pos[1] + pos[1] 
        if new_y < 0 or new_x < 0 or new_y == len(maps) or new_x == len(maps[0]):
            continue
        elif opposite[i] == current.dir:
            continue
        else:
            new_nums = 1
            if current.dir == i:
                new_nums = current.prev_dir_num + 1
            if new_nums == 4: # If we already have 3 in a row
                continue
            new_g = current.g_value + maps[new_y][new_x]
            #new_h = manhatten_distance((new_y, new_x), end_pos)
            new_h = 0
            legal_neighbors.append(Node((new_y, new_x), new_g, new_h, current, i, new_nums))

    return legal_neighbors

def manhatten_distance(start: tuple, end: tuple):
    return abs(start[0]-end[0]) + abs(start[1]-end[1]) 

if __name__ == "__main__":
    
    start = time.time()
    result = main("test17.txt")
    end = time.time()
    expected = 102
    assert result == expected, f"Expected {expected} but got {result}"
    print(end - start)

    start = time.time()
    result = main("input17.txt")
    end = time.time()
    expected = 7798
    assert result == expected, f"Expected {expected} but got {result}"
    print(end - start)
    

    #https://old.reddit.com/r/adventofcode/comments/18luw6q/2023_day_17_a_longform_tutorial_on_day_17/