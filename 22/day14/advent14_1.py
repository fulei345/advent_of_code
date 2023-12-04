import unittest
import re as regex
import time

# Make a list of tuples with rocks and delete them when new sand lands ontop ??



def main(file: str) -> int:
    with open(file) as f:
        liste : list[str] = f.read().splitlines()
        result_sum = 0
        all_points = set()
        for line in liste:
            coords = line.split(" -> ")
            prev = None
            for coord in coords:
                x, y = coord.split(",")
                current = (int(x),int(y))
                all_points.add(current)

                if prev:
                    if prev[0] != current[0]:
                        smallest = min(prev[0], current[0])
                        biggest = max(prev[0], current[0])
                        for i in range(smallest, biggest+1):
                            all_points.add((i,prev[1]))
                    else:
                        smallest = min(prev[1], current[1])
                        biggest = max(prev[1], current[1])
                        for i in range(smallest, biggest+1):
                            all_points.add((prev[0],i))
                prev = (int(x),int(y))

        drop_point = (500,0)
        reach_abyss = False
        current = drop_point

        while not reach_abyss:
            down_points = [x for x in all_points if x[0] == current[0]]
            reach_abyss = len(down_points) == 0 # Check if we reached abyss
            if reach_abyss:
                break
            closest_distance = 1000
            for point in down_points:
                if point[1]-current[1] >= 0 and point[1]-current[1] < closest_distance:
                    closest_distance = point[1]-current[1]
            current = (current[0], closest_distance+current[1]-1)
            # We have reached the tallest point down
            if (current[0]-1,current[1]+1) in all_points:
                if (current[0]+1,current[1]+1) in all_points:
                    all_points.add(current)
                    result_sum += 1
                    current = drop_point
                else:
                    current = (current[0]+1,current[1]+1)
                    continue
            else:
                current = (current[0]-1,current[1]+1)
                continue
            

        return result_sum
                

class TestStringMethods(unittest.TestCase):

    def testtest(self):
        self.assertEqual(main("test14.txt"), 24)

if __name__ == "__main__":


    start = time.time()
    print(main("input14.txt"))
    end = time.time()
    print(end - start)
    unittest.main()
    