import re
from collections import OrderedDict
from functools import reduce

class Solution():

    answers = []

    def __init__(self, filename):
        self.maps = OrderedDict()
        self.parse_input(filename)

    def parse_input(self, filename):

        with open(filename) as file:
            seeds_line = file.readline()
            pattern = r'(\w+)-to-(\w+)'

            self.seeds = list(map(int, seeds_line.split(':')[1].split()))

            current_key = None
            for line  in file:
                if line == "\n":
                    current_key = None
                    continue

                matches = re.search(pattern, line)
                if matches:
                    from_to = (matches[1], matches[2])
                    self.maps[from_to] = []
                    current_key = from_to
                else:
                    range = tuple(map(int, line.split()))
                    self.maps[current_key].append(range)

    def solve(self):
        loc = -1 # search by 1000 increments first

        while True:
            loc += 1 # 1000 # search by 1000 increments first then refine
            print("try ", loc)

            val = loc
            ranges = list(self.maps.values())

            for i in range(len(ranges) - 1, -1, -1):
                val = self.map_back_range(val, ranges[i])
                
            if self.check_seed_in_range(val):
                print("Found", loc)
                self.answers = [loc]
                return

    def check_seed_in_range(self, seed):
        for i in range(len(self.seeds)//2):
            if seed >= self.seeds[2*i] and seed < self.seeds[2*i] + self.seeds[2*i+1]:
                return True
        return False                
    
    def map_back_range(self, val, ranges):
        for rn in ranges:
            if val >= rn[0] and val < rn[0] + rn[2]:
                return rn[1] + (val - rn[0])

        return val


if __name__ == '__main__':
    filename = "input/day5.txt"
    solution = Solution(filename)
    solution.solve()
    print(solution.answers)
