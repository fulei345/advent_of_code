from functools import cmp_to_key

def main2(filename):
    with open(filename) as f:
        lines = []
        result = []
        for line in f:
            temp = []
            if line == "\n":
                continue
            l = line[0:len(line)-1]
            

            if len(l) == 1:
                num = int(l)
                temp.append(num)
            else:
                temp,_ = parse_list(l,0)
            lines.append(temp)
        lines.append([[2]])
        lines.append([[6]])
    
    lol = sorted(lines, key=cmp_to_key(compare_lists))
    for index, l in enumerate(lol):
        if l == [[2]] or l == [[6]]:
            result.append(index+1)
    print(result[0] * result[1])

def main(filename):
    with open(filename) as f:
        lines = []
        index = 1
        result = []
        for i, line in enumerate(f):
            temp = []
            if line == "\n":
                lines = []
                continue
            l = line[0:len(line)-1]
            if len(l) == 1:
                num = int(l)
                temp.append(num)
                lines.append(temp)
            else:
                temp, _ = parse_list(l,0)
                lines.append(temp)

            if (i+2) % 3 == 0:
                temp = compare_lists(lines[0], lines[1])
                if temp < 0:
                    result.append(index)
                index += 1
    print(sum(result))

def compare_lists(left: list, right: list):
    l_len = len(left)
    r_len = len(right)
    
    index = 0
    max_length = min(l_len, r_len)
    while index < max_length:
        l = left[index]
        r = right[index]
        l_type = type(l)
        r_type = type(r)
        if l_type == r_type:
            if l_type == int:
                result = compare_num(l, r)
                if not result == 0:
                    return result
            else:
                result = compare_lists(l, r)
                if not result == 0:
                    return result
        else:
            if l_type == int:
                l = [l]
            else:
                r = [r]
            result = compare_lists(l, r)
            if not result == 0:
                return result
        index += 1
    if l_len == index and r_len > index:
        return -1
    elif l_len == index and r_len == index:
        return 0
    else:
        return 1


                            
    # Something about indexing ?

def compare_num(left: int, right: int):
    if left == right:
        return 0
    elif left > right:
        return 1
    else:
        return -1


def parse_list(l: list, index):
    temp = []
    new_index = index
    seen_new = False
    num_string = ""
    while new_index < len(l):
        if l[new_index] == "[":
            if not seen_new:
                seen_new = True
            else:
                num, new_index = parse_list(l, new_index)
                temp.append(num)
        elif l[new_index] == ",":
            if num_string != "":
                temp.append(int(num_string))
                num_string = ""
        elif l[new_index] == "]":
            if num_string != "":
                temp.append(int(num_string))
                num_string = ""
            return temp, new_index
        else:
            num_string = num_string + l[new_index]
        new_index += 1
    return None

if __name__ == "__main__":
    # main("22/input/test13.txt")
    # main("22/input/input13.txt")
    main2("22/input/test13.txt")
    main2("22/input/input13.txt")
