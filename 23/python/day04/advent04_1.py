import unittest
import re as regex
import time

# Split on : and split on |
# Use regex againg and find alle the numbers
# Lav winning numbers og numbers
# check for hvert winning og ryk 1 til venstre



def main(file: str) -> int:
    with open(file) as f:
        liste : list[str] = f.read().splitlines()
        
        result_sum = 0
        for y, line in enumerate(liste):
            numbers = line.split(":")[1]
            winning, card = numbers.split("|")
            winning = regex.findall(r"\d+", winning)
            card = regex.findall(r"\d+", card)

            point = 0
            is_set = False
            for num in winning:
                if num in card:
                    if not is_set:
                        point = 1
                        is_set = True
                    else:
                        point = point << 1
            
            result_sum += point

        return result_sum    
        

class TestStringMethods(unittest.TestCase):

    def testtest(self):
        self.assertEqual(main("test04.txt"), 13)

if __name__ == "__main__":


    start = time.time()


    print(main("input04.txt"))
    end = time.time()
    print(end - start)
    unittest.main()
    