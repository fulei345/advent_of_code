filename = "input/input1.txt"

def day1_pt1(nums):
    return increasing(nums, 1)

def day1_pt2(nums):
    return increasing(nums, 3)

# Length of window.
# Just needs to compare the first and last in the windows since the others overlap
def increasing(nums, window: int):
    return sum(nums[i] > nums[i-window] for i in range(window, len(nums)))

with open(filename) as f:
    liste = f.read().splitlines()
    liste = list(map(int, liste))

    print(day1_pt1(liste))
    print(day1_pt2(liste))