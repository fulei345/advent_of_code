import unittest
import re as regex
import time

# Only loops over once

def main(file: str) -> int:
    with open(file) as f:
        liste : list[str] = f.read().splitlines()
        
        temp = liste[0].split(":")[1].split("|")[0]
        temp = len(regex.findall(r"\d+", temp))

        next_numbers = [0] * (temp + 1)
        result_sum = 0
        for line in liste:
            numbers = line.split(":")[1]
            winning, card = numbers.split("|")
            winning = regex.findall(r"\d+", winning)
            card = regex.findall(r"\d+", card)

            points = 0
            for num in winning:
                if num in card:
                    points += 1
            result_sum += next_numbers[0] + 1

            for i in range(1, points + 1):
                next_numbers[i] += next_numbers[0]+1
            # Move
            for i in range(1, len(next_numbers)):
                next_numbers[i-1] = next_numbers[i]
            next_numbers[-1] = 0

        return result_sum    
        

class TestStringMethods(unittest.TestCase):

    def testtest(self):
        self.assertEqual(main("test04.txt"), 30)

if __name__ == "__main__":
    start = time.time()
    print(main("input04.txt"))
    end = time.time()
    print(end - start)
    unittest.main()
    