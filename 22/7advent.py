def main(filename):
    cd = Directory("", None)
    with open(filename) as f:
        for line in f:
            cmdline = line[0:len(line)-1]
            cmdline = cmdline.split(" ")
            if cmdline[0] == "$":
                if cmdline[1] == "cd":
                    if cmdline[2] == "/":
                        cd = Directory("/", None)
                    elif cmdline[2] == "..":
                        if cd.parent != None:
                            cd = cd.parent
                            # Count dirs and send that also
                    else:
                        cd = cd.dirs[cmdline[2]]
                elif cmdline[1] == "ls":
                    pass
            else:
                if cmdline[0] == "dir":
                    temp = Directory(cmdline[1], cd)
                    cd.dirs[cmdline[1]] = temp
                else:
                    cd.files[cmdline[1]] = int(cmdline[0])

    while cd.parent != None:
        cd = cd.parent

    all_sizes = []
    count_files(cd,all_sizes)
    all_sizes.sort()

    total_size = 70000000
    upgrade = 30000000
    used = all_sizes[-1]
    unused = total_size - used
    free_space = upgrade - unused
    
    index = -1
    temp_total = 70000000
    while temp_total > free_space:
        index -= 1
        temp_total = all_sizes[index]
    print(all_sizes[index+1])


    while cd.parent != None:
        cd = cd.parent
    print(part1(cd))

    
def count_files(cd, list):
    for key, value in cd.files.items():
        cd.fullsize += value
    for key, value in cd.dirs.items():
        cd.fullsize += count_files(cd.dirs[key],list)
    if cd.fullsize <= 100000:
        cd.under = True
    list.append(cd.fullsize)
    return cd.fullsize

def part1(cd):
    temp = 0
    for key, value in cd.dirs.items():
        temp += part1(cd.dirs[key])
    if cd.under:
        temp += cd.fullsize
    return temp

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.files = dict()
        self.parent = parent
        self.dirs = dict()
        self.under = False
        self.fullsize = 0
        
    def __str__(self) -> str:
        lol = "Name: "+ self.name + "\n"
        lol += "Files: "
        for key, value in self.files.items():
            lol += key + " "
        lol += "Dirs: "
        for key, value in self.dirs.items():
            lol += key + " "
        lol += "\nFullsize: " + str(self.fullsize) 
        return lol



if __name__ == "__main__":
    # main("input/test7.txt")
    main("input/input7.txt")
