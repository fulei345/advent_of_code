def main(filename):
    with open(filename) as f:
        left = []
        right = []
        left_done = False
        right_done = False
        index = 1
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
                print(left)
                print(right)

def compare_lists(left: list, right: list):
    if len(left) == 0:
        return True
    elif len(right) == 0:
        return False
    # Something about indexing ?




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
    main("22/input/test13.txt")
    # main("22/input/input13.txt")
