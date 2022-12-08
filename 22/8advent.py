def main(filename):
    mapps = []
    with open(filename) as f:
        liste = f.read().splitlines()

        for line in liste:

            res = re.findall('\d', line)
            res = list(map(int, res))
            mapps.append(res)

        tallest_trees = []
        basins_size = []

        rows, cols = (len(mapps), len(mapps[0]))
        arr = [[0 for i in range(cols)] for j in range(rows)]


        # Loop over from all sides
        # North 1
        # East 2
        # South 3
        # West 4

        for i, line in enumerate(mapps):
            for k, num in enumerate(line):
                if arr[i][k] == 0:
                arr, high, lowest =check_basin(arr, mapps, i, k)
                if high > 0:
                    low_points.append(lowest)
                    basins_size.append(high)



        
    # Count the rest of the folders going up
    while cd.parent != None:
        all_folders.append(count_folder(cd))
        cd = cd.parent
    all_folders.append(count_folder(cd))
    all_folders.sort()

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

    print(part1(cd))

# Find size of small folders
def part1(cd):
    temp = 0
    for key, value in cd.dirs.items():
        temp += part1(cd.dirs[key])
    if 100000 >= cd.fullsize:
        temp += cd.fullsize
    return temp

# Count files in folder and add to parent
def count_folder(cd):
    for key, value in cd.files.items():
        cd.fullsize += value
    if cd.parent != None:
        cd.parent.fullsize += cd.fullsize
    return cd.fullsize

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
        self.under = False
        self.fullsize = 0
        
    def __str__(self) -> str:
        result = "Name: "+ self.name + "\n"
        result += "Files: "
        for key, value in self.files.items():
            result += key + " "
        result += "Dirs: "
        for key, value in self.dirs.items():
            result += key + " "
        result += "\nFullsize: " + str(self.fullsize) 
        return result



if __name__ == "__main__":
    main("input/test7.txt")
    main("input/input7.txt")
