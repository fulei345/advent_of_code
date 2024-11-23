filename = "input/input6.txt"

# simulate n timestep on a liste
def simulate(input, n):
    working = input
    for i in range(n):
        temp = [0] * 9
        for i in range(1, 9):
            temp[i-1] = working[i]
        temp[8] = working[0]
        temp[6] += working[0]
        working = temp
    return working

with open(filename) as f:
    liste = f.read().splitlines()
    liste = liste[0].split(',')
    liste = list(map(int, liste))

    all_lol = [0] * 9

    for num in liste:
        all_lol[num] += 1

    # First exercise
    print(sum(simulate(all_lol, 80)))

    # Second exercise
    print(sum(simulate(all_lol, 256)))


