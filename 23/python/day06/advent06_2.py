import unittest
import re as regex
import time

# Dynamic programming

def main(file: str) -> int:
    with open(file) as f:
        liste : list[str] = f.read().splitlines()
        times = regex.findall(r"\d+", liste[0])
        distances = regex.findall(r"\d+", liste[1])
        temp = ""
        for time in times:
            temp = temp + time
        times = [int(temp)]
        temp = ""
        for distance in distances:
            temp = temp + distance
        distances = [int(temp)]
        
        result = []
        for i in range(len(times)):
            # This is a race
            result.append(0)
            for x in range(times[i]):
                distance = x*(times[i]-x)
                if distance > distances[i]:
                    result[i] += 1
                else:
                    if result[i] > 1:
                        break

        result_sum = 1
        for res in result:
            result_sum *= res
        return result_sum

class TestStringMethods(unittest.TestCase):

    def testtest(self):
        self.assertEqual(main("test06.txt"), 71503)

if __name__ == "__main__":


    start = time.time()
    print(main("input06.txt"))
    end = time.time()
    print(end - start)
    unittest.main()
    