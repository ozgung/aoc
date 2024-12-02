import re
from collections import OrderedDict

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
        for seed in self.seeds:
            val = seed
            for i, ranges in enumerate(self.maps.values()):
                print(list(self.maps.keys())[i][0], val)
                val = self.map_range(val, ranges)
                

            self.answers.append(val) 


    def map_range(self, val, ranges):
        for rn in ranges:
            if val >= rn[1] and val < rn[1] + rn[2]:
                return rn[0] + (val - rn[1])

        return val
    

if __name__ == '__main__':
    filename = "input/day5.txt"
    solution = Solution(filename)
    solution.solve()
    print(solution.answers)
    print(min(solution.answers))