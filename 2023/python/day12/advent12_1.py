import unittest
import time

# Lav rekursiv funktion der prøver alt

# index_n direkte før mængder af # (på den jeg er lige nu)
# check_preceding checker om der kan placeres en # der
# 

def main(file: str) -> int:
    with open(file) as f:
        liste : list[str] = f.read().splitlines()

        total_combs = 0

        for y, line in enumerate(liste):
            springs, nums = line.split(" ")
            nums = list(map(int,nums.split(",")))
            springs = list(springs)
            total_combs += find_combs(springs, nums, 0, 0)

        return total_combs

# Maybe more input
def find_combs(springs, nums, index, count):
    total = 0
    if index == len(springs): # If we are at the end and all is used good
        if len(nums) == 0:
            print(springs)
            return 1
        elif count == nums[0] and len(nums) == 1:
            print(springs)
            return 1
        else:
            return 0
        
    if springs[index] == "#":
        if (check_preceding(springs, index,nums, count)):
            total += find_combs(springs, nums, index+1, count+1)
        else:
            return total
    elif springs[index] == ".":
        if count > 0:
            if count == nums[0]:
                total += find_combs(springs, nums[1::], index+1, 0)
            else:
                return total
        else:
            total += find_combs(springs, nums, index+1, 0)
    else:
        if (check_preceding(springs, index,nums, count)):
            springs[index] = "#"
            total += find_combs(springs, nums, index+1, count+1)
            springs[index] = "?"
            if count == 0:
                springs[index] = "."
                total += find_combs(springs, nums, index+1, 0)
                springs[index] = "?"
        else:
            if count > 0:
                if count == nums[0]:
                    springs[index] = "."
                    total += find_combs(springs, nums[1::], index+1, 0)
                    springs[index] = "?"
            else:
                springs[index] = "."
                total += find_combs(springs, nums, index+1, 0)
                springs[index] = "?"
    return total

def check_preceding(springs, index, nums , count):
    if len(nums) == 0:
        return False
    return count < nums[0]
    if index == 0:               # We are at start
        return True
    if index_n == 0 and springs[index-1] == ".": # If we are at start of indexing number and prev is .
        return True 
    for i in range(index_n+1, 0, -1): # We check precedings of # is equal to the number
        if springs[index-i] != "#":
            return False
    if index-(index_n+2) == 0: # IDK
        return True
    if springs[index-(index_n+2)] == ".":
        return True
    else:
        return False

if __name__ == "__main__":
    
    start = time.time()
    result = main("test12.txt")
    end = time.time()
    expected = 21
    assert result == expected, f"Expected {expected} but got {result}"
    print(end - start)

    start = time.time()
    result = main("input12.txt")
    end = time.time()
    #assert result == 6717, f"Expected 6717 but got {result}"
    print(result)
    print(end - start)
    