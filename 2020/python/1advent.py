filename = "input1.txt"
with open(filename) as f:
    liste = f.read().splitlines()
    liste = list(map(int, liste))

    liste = [num for num in liste if num < 2020]

    for i, num1 in enumerate(liste):
        for k in range(i, len(liste)):
            for g in range(k, len(liste)):
                if num1 + liste[k] + liste[g] == 2020:
                    print(num1 * liste[k] * liste[g])