# filename = "input/test1.txt"
filename = "../inputs/day1input"
with open(filename) as f:
    liste = f.read().splitlines()

    elf_list = []
    sum = 0
    for s in liste:
        if s == '':
            elf_list.append(sum)
            sum = 0
        else:
            sum += int(s)
    elf_list.sort()
    print(elf_list[-1])

    print(elf_list[-1] + elf_list[-2] + elf_list[-3])
