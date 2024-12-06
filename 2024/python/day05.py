with open("/home/fulei/git/advent_of_code/aoc_inputs/2024/day05input") as f:
    ls = f.read().strip().split("\n\n")

mappings = ls[0].splitlines()
update = ls[1].splitlines()

map = {}

for i in mappings:
    (left, right) = i.split("|")
    if left not in map:
        map[left] = [right]
    else:
        liste = map[left]
        liste.append(right)
        map[left] = liste

def check_line(nums: list, map: dict):
    for index, char in enumerate(nums):
        if char in map:
            before = map[char]
            for b in before:
                if b in nums:
                    after_index = nums.index(b)
                    if index > after_index:
                        return False, b, index
    return True, "lol", 0
    

sum = 0
for u in update:
    # Line
    check = True
    nums = u.split(",")
    for index, char in enumerate(nums):
        if char in map:
            before = map[char]
            for b in before:
                if b in nums:
                    after_index = nums.index(b)
                    if index > after_index:
                        check = False
    if check:
        sum = sum + int(nums[int(len(nums)/2)])
print(sum)



sum = 0
for u in update:
    # Line
    nums = u.split(",")
    check, char, index = check_line(nums, map)
    bad = False
    while not check:
        nums.remove(char)
        nums.insert(index, char)
        check, char, index = check_line(nums, map)
        bad = True
    if bad:
        sum = sum + int(nums[int(len(nums)/2)])

print(sum)
        

