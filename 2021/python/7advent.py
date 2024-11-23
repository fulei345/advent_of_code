filename = "input/input7.txt"

def bruteforce(input):
    smallest_sum = 10000000000
    for i in range(min(input), max(input) + 1):
        small_sum = 0
        for num in input:
            temp = abs(i-num)
            small_sum += sum(range(temp + 1))
        if small_sum < smallest_sum:
            smallest_sum = small_sum
    return smallest_sum


with open(filename) as f:
    liste = f.read().splitlines()
    liste = liste[0].split(',')
    liste = list(map(int, liste))
    liste.sort()

    test_input = [16,1,2,0,4,2,7,1,2,14]

    print(bruteforce(test_input))
    print(bruteforce(liste))

