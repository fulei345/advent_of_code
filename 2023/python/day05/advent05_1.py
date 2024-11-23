import unittest
import re as regex
import time

# Make a list of all the 
# Func that takes the current list of numbers and a mapping and do the shit to each number

def main(file: str) -> int:
    with open(file) as f:
        liste : list[str] = f.read().splitlines()
        temp = liste[0].split()
        seeds = list(map(int, temp[1:]))
        result_sum = 0
        names_list = []
        map_list = []
        liste = liste[1:]
        for y, line in enumerate(liste):
            name = line.find("map")
            if name != -1:
                names_list.append(line.split()[0])
                map_list.append([])
            else:
                numbers = list(map(int, regex.findall(r"\d+", line)))
                if len(numbers) == 0:
                    continue
                dest = numbers[0]
                source = numbers[1]
                d_range = numbers[2]
                map_list[-1].append([(dest,dest+d_range),(source,source+d_range)])

        for maps in map_list:
            seeds = map_all_funcs(maps, seeds)
        return min(seeds)    

def map_all_funcs(func, numbers):
    result = []
    for numb in numbers:
        number_appended = False
        for line in func:
            source_start = line[1][0]
            source_end = line[1][1]
            if source_start <= numb <= source_end:
                result.append(line[0][0] + (numb-source_start))
                number_appended = True
        if not number_appended:
            result.append(numb)
    return result

class TestStringMethods(unittest.TestCase):

    def testtest(self):
        self.assertEqual(main("test05.txt"), 35)

if __name__ == "__main__":


    start = time.time()
    print(main("input05.txt"))
    end = time.time()
    print(end - start)
    unittest.main()
    