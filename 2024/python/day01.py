filename = "/home/fulei/git/advent_of_code/aoc_inputs/2024/day1input"

def part1(input):
    liste = input.splitlines()

    rightcol = []
    leftcol = []
    for l in liste:
        lol = l.split()
        leftcol.append(int(lol[0]))
        rightcol.append(int(lol[1]))

    rightcol.sort()
    leftcol.sort()

    result = 0
    for (l, r) in zip(rightcol, leftcol):
        result += abs(l-r)

    return result

def part2(input):
    liste = input.splitlines()

    rightcol = []
    leftcol = []
    for l in liste:
        lol = l.split()
        leftcol.append(lol[0])
        rightcol.append(lol[1])

    dict = {}
    for s in rightcol:
        if s not in dict:
            dict[s] = 1
        else:
            dict[s] += 1

    result = 0
    for num in leftcol:
        if num in dict:
            result += int(num) * dict[num]

    return result

test_ = "3   4\n4   3\n2   5\n1   3\n3   9\n3   3"

# print(part1(test_))

print(part2(test_))

with open(filename) as f:
    input = f.read()
    print("part1: " + str(part1(input)))
    print("part2: " + str(part2(input)))