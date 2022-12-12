def get_tallest_trees(forrest: list, direction: int):
    seen_trees = set()

    y_length = len(forrest[0])
    x_length = len(forrest)

    # Forloop
    # North
    if direction == 1 or direction == 3:
        for y in range(y_length):
            current_tallest = -1
            if direction == 1:
                for x in range(x_length):
                    tree = forrest[x][y]
                    if current_tallest < tree:
                        current_tallest = tree
                        seen_trees.add((x,y))
            elif direction == 3:
                for x in range(x_length-1,-1,-1):
                    tree = forrest[x][y]
                    if current_tallest < tree:
                        current_tallest = tree
                        seen_trees.add((x,y))
    elif direction == 2 or direction == 4:
        for x in range(x_length):
            current_tallest = -1
            if direction == 2:
                for y in range(y_length-1,-1,-1):
                    tree = forrest[x][y]
                    if current_tallest < tree:
                        current_tallest = tree
                        seen_trees.add((x,y))

            elif direction == 4:
                for y in range(y_length):
                    tree = forrest[x][y]
                    if current_tallest < tree:
                        current_tallest = tree
                        seen_trees.add((x,y))
    return seen_trees

def tree_score(point: tuple, forrest: list):
    x_point, y_point = point
    y_length = len(forrest[0])
    x_length = len(forrest)

    tree_height = forrest[x_point][y_point]
    score = 1

    
    temp = 0
    for x in range(x_point+1, x_length):
        if forrest[x][y_point] < tree_height:
            temp += 1
        else:
            temp += 1
            break
    score *= temp

    temp = 0
    for x in range(x_point-1, -1, -1):
        if forrest[x][y_point] < tree_height:
            temp += 1
        else:
            temp += 1
            break
    score *= temp

    temp = 0
    for y in range(y_point+1, y_length):
        if forrest[x_point][y] < tree_height:
            temp += 1
        else:
            temp += 1
            break
    score *= temp

    temp = 0
    for y in range(y_point-1, -1, -1):
        if forrest[x_point][y] < tree_height:
            temp += 1
        else:
            temp += 1
            break
    score *= temp

    return score

def main(filename):
    forrest = []
    with open(filename) as f:
        for line in f:
            tree_line = line[0:len(line)-1]
            temp_line = []
            for tree in tree_line:
                temp_line.append(int(tree))
            forrest.append(temp_line)
    
    tallest = set()
    tallest = tallest.union(get_tallest_trees(forrest, 1))
    tallest = tallest.union(get_tallest_trees(forrest, 2))
    tallest = tallest.union(get_tallest_trees(forrest, 3))
    tallest = tallest.union(get_tallest_trees(forrest, 4))
    print(len(tallest))

    highest_score = 0
    for tree in tallest:
        temp = tree_score(tree, forrest)
        if temp > highest_score:
            highest_score = temp

    print(highest_score) 

    #print(tree_score((3,2), forrest))
if __name__ == "__main__":
    main("input/test8.txt")
    main("input/input8.txt")
