import unittest
import re as regex
import time

# Make a list of tuples with rocks and delete them when new sand lands ontop ??



def main(file: str) -> int:
    with open(file) as f:
        liste : list[str] = f.read().splitlines()
        result_sum = 0
        all_points = set()
        highest_y = 0 # To find ground
        for line in liste:
            coords = line.split(" -> ")
            prev = None
            for coord in coords:
                x, y = map(int,coord.split(","))
                current = (x,y)
                if y > highest_y:
                    highest_y = y
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
                prev = (x,y)

        ground = highest_y+2
        for i in range(1000):
            all_points.add((i,ground))

        drop_point = (500,0)
        filled_cave = False
        lifo = [drop_point]

        while not filled_cave:
            if len(lifo) == 0:
                break
            point = lifo[-1]
            down = (point[0], point[1]+1)
            downleft = (point[0]-1, point[1]+1)
            downright = (point[0]+1, point[1]+1)
            if down not in all_points:
                lifo.append(down)
                continue
            if downleft not in all_points:
                lifo.append(downleft)
                continue
            if downright not in all_points:
                lifo.append(downright)
                continue
            all_points.add(lifo.pop())
            result_sum += 1
            if len(all_points) == 0:
                filled_cave = True

        return result_sum
                

class TestStringMethods(unittest.TestCase):

    def testtest(self):
        self.assertEqual(main("test14.txt"), 93)

if __name__ == "__main__":


    start = time.time()
    print(main("input14.txt"))
    end = time.time()
    print(end - start)
    unittest.main()
    