def main(filename):
    count_1 = 0
    count_2 = 0
    with open(filename) as f:
        for line in f:
            pair_of_elves = line[0:len(line)-1]
            temp_list = pair_of_elves.split(",")
            first_section, second_section = temp_list[0], temp_list[1]
            
            first_range = first_section.split("-")
            second_range = second_section.split("-")

            first_list = [int(first_range[0]),int(first_range[1])]
            second_list = [int(second_range[0]),int(second_range[1])]

            if find_overlap_full(first_list, second_list):
                count_1 += 1
                count_2 += 1
            else:
                if find_overlap(first_list, second_list):
                    count_2 += 1

    print(count_1)
    print(count_2)

def find_overlap_full(first_list, second_list):
    if first_list[0] <= second_list[0] and first_list[1] >= second_list[1]:
        return True
    elif first_list[0] >= second_list[0] and first_list[1] <= second_list[1]:
        return True
    else:
        return False

def find_overlap(first_list, second_list):
    if first_list[0] <= second_list[0]:
        return first_list[1] >= second_list[0]
    elif first_list[0] >= second_list[0]:
        return first_list[0] <= second_list[1]
        


if __name__ == "__main__":
    main("input/test4.txt")
    main("input/input4.txt")
