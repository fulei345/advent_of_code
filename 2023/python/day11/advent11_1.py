import unittest
import time

# Forstår ikke expansion af de andre rows og columns
# It is just doubling that single row or column
# Men bare brug manhatten distance på 488  * 488 + the inbetween rows and colums

def main(file: str) -> int:
    with open(file) as f:
        liste : list[str] = f.read().splitlines()

        rows = [True] * len(liste)
        columns = [True] * len(liste)

        galaxies = []
        for y, line in enumerate(liste):
            for x, char in enumerate(line):
                if char == "#":
                    rows[y] = False
                    columns[x] = False
                    galaxies.append((y,x))
        
        # When finding distance pop one and compare
        total_distance = 0
        while len(galaxies) > 0:
            current = galaxies.pop()

            for galaxy in galaxies:
                distance = abs(current[0]-galaxy[0]) + abs(current[1]-galaxy[1])
                mini = min(current[0],galaxy[0])
                maxi = max(current[0],galaxy[0])
                for i in range(mini+1, maxi):
                    if rows[i]:
                        distance += 1
                mini = min(current[1],galaxy[1])
                maxi = max(current[1],galaxy[1])
                for i in range(mini+1, maxi):
                    if columns[i]:
                        distance += 1
                total_distance += distance
        return total_distance

if __name__ == "__main__":
    
    start = time.time()
    result = main("test10.txt")
    end = time.time()
    assert result == 374, f"Expected 374 but got {result}"
    print(end - start)

    start = time.time()
    result = main("input10.txt")
    end = time.time()
    #assert result == 6717, f"Expected 6717 but got {result}"
    print(result)
    print(end - start)
    