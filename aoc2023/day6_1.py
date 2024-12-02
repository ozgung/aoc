import re
from collections import OrderedDict
from functools import reduce
from operator import mul

class Solution():

    def __init__(self, filename):
        self.parse_input(filename)
        self.answer = None
        self.answers = []

    def parse_input(self, filename):
        
        with open(filename) as file:
            self.times = map(int, file.readline().split(':')[1].split())
            self.distances = map(int, file.readline().split(':')[1].split())

    def compute_wins(self, time, record_distance):
        wins = []
        for t in range(1, time):
            dist = (time - t) * t
            if dist > record_distance:
                wins.append(dist)

        return len(wins)

    def solve(self):
        for el in zip(self.times, self.distances):

            self.answers.append(self.compute_wins(*el))

        self.answer = reduce(mul, self.answers)

if __name__ == '__main__':
    # test
    filename = "input/day6test.txt"
    solution = Solution(filename)
    solution.solve()
    print("Test: ", solution.answer)
    assert solution.answer == 288
    
    # real solution
    filename = "input/day6.txt"
    solution = Solution(filename)
    solution.solve()
    print("Solution: ", solution.answer)