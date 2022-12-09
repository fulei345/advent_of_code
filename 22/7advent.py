def main(filename):
    cd = Directory("", None)
    all_folders =[]
    with open(filename) as f:
        for line in f:
            cmdline = line[0:len(line)-1]
            cmdline = cmdline.split(" ")
            # Command
            if cmdline[0] == "$":
                if cmdline[1] == "cd":
                    if cmdline[2] == "/":
                        cd = Directory("/", None)
                    elif cmdline[2] == "..":
                        # Count folder and go up
                        if cd.parent != None:
                            all_folders.append(count_folder(cd))
                            cd = cd.parent
                    else:
                        # Change directory
                        cd = cd.dirs[cmdline[2]]
                elif cmdline[1] == "ls":
                    pass
            else:
                # List dir
                if cmdline[0] == "dir":
                    temp = Directory(cmdline[1], cd)
                    cd.dirs[cmdline[1]] = temp
                else:
                    # List file
                    cd.files[cmdline[1]] = int(cmdline[0])
        
    # Count the rest of the folders going up
    while cd.parent != None:
        all_folders.append(count_folder(cd))
        cd = cd.parent
    all_folders.append(count_folder(cd))
    all_folders.sort()

    print(sum([num for num in all_folders if num <= 100_000]))

    # Calc space needed to delete
    total_size = 70000000
    upgrade = 30000000
    used = all_folders[-1]
    unused = total_size - used
    free_space = upgrade - unused
    
    # Find folder to delete
    index = -1
    temp_total = 70000000
    while temp_total > free_space:
        index -= 1
        temp_total = all_folders[index]
    print(all_folders[index+1])

# Count files in folder and add to parent
def count_folder(cd):
    for key, value in cd.files.items():
        cd.total_size += value
    if cd.parent != None:
        cd.parent.total_size += cd.total_size
    return cd.total_size

class Directory:
    # Name of the folder
    # Dictionary of its files
    # Pointer to parent dict
    # Total size
    def __init__(self, name, parent):
        self.name = name
        self.files = dict()
        self.parent = parent
        self.dirs = dict()
        self.total_size = 0
        
    def __str__(self) -> str:
        result = "Name: "+ self.name + "\n"
        result += "Files: "
        for key, value in self.files.items():
            result += key + " "
        result += "Dirs: "
        for key, value in self.dirs.items():
            result += key + " "
        result += "\n Total size: " + str(self.total_size) 
        return result



if __name__ == "__main__":
    main("input/test7.txt")
    main("input/input7.txt")
