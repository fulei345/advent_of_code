with open("/home/fulei/git/advent_of_code/aoc_inputs/2024/day09input") as f:
    ls = f.read()

#Small example

# ls = "2333133121414131402"

new_liste = []

files_values = []
files_indexes = []
# Indexes is their number index, and their index in the index file
# Values is how many are there

empty_values = []
empty_indexes = []

block_index = 0
for index, char in enumerate(ls):
    value = int(char)
    if index % 2 == 0:
        files_indexes.append(block_index)
        for i in range(value):
            new_liste.append(str(block_index))
        files_values.append(value)
        block_index += 1
    else:
        empty_indexes.append(len(new_liste))
        for i in range(value):
            new_liste.append(".")
        empty_values.append(value)

for i in range(len(files_indexes)-1, -1, -1):
    how_many = files_values[i]
    for index, k in enumerate(empty_values):
        if k >= how_many:
            remove_index = new_liste.index(str(files_indexes[i]))
            for l in range(empty_indexes[index], empty_indexes[index]+how_many):
                new_liste[l] = str(files_indexes[i])

            for l in range(remove_index, remove_index+how_many):
                new_liste[l] = "."
            empty_values[index] -= how_many
            empty_indexes[index] += how_many 
            # print("".join(new_liste))
            break


result = 0
for index, num in enumerate(new_liste):
    if num != ".":
        result += int(num) * index

# print(new_liste)
print(result)