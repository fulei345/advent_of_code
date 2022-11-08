# FILENAME = "input/test2.txt"
FILENAME = "input/input2.txt"


def main():
    pass

def load_data(path):
    with open(path) as f:
        total_count = 0
        liste = f.read().splitlines()
        for line in liste:
            split = line.split()
            numbers = split[0].split('-')

            
            low_num = int(numbers[0])
            high_num = int(numbers[1])
            alhpa = split[1][0]


            """ count = 0
            for s in split[2]:
                if s is alhpa:
                    count += 1
                    if count > high_num:
                        break
            if count < low_num:
                continue
            if low_num <= count <= high_num:
                total_count += 1 """
            if (split[2][low_num-1] is alhpa and not split[2][high_num-1] is alhpa ) or split[2][high_num-1] is alhpa and not split[2][low_num-1] is alhpa:
                total_count += 1
        print(total_count)

if __name__ == '__main__':
    load_data(FILENAME)