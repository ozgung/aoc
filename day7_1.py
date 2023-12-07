from collections import Counter
from functools import cmp_to_key

class Solution():

    cards = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}

    def __init__(self, filename):
        self.parse_input(filename)
        self.answer = None
        self.answers = []

    def parse_input(self, filename):
        self.hands = []
        self.bids = []
        with open(filename) as file:
            for line in file:
                ln = line.split()
                self.hands.append(ln[0])
                self.bids.append(int(ln[1]))

    def find_type(self, hand):
        counts = sorted(Counter(hand).values(), reverse=True)

        if counts[0] == 5:
            return 7 # five of a kind
        elif counts[0] == 4:
            return 6 # four of a kind
        elif counts[0] == 3 and counts[1] == 2:
            return 5 # full house
        elif counts[0] == 3:
            return 4 # three of a kind
        elif counts[0] == 2 and counts[1] == 2:
            return 3 # two pair
        elif counts[0] == 2:
            return 2 # one pair
        else:
            assert len(counts) == 5
            return 1 # high card
        
    
    def solve(self):
        self.types = []
        
        for hand in self.hands:
            self.types.append(self.find_type(hand))

        
        def comparator(item1, item2):
            if item1[1] > item2[1]:
                return 1
            elif item1[1] < item2[1]:
                return -1
            else:
                for i in range(len(item1[2])):
                    if item1[2][i] == item2[2][i]:
                        continue
                    val1, val2 = self.cards[item1[2][i]], self.cards[item2[2][i]]
                    if val1 > val2:
                        return 1
                    elif val1 < val2:
                        return -1
                return 0

        zipped = list(zip(self.bids, self.types, self.hands))
        ordered = list(sorted(zipped, key=cmp_to_key(comparator)))

        for i in range(len(ordered)):
            rank = i + 1
            bid = ordered[i][0]
            self.answers.append(rank * bid)

        self.answer =  sum(self.answers)


if __name__ == '__main__':
    # test
    filename = "input/day7test.txt"
    solution = Solution(filename)
    solution.solve()
    print("Test: ", solution.answers)
    print("Test: ", solution.answer)
    assert solution.answer == 6440
    
    # real solution
    filename = "input/day7.txt"
    solution = Solution(filename)
    solution.solve()
    print("Solution: ", solution.answer)