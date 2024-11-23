def check_not_common(liste, length):
    set_var = set(liste)
    return len(set_var) == length

def main(filename):
    with open(filename) as f:
        for line in f:
            communication = line[0:len(line)-1]
            for i in range(len(communication) - 3):
                if check_not_common(communication[i:i+4],4):
                    print(i+4)
                    break
            for i in range(len(communication) - 13):
                if check_not_common(communication[i:i+14],14):
                    print(i+14)
                    break

            




if __name__ == "__main__":
    main("input/test6.txt")
    main("input/input6.txt")
