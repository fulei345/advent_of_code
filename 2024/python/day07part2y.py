with open("/home/fulei/git/advent_of_code/aoc_inputs/2024/day07input") as f:
    ls = f.read().strip().splitlines()
# ls: list = """190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20""".splitlines()

sum = 0

def check_line(testvalue: int, calibrator: list, current_sum):
    if len(calibrator) == 0:
        return testvalue == current_sum
    elif current_sum > testvalue:
        return False
    next_sum = int(str(current_sum) + str(calibrator[0]))
    if check_line(testvalue, calibrator[1::], next_sum):
        return True
    next_sum = current_sum * calibrator[0]
    if check_line(testvalue, calibrator[1::], next_sum):
        return True
    next_sum = current_sum + calibrator[0] 
    return check_line(testvalue, calibrator[1::], next_sum)



for line in ls:
    testvalue, calibrators = line.split(":")
    testvalue: int = int(testvalue)
    calibrators = calibrators.split()
    calibrators= list(map(int, calibrators))
    
    if check_line(testvalue, calibrators[1::], calibrators[0]):
        sum += testvalue

print(sum)



