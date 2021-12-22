filename = "input9.txt"
import re

results = []

with open(filename) as f:
    liste = f.read().splitlines()

    res = re.findall('\d', liste[0])
    print(res)