FILENAME = "input/input14.txt"
#FILENAME = "input/test14.txt"

def main():
    func_dict, func_list, input_string, alphabet = load_data(FILENAME)

    first = input_string[0]
    last = input_string[-1]

    for i in range(len(input_string)-1):
        s = input_string[i:i+2]
        if s in func_dict.keys():
            func_list[func_dict[s][1]] += 1

    for i in range(40):
        func_list = one_step(func_dict, func_list)

    for i, key in enumerate(func_dict.keys()):
        alphabet[key[0]] += func_list[i]
        alphabet[key[1]] += func_list[i]

    alphabet[first] += 1
    alphabet[last] += 1

    for i, key in enumerate(alphabet.keys()):
        alphabet[key] /= 2

    print(first)
    print(last)
    print(alphabet)

    result_list = list(alphabet.values())
    result_list.sort()
    print(result_list[-1]-result_list[0])
    # Save first and last to count

def one_step(func_dict, func_list):
    temp_list = [0] * len(func_list)
    key_list = list(func_dict.keys())
    for i in range(len(key_list)):
        key = key_list[i]
        result = func_dict[key][0]
        index = func_dict[key][1]
        insert_list = []
        insert_list.append(key[0] + result)
        insert_list.append(result + key[1])
        for s in insert_list:
            if s in key_list:
                sindex = func_dict[s][1]
                temp_list[sindex] += func_list[index]
    return temp_list

# Makes a dictionary and a string
def load_data(path):
    with open(path) as f:
        alphabet = dict()
        func = dict()
        func_list = []
        liste = f.read().splitlines()
        input_string = liste[0]
        for i, line in enumerate(liste):
            if i > 1:
                temp = line.split(' -> ')
                func_list.append(0)
                func.update({temp[0]: [temp[1], len(func_list) -1]})
                keys = alphabet.keys()
                temp_list = [temp[0][0], temp[0][1], temp[1]]
                for alf in temp_list:
                    if alf not in keys:
                        alphabet.update({alf: 0})

    return func, func_list, input_string, alphabet

if __name__ == '__main__':
    main()