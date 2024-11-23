import time

                            

def main(file: str) -> int:
    with open(file) as f:
        liste : list[str] = f.read().splitlines()

        inits = liste[0].split(",")

        total = 0
        for init in inits:
            total += calc_value(init)
    return total

def calc_value(init):
    current_value = 0
    for char in init:
        current_value += ord(char)
        current_value *= 17
        current_value = current_value % 256
    return current_value

if __name__ == "__main__":
    
    start = time.time()
    result = main("test15_1.txt")
    end = time.time()
    expected = 52
    assert result == expected, f"Expected {expected} but got {result}"
    print(end - start)

    start = time.time()
    result = main("test15.txt")
    end = time.time()
    expected = 1320
    assert result == expected, f"Expected {expected} but got {result}"
    print(end - start)

    start = time.time()
    result = main("input15.txt")
    end = time.time()
    expected = 507666
    assert result == expected, f"Expected {expected} but got {result}"
    print(end - start)
    