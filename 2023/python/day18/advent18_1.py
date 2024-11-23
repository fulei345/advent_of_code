import time
# Would like to know how big my 

def main(file: str) -> int:
    maps: list[list[int]] = None
    with open(file) as f:
        liste : list[str] = f.read().splitlines()
        for i in range(len(liste)):
            liste[i] = list(map(int, [*liste[i]]))
        maps = liste
    
    result = a_star(maps, (0,0), (len(maps)-1, len(maps[0])-1))
    return result

if __name__ == "__main__":
    
    start = time.time()
    result = main("test17.txt")
    end = time.time()
    expected = 102
    assert result == expected, f"Expected {expected} but got {result}"
    print(end - start)

    start = time.time()
    result = main("input17.txt")
    end = time.time()
    expected = 7798
    assert result == expected, f"Expected {expected} but got {result}"
    print(end - start)

    #https://old.reddit.com/r/adventofcode/comments/18luw6q/2023_day_17_a_longform_tutorial_on_day_17
