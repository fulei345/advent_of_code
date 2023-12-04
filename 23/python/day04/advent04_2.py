import unittest
import re as regex

# First count the winnings on each card then loop over them again

def main(file: str) -> int:
    with open(file) as f:
        liste : list[str] = f.read().splitlines()
        
        all_cards = []
        winnings_on_cards = []
        for y, line in enumerate(liste):
            numbers = line.split(":")[1]
            winning, card = numbers.split("|")
            winning = regex.findall(r"\d+", winning)
            card = regex.findall(r"\d+", card)

            points = 0
            for num in winning:
                if num in card:
                    points += 1
            
            winnings_on_cards.append(points)
            all_cards.append(1)
        result_sum = 0

        for index, num_card in enumerate(all_cards):
            for i in range(index+1, index+winnings_on_cards[index]+1):
                all_cards[i] += num_card
            result_sum += num_card
            

        return result_sum    
        

class TestStringMethods(unittest.TestCase):

    def testtest(self):
        self.assertEqual(main("test04.txt"), 30)

if __name__ == "__main__":
    print(main("input04.txt"))
    unittest.main()
    