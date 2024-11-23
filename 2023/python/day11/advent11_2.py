import unittest
import time

# Forstår ikke expansion af de andre rows og columns
# It is just doubling that single row or column
# Men bare brug manhatten distance på 488  * 488 + the inbetween rows and colums

def main(file: str, expansion: int) -> int:
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
                        distance += expansion
                mini = min(current[1],galaxy[1])
                maxi = max(current[1],galaxy[1])
                for i in range(mini+1, maxi):
                    if columns[i]:
                        distance += expansion
                total_distance += distance
        return total_distance

if __name__ == "__main__":
    
    start = time.time()
    result = main("test10.txt", 9)
    end = time.time()
    assert result == 1030, f"Expected 1030 but got {result}"
    print(end - start)

    start = time.time()
    result = main("test10.txt", 99)
    end = time.time()
    assert result == 8410, f"Expected 8410 but got {result}"
    print(end - start)

    start = time.time()
    result = main("input10.txt",999999)
    end = time.time()
    assert result == 791134099634, f"Expected 791134099634 but got {result}"
    print(result)
    print(end - start)
