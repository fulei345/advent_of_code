with open("/home/fulei/git/advent_of_code/aoc_inputs/2024/day11input") as f:
    ls = f.read()

# Small example
# ls = "125 17"

liste = ls.split()


# List of things in difference categories
# 0, 1, even digits, odd digits
categories = [0, 0, 0, 0]
blinks = 75

for _ in range(blinks):
    new_liste = []
    for num in liste:
        if num == "0":
            new_liste.append("1")
        elif len(num) % 2 == 0:
            half = int(len(num)/2)
            new_liste.append(num[:half])
            second = int(num[half:])
            new_liste.append(str(second))
        else:
            real = int(num)
            new_liste.append(str(real*2024))
    liste = new_liste
        

    

print(len(liste))