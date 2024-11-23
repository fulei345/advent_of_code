filename = "input/input10.txt"
#filename = "test10.txt"

with open(filename) as f:
    liste = f.read().splitlines()

    for_ = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
    }
    back_ = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
    }

    back_error_num = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
    }

    back_complete_num = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
    }

    error_points = 0
    complete_points = []
    for line in liste:
        stack = []
        complete = ""
        complete_point = 0
        for char in line:
            if char in for_.keys():
                stack.append(char)
            elif char in back_.keys():
                if len(stack) > 0:
                    if back_[char] == stack[-1]:
                        stack.pop()
                    else:
                        print("Expected", for_[stack.pop()], " Found", char)
                        error_points += back_error_num[char]
                        stack = []
                        break
        if len(stack) > 0:
            for cha in stack:
                complete = for_[cha] + complete
            for cha in complete:
                complete_point *= 5
                complete_point += back_complete_num[cha]
        if complete_point > 0:
            complete_points.append(complete_point)
            print(complete)

    complete_points.sort()
    print(error_points)
    print(complete_points[int(len(complete_points)/2)])


