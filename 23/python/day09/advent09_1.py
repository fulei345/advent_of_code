import unittest
import time

# Lister af differencer og find den næste med en lidt akavet metode men lad os da prøve

def main(file: str) -> int:
    with open(file) as f:
        liste : list[str] = f.read().splitlines()
        result = 0
        for line in liste:
            numbers = list(map(int, line.split()))
            last_numbers = [numbers[-1]]
            difference = 9999
            while difference != 0:
                new_numbers = []
                for i in range(len(numbers)-1):
                    new_numbers.append(numbers[i+1]-numbers[i])
                last_difference = new_numbers[-1]
                last_numbers.append(last_difference)
                difference = last_difference
                numbers = new_numbers
            
            new_numb = 0
            for i in range(len(last_numbers)-2, -1, -1):
                new_numb = last_numbers[i] + new_numb
            result += new_numb

        return result        

if __name__ == "__main__":
    
    start = time.time()
    result = main("test09.txt")
    end = time.time()
    assert result == 114, f"Expected 114 but got {result}"
    print(end - start)

    start = time.time()
    result = main("input09.txt")
    end = time.time()
    assert result == 1684566095, f"Expected 1684566095 but got {result}"
    print(end - start)
    