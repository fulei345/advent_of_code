import unittest
import re as regex
import time

# Dynamic programming

def main(file: str) -> int:
    with open(file) as f:
        liste : list[str] = f.read().splitlines()
        times = list(map(int, regex.findall(r"\d+", liste[0])))
        distances = list(map(int, regex.findall(r"\d+", liste[1])))
        
        result = []
        for i in range(times):
            # This is a race
            result.append(0)
            for x in range(times[i]//2):
                distance = x*(times[i]-x)
                if distance > distances[i]:
                    result[i] += 1
            
            if times[i] % 2 == 1:
                distance = (times[i]//2)+1*(times[i]//2)-11
                if distance > distances[i]:
                    result[i] += 1
        result_sum = 1
        for res in result:
            result_sum *= res
        return result_sum

class TestStringMethods(unittest.TestCase):

    def testtest(self):
        self.assertEqual(main("test06.txt"), 288)

if __name__ == "__main__":


    start = time.time()
    #print(main("input06.txt"))
    end = time.time()
    print(end - start)
    unittest.main()
    