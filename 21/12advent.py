FILENAME = "input/input12.txt"
#FILENAME = "input/test12.txt"

def main():
    array, vert_dict = load_data(FILENAME)

    for line in array:
        print(line)

    final_count = find_all_paths(array, 'start', [], vert_dict, normal_check)
    print(final_count)
    final_count = find_all_paths(array, 'start', [], vert_dict, small_check)
    print(final_count)

def load_data(path):
    with open(path) as f:
        liste = f.read().splitlines()
        vertex = []
        edges = []
        vert_dict = dict()
        for line in liste:
            first, second = line.split('-')
            if first not in vertex:
                vertex.append(first)
                vert_dict.update({first: len(vertex)-1})
                vert_dict.update({len(vertex)-1: first})
            if second not in vertex:
                vertex.append(second)
                vert_dict.update({second: len(vertex)-1})
                vert_dict.update({len(vertex)-1: second})
            edges.append((first,second))

        rows, cols = (len(vertex), len(vertex))
        array = [[0 for i in range(cols)] for j in range(rows)]
        for first, second in edges:
            array[vert_dict[first]][vert_dict[second]] = 1
            array[vert_dict[second]][vert_dict[first]] = 1
        return array, vert_dict

def small_check(stack: list, dist: str):
    if dist == 'start':
        return False
    if dist.islower():
        temp_stack = [x for x in stack if x.islower()]
        if dist in stack and len(temp_stack) == len(set(temp_stack)):
            return True
        elif dist in stack and len(temp_stack) != len(set(temp_stack)):
            return False
        elif dist not in stack:
            return True
    return True

def normal_check(stack: list, dist: str):
    if dist == 'start':
        return False
    if dist.islower():
        if dist in stack:
            return False
    return True

def find_all_paths(paths : list, current: str, stack: list, vert_dict: dict, func):
    count = 0
    stack.append(current)
    if current == 'end':
        count += 1
        print(stack)
    else:
        for i, point in enumerate(paths[vert_dict[current]]):
            if point == 1:
                if func(stack, vert_dict[i]):
                    temp_count = find_all_paths(paths, vert_dict[i], stack, vert_dict, func)
                    count += temp_count
    stack.pop()
    return count

if __name__ == '__main__':
    main()
