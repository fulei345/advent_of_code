def main(filename):
    with open(filename) as f:
        left = []
        right = []
        left_done = False
        right_done = False
        index = 1
        result = []
        for line in f:
            if line == "\n":
                left = []
                right = []
                left_done = False
                right_done = False
                continue
            l = line[0:len(line)-1]

            if len(l) == 1:
                num = int(l)
                if left_done:
                    right.append(num)
                    right_done = True
                else:
                    left_done = True
                    left.append(num)
            else:
                if left_done:
                    right,_ = parse_list(l,0)
                    right_done = True
                else:
                    left_done = True
                    left,_ = parse_list(l,0)

            if left_done and right_done:
                # print(left)
                # print(right)
                temp = compare_lists(left, right)
                if temp:
                    result.append(index)
                # print(compare_lists(left, right))
                index += 1
    print(sum(result))

def compare_lists(left: list, right: list):
    l_len = len(left)
    r_len = len(right)
    
    if l_len == 0 and r_len == 0:
        return None
    elif l_len == 0:
        return True
    elif r_len == 0:
        return False
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
                if result is not None:
                    return result
                elif not result:
                    return False
            else:
                result = compare_lists(l, r)
                if result is not None:
                    return result
        else:
            if l_type == int:
                l = [l]
            else:
                r = [r]
            result = compare_lists(l, r)
            if result is not None:
                return result
        index += 1
    if l_len == index and r_len == index:
        return None
    elif l_len == index:
        return True
    elif r_len == index:
        return False


                            
    # Something about indexing ?

def compare_num(left: int, right: int):
    if left < right:
        return True
    elif right < left:
        return False
    else:
        return None


def parse_list(l: list, index):
    temp = []
    new_index = index
    seen_new = False
    while new_index < len(l):
        if l[new_index] == "[":
            if not seen_new:
                seen_new = True
            else:
                num, new_index = parse_list(l, new_index)
                temp.append(num)
        elif l[new_index] == ",":
            pass
        elif l[new_index] == "]":
            return temp, new_index
        else:
            temp.append(int(l[new_index]))
        new_index += 1
    return None

if __name__ == "__main__":
    # main("22/input/test13.txt")
    main("22/input/input13.txt")
