with open("/home/fulei/git/advent_of_code/aoc_inputs/2024/day09input") as f:
    ls = f.read()

# Small example
# ls = "2333133121414131402"

new_liste = []

block_index = 0
for index, char in enumerate(ls):
    value = int(char)
    if index % 2 == 0:
        for i in range(value):
            new_liste.append(str(block_index))
        block_index += 1
    else:
        for i in range(value):
            new_liste.append(".")


while '.' in new_liste:
    new = new_liste.pop()
    if new != '.':
        new_index = new_liste.index('.')
        new_liste[new_index] = new

result = 0
for index, num in enumerate(new_liste):
    if num != ".":
        result += int(num) * index

print(result)