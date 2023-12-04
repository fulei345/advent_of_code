import unittest
import re as regex

class Number:
    def __init__(self, num: int, y_axis: int, x_start: int, x_end: int):
        self.num = num
        self.y_axis = y_axis
        self.x_start = x_start
        self.x_end = x_end
        self.countedfor = False

def main(file: str) -> int:
    with open(file) as f:
        liste : list[str] = f.read().splitlines()
        
        number_list : Number = []
        symbol_list = []
        for y, line in enumerate(liste):
            for match in regex.finditer(r"\d+", line):
                number_list.append(Number(int(match.group()), y, match.span()[0], match.span()[1]))
            for x, char in enumerate(line):
                if not char.isdigit() and not char == ".":
                    symbol_list.append((y,x))

        result_sum = 0
        
        for symb in symbol_list:
            y = symb[0]
            x = symb[1]
            symb_set = [(y+1,x-1),(y+1,x),(y+1,x+1),(y,x+1),(y-1,x+1),(y-1,x),(y-1,x-1),(y,x-1)]
            found_numbers = []
            for number in number_list:
                numb_set = []
                for i in range(number.x_start, number.x_end):
                    numb_set.append((number.y_axis,i))
                for numb in numb_set:
                    if not number.countedfor:
                        if numb in symb_set:
                            found_numbers.append(number)
                            number.countedfor = True
                            continue
            if len(found_numbers) == 2:
                result_sum += found_numbers[0].num * found_numbers[1].num
        return result_sum    
        

class TestStringMethods(unittest.TestCase):

    def testtest(self):
        self.assertEqual(main("test03.txt"), 413)

if __name__ == "__main__":
    print(main("input03.txt"))
    #unittest.main()
    