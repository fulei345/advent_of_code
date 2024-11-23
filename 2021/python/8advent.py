filename = "input/input8.txt"

results = []

with open(filename) as f:
    liste = f.read().splitlines()
    liste = [line.split('|') for line in liste]

    number_list = [line[0] for line in liste]
    four_digit_list = [line[1] for line in liste]

    results = []
    know_count = []

    four_digit_list = [line.split() for line in four_digit_list]
    number_list = [line.split() for line in number_list]

    dict_list = []
    num_dict = dict()

    # First part

    for i, line in enumerate(four_digit_list):
        result_temp = []
        know_count.append(0)
        num_dict = dict()
        # To count the val on rigth side
        for num in line:
            length = len(num)
            if length == 2:
                result_temp.append(1)
                know_count[-1] += 1
            elif length == 3:
                result_temp.append(7)
                know_count[-1] += 1
            elif length == 4:
                result_temp.append(4)
                know_count[-1] += 1
            elif length == 7:
                result_temp.append(8)
                know_count[-1] += 1
            else:
                result_temp.append(-1)
        # To save the num_dict
        for num in number_list[i]:
            length = len(num)
            if length == 2:
                num_dict.update({1: set(num)})
            elif length == 3:
                num_dict.update({7: set(num)})
            elif length == 4:
                num_dict.update({4: set(num)})
            elif length == 7:
                num_dict.update({8: set(num)})
        dict_list.append(num_dict)
        results.append(result_temp)


    print(sum(know_count))

    ls = 0

    for i, line in enumerate(number_list):
        line.sort(key=len)

        trans = {
    "a": "r",
    "b": "r",
    "c": "r",
    "d": "r",
    "e": "r",
    "f": "r",
    "g": "r"
    }

        set_list = [set(num) for num in line]
        num_dict = dict_list[i]

        a_ = num_dict[7].difference(num_dict[1])
        trans["a"] = next(iter(a_))

        # Find 6
        for k in range(6, 9):
            temp_set = set_list[k].difference(num_dict[4])
            one = num_dict[1].difference(set_list[k])
            if len(temp_set) == 2:
                num_dict.update({9: set_list[k]})
            elif len(temp_set) == 3:
                if len(one) == 1:
                    num_dict.update({6: set_list[k]})
                    trans["c"] = next(iter(one))
                    temp_set = num_dict[1].difference(one)
                    trans["f"] = next(iter(temp_set))
                elif len(one) == 0:
                    num_dict.update({0: set_list[k]})

        temp_set = num_dict[8].difference(num_dict[0])
        trans["d"] = next(iter(temp_set))

        temp_set = num_dict[8].difference(num_dict[9])
        trans["e"] = next(iter(temp_set))

        temp_set = num_dict[8].difference(num_dict[4])
        chair = set(trans.values())
        temp_set = temp_set.difference(chair)
        trans["g"] = next(iter(temp_set))

        chair = set(trans.values())
        temp_set = num_dict[8].difference(chair)
        trans["b"] = next(iter(temp_set))

        num_dict.update({2: {trans['a'], trans['c'], trans['d'],  trans['e'], trans['g']}})
        num_dict.update({3: {trans['a'], trans['c'], trans['d'],  trans['f'], trans['g']}})
        num_dict.update({5: {trans['a'], trans['b'], trans['d'],  trans['f'], trans['g']}})

        # Update the four digit list
        for index, num in enumerate(four_digit_list[i]):
            if results[i][index] == -1:
                temp_set = set(num)
                if len(temp_set) == 5:
                    if num_dict[2] == temp_set:
                        results[i][index] = 2
                        know_count[i] += 1
                    elif num_dict[3] == temp_set:
                        results[i][index] = 3
                        know_count[i] += 1
                    elif num_dict[5] == temp_set:
                        results[i][index] = 5
                        know_count[i] += 1
                elif len(temp_set) == 6:
                    if num_dict[6] == temp_set:
                        results[i][index] = 6
                        know_count[i] += 1
                    elif num_dict[0] == temp_set:
                        results[i][index] = 0
                        know_count[i] += 1
                    elif num_dict[9] == temp_set:
                        results[i][index] = 9
                        know_count[i] += 1

    summer = 0
    for line in results:
        for i, num in enumerate(line):
            if i == 0:
                summer += num * 1000
            elif i ==1:
                summer += num * 100
            elif i ==2:
                summer += num * 10
            elif i ==3:
                summer += num

    print(summer)

