#FILENAME = "input/test2.txt"
FILENAME = "input/input2.txt"

def main():
    total_list = load_data(FILENAME)
    first_count = 0
    second_count = 0
    for line in total_list:
        low, high, letter, string = line
        count = 0
        # First part
        for s in string:
            if s is letter:
                count += 1
                if count > high:
                    break

        if low <= count <= high:
            first_count += 1
        # Second
        if (letter is string[low-1] and not letter is string[high-1]) or (letter is string[high-1] and not letter is string[low-1]):
            second_count += 1
    print(first_count, second_count)


def load_data(path):
    total_list = []
    with open(path) as f:
        list = f.read().splitlines()
        for line in list:
            temp_list = [] # [Low ,High ,Letter, String]
            split = line.split() # [Low-High, Letter:, String]
            numbers = split[0].split('-')
            
            temp_list.append(int(numbers[0])) # Low
            temp_list.append(int(numbers[1])) # High
            temp_list.append(split[1][0]) # Letter
            temp_list.append(split[2]) # string
            total_list.append(temp_list)
    return total_list

if __name__ == '__main__':
    main()
