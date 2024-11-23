import unittest

dictionary : dict = {"one": "1","two": "2",
                     "three": "3","four": "4",
                     "five": "5","six": "6",
                     "seven": "7", "eight": "8",
                     "nine": "9"}

def main(file: str) -> int:
    with open(file) as f:
        liste : list[str] = f.read().splitlines()
        result_sum : int = 0
        for line in liste:
            first : str = ""
            first_index : int = 99
            last : str = ""
            last_index : int = -1
            for index, char in enumerate(line):
                if char.isdigit():
                    if index < first_index:
                        first : str = char
                        first_index : int = index
                    if index > last_index:
                        last : str = char
                        last_index : int = index
            result_sum += int(first + last)
        return result_sum
    

class TestStringMethods(unittest.TestCase):

    def testtest(self):
        self.assertEqual(main("test01.txt"), 142)

    def testinput(self):
        self.assertEqual(main("input01.txt"), 56397)

if __name__ == "__main__":
    main("test01.txt")
    print(main("input01.txt"))
    unittest.main()