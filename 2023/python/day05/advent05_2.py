import re as regex
import time

# The first row is a index and a range -1
# All the others lines is the same 

def main(file: str) -> int:
    with open(file) as f:
        liste : list[str] = f.read().splitlines()
        seeds = list(map(int, regex.findall(r"\d+", liste[0]))) # Find all ranges for seeds
        seeds_ranges = []
        for i in range(0, len(seeds), 2):
            seeds_ranges.append((seeds[i], seeds[i]+seeds[i]-1))

        map = []
        liste = liste[1:]
        for y, line in enumerate(liste):
            name = line.find("map")
            if name != -1:
                # Do the mapping of new seeds
                if len(map) > 0:
                    map.sort()
                    seeds_ranges.sort()
                    seeds_ranges = map_all_seeds(map, seeds_ranges)
                map = []
            else:
                numbers = list(map(int, regex.findall(r"\d+", line)))
                if len(numbers) == 0:
                    continue
                left_s = numbers[0]
                right_s = numbers[0]+numbers[2]-1
                left_d = numbers[1]
                right_d = numbers[1]+numbers[2]-1
                map.append(((left_s, right_s), (left_d, right_d)))
        seeds.sort()
        return seeds[0][0]

def map_all_seeds(map, seeds):
    map_c = 0
    seeds_c = 0
    new_seeds = []
    new = overlap(map[map_c], seeds[seeds_c])


# Returns new ranges
def overlap(map_line, seed):
    result = []
    for numb in numbers:
        number_appended = False
        for line in func:
            source_start = line[1][0]
            source_end = line[1][1]
            if source_start <= numb <= source_end:
                result.append(line[0][0] + (numb-source_start))
                number_appended = True
        if not number_appended:
            result.append(numb)
    return result

if __name__ == "__main__":
    
    start = time.time()
    result = main("test05.txt")
    end = time.time()
    assert result == 46, f"Expected 46 but got {result}"
    print(end - start)

    start = time.time()
    result = main("input05.txt")
    end = time.time()
    assert result == 69323688, f"Expected 69323688 but got {result}"
    print(end - start)

    