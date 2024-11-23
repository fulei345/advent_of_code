def main(filename):
    maze = []
    start_nodes: list[Node] = []
    with open(filename) as f:
        index = 0
        for line in f:
            l = line[0:len(line)-1]
            temp_line = []
            for i, square in enumerate(l):
                if square == "S" or square == "a":
                    temp: Node = Node((i,index), 0, None, 0)
                    start_nodes.append(temp)
                    temp_line.append(0)
                elif square == "E":
                    end_point = (i,index)
                    temp_line.append(26)
                else:
                    temp_line.append(ord(square)-97)
            maze.append(temp_line)
            index += 1



    for line in maze:
        print(line)


    # Part2
    seen : list[Node] = start_nodes
    frontier: list[Node] = []
    for node in seen:
        temp = neighbors(node, seen, maze, frontier)
        frontier.extend(temp)
    
    highest_score = -1000
    for i, node in  enumerate(frontier):
        if node.calc_score(end_point) > highest_score:
            highest_node = node
            highest_score = node.score
    seen.append(highest_node)
    frontier.remove(highest_node)


    # start: Node = Node(start_point, 0, None, -1)
    # highest_score = -1000
    # highest_node = start
    # frontier: list[Node] = []
    # seen : list[Node] = []
    # seen.append(start)

    while highest_node.height != 26:
        changed = False
        temp = neighbors(highest_node, seen, maze, frontier)
        for node in temp:
            if node.calc_score(end_point) > highest_score:
                highest_score = node.score
                highest_node = node
                changed = True
        frontier.extend(temp)
        if len(frontier) == 0:
            break
        if not changed:
            highest_score = -1000
            for i, node in  enumerate(frontier):
                if node.score > highest_score:
                    highest_node = node
                    highest_score = node.score
        seen.append(highest_node)
        frontier.remove(highest_node)

    print(highest_node.length)
        

class Node:
    def __init__(self, point: tuple, length: int, prev: any, height):
        self.point = point
        self.length = length
        self.prev = prev
        self.height = height
        self.score = 0

    def calc_score(self, end: tuple):
        self.score = self.height - distance(self.point, end) - self.length
        return self.score


def neighbors(node: Node, seen: list[Node], maze: list[list[int]], frontier: list[Node]) -> list: 
    temp = []
    x = node.point[0]
    y = node.point[1]
    width = len(maze[0])-1
    height = len(maze)-1

    new_node = get_neighbor(x, y+1, width, height, node, seen, maze, frontier)
    if new_node != None:
        temp.append(new_node)
    
    new_node = get_neighbor(x+1, y, width, height, node, seen, maze, frontier)
    if new_node != None:
        temp.append(new_node)

    new_node = get_neighbor(x, y-1, width, height, node, seen, maze, frontier)
    if new_node != None:
        temp.append(new_node)

    new_node = get_neighbor(x-1, y, width, height, node, seen, maze, frontier)
    if new_node != None:
        temp.append(new_node)
    
    return temp

def get_neighbor(new_x: int, new_y: int, width: int, height: int, node: Node, seen: list[Node], maze: list[list[int]], frontier: list[Node]):
    if 0 <= new_x <= width and 0 <= new_y <= height:
        new_height: int = maze[new_y][new_x]
        if new_height-1 <= node.height:
            new_node: Node = check_nodes((new_x,new_y), seen)
            if new_node != None:
                if new_node.length > node.length + 1:
                    new_node.prev = node
                    new_node.length = node.length + 1
            else:
                frontier_node: Node = check_nodes((new_x,new_y), frontier)
                if frontier_node != None:
                    if frontier_node.length > node.length + 1:
                        temp_node: Node = Node((new_x,new_y), node.length + 1, node, new_height)
                        return temp_node
                else:
                    temp_node: Node = Node((new_x,new_y), node.length + 1, node, new_height)
                    return temp_node
    return None


def check_nodes(new_point: tuple, list:list[Node]):
    for node in list:
        if node.point == new_point:
            return node
    return None

def distance(current, end):
    x_1, y_1 = current
    x_2, y_2 = end
    return abs(x_1 - x_2) +  abs(y_1 - y_2)


if __name__ == "__main__":
    #main("22/input/test12.txt")
    main("22/input/input12.txt")
