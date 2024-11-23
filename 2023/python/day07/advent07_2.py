import unittest
import time
from functools import cmp_to_key
import datetime

# Determine type derefter lav en sortering af dem baseret på det
# Types 0-6
# Card list 0-12


"""32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

class camel_hand:
    def __init__(self, hand: list, type: int, bet: int):
        self.hand: list = hand
        self.type: int = type
        self.bet: int = bet

    def __lt__(self, other):
        if self.type < other.type:
            return True
        elif self.type > other.type:
            return False
        else:
            for i in range(len(self.hand)):
                if self.hand[i] == other.hand[i]:
                    continue
                return self.hand[i] < other.hand[i]
"""
def compare_camel(left: camel_hand, right: camel_hand):
    if left.type > right.type:
        return 1
    elif left.type < right.type:
        return -1
    else:
        return compare_nums(left.hand, right.hand)

def compare_nums(left: list, right: list):
    for i in range(len(left)):
        if left[i] == right[i]:
            continue
        elif left[i] > right[i]:
            return 1
        else:
            return -1
"""

def find_type(hand: list):
    types = [0]*13
    highest = -1
    for c in hand:
        types[c] += 1
        if c != 0 and types[c] > highest:
            highest = types[c]
            index = c
    
    if highest == -1:
        return 6
    jokers = types[0]
    highest += jokers
    types[index] += jokers
    types[0] = 0

    twos = 0
    for index,num in enumerate(types):
        if index != 0 and num == 2:
            twos += 1

    if highest == 5:
        return 6
    elif highest == 4:
        return 5
    elif highest == 3:
        if twos == 1:
            return 4
        else:
            return 3
    elif highest == 2:
        if twos == 2:
            return 2
        else:
            return 1
    else:
        return 0

def main(file: str) -> int:
    with open(file) as f:
        liste : list[str] = f.read().splitlines()
        camels = []
        for line in liste:
            # This is a race
            hand, bet = line.split()
            hand_liste = []
            for c in hand:
                if c == "A":
                    hand_liste.append(12)
                elif c == "K":
                    hand_liste.append(11)
                elif c == "Q":
                    hand_liste.append(10)
                elif c == "J":
                    hand_liste.append(0)
                elif c == "T":
                    hand_liste.append(9)
                else:
                    hand_liste.append(int(c)-1)
            
            type = find_type(hand_liste)
            camels.append(camel_hand(hand_liste, type, int(bet)))
        #camels = sorted(camels, key=cmp_to_key(compare_camel))
        camels.sort()
        result = 0
        for index, camel in enumerate(camels):
            result += (index +1) * camel.bet
        
        return result

class TestStringMethods(unittest.TestCase):

    def testtest(self):
        self.assertEqual(main("test07.txt"), 6839)

if __name__ == "__main__":


    start = time.time()
    print(main("input07.txt"))
    end = time.time()
    print(str(datetime.timedelta(seconds=end-start)))
    #unittest.main()
    