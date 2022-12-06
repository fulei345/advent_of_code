def check_not_common(liste):
    set_var = set(liste)
    return len(set_var) == 4

def main(filename):
    with open(filename) as f:
        for line in f:
            communication = line[0:len(line)-1]
            for i in range(len(communication) - 3):
                if check_not_common(communication[i:i+4]):
                    print(i+4)
                    break




if __name__ == "__main__":
    main("input/test6.txt")
    main("input/input6.txt")
