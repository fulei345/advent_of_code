import unittest
import re as regex
import time
import math

# Dynamic programming

def main(file: str) -> int:
    with open(file) as f:
        liste : list[str] = f.read().splitlines()
        times = regex.findall(r"\d+", liste[0])
        times = int("".join(times))
        distances = regex.findall(r"\d+", liste[1])
        distances = int("".join(distances))

        #(times-second_time)*times - distance = 0
        # times² - second_time*times - disntace = 0
        
        first_x = (-times -  math.sqrt(times ** 2 - 4 * (-1) * -distances)) // (2 * (-1))
        second_x = (-times +  math.sqrt(times ** 2 - 4 * (-1) * -distances)) // (2 * (-1))
        
        return int(first_x - second_x)

class TestStringMethods(unittest.TestCase):

    #def testtest(self):
    #    print("Test result")
    #    self.assertEqual(main("test06.txt"), 71503)
    
    def testinput(self):
        print("Input result")
        self.assertEqual(main("input06.txt"), 42948149)

if __name__ == "__main__":

    unittest.main()
    