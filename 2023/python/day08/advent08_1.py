import unittest
import time

# Bruteforce metoden er at gå igennem hele node systemet
# Eller save min vej til hver node som en 
# Først lav tuples af de strings (source, left, right)

class Node:
    def __init__(self, source: str):
        self.left: Node = None
        self.right: Node = None
        self.source: str = source

    #def set_nodes(self, left: Node, right: Node):
    #    self.left = left
    #    self.right = right
    

def main(file: str) -> int:
    with open(file) as f:
        liste : list[str] = f.read().splitlines()
        commands = liste[0]
        tuple_list = []
        name_list = []
        for i in range(2,len(liste)):
            first, second = liste[i].split(" = ")
            left, right = second.split(", ")
            left = left[1] + left[2] + left[3]
            right = right[0] + right[1] + right[2]
            tuple_list.append((first,left,right))
            name_list.append(first)
        tuple_list.sort()
        name_list.sort()
        temp = []
        for tup in tuple_list:
            left_index = name_list.index(tup[1])
            right_index = name_list.index(tup[2])
            temp.append((tup[0], left_index, right_index))
        tuple_list = temp

        
        current = tuple_list[0]
        result = 0
        command_counter = 0
        while current[0] != "ZZZ":
            if commands[command_counter] == "L":
                current = tuple_list[current[1]]
            elif commands[command_counter] == "R":
                current = tuple_list[current[2]]
            if command_counter == len(commands)-1:
                command_counter = 0
            else:
                command_counter += 1
            result += 1
        return result


class TestStringMethods(unittest.TestCase):

    def testtest(self):
        self.assertEqual(main("test08.txt"), 2)

    def testtest2(self):
        self.assertEqual(main("test08_2.txt"), 6)

if __name__ == "__main__":


    start = time.time()
    print(main("input08.txt"))
    end = time.time()
    print(end - start)
    unittest.main()
    