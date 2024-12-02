import re
from collections import OrderedDict
from functools import reduce
from operator import mul
import math

class Solution():

    def __init__(self, filename):
        self.parse_input(filename)
        self.answer = None
        self.answers = []

    def parse_input(self, filename):
        with open(filename) as file:
            self.times = file.readline().split(':')[1].split()
            self.distances = file.readline().split(':')[1].split()

            self.times = [int("".join(self.times))]
            self.distances = [int("".join(self.distances))]

    def compute_wins_analytic(self, time, record_distance):
        def discriminant(a, b, c):
            return b**2 - 4*a*c

        a, b, c = 1.0, float(time), float(record_distance)
        disc = discriminant(a, b, c)
        
        if disc > 0:
            sq_disc = math.sqrt(disc)
            root1 = (-b + sq_disc) / 2 * a
            root2 = (-b - sq_disc) / 2 * a
            start = math.ceil(min(-root1, -root2))
            end = math.floor(max(-root1, -root2))
            return end - start + 1
        
    def solve(self):
        for el in zip(self.times, self.distances):

            self.answer = self.compute_wins_analytic(*el)

if __name__ == '__main__':
    # test
    filename = "input/day6test.txt"
    solution = Solution(filename)
    solution.solve()
    print("Test: ", solution.answer)
    assert solution.answer == 71503
    
    # real solution
    filename = "input/day6.txt"
    solution = Solution(filename)
    solution.solve()
    print("Solution: ", solution.answer)