from dataclasses import dataclass
from copy import deepcopy
from itertools import product

@dataclass
class Part:
    x: int
    m: int
    a: int
    s: int

class Solution:
    def __init__(self, filename):
        self.answer = None
        self.answers = []
        self.parse_input(filename)

    def parse_input(self, filename):
        with open(filename, 'r') as file:
            self.workflows = {}
            for line in file:
                if line == '\n':
                    break
                # px{a<2006:qkq,m>2090:A,rfg}
                nm, rest = line.strip().split('{')
                commands = rest[:-1].split(',')
                self.workflows[nm] = commands

            self.parts = []
            for line in file:
                params = line.strip()[1:-1].split(',')
                l = [p.split('=')[1] for p in params]
                l = map(int, l)
                self.parts.append(Part(*l))
    
    def process(self, in_ranges, name):
        def filter(c, ranges):
            prop = c[0]
            op = c[1]
            val = int(c[2:])
            others = deepcopy(ranges)
            if op == '<':
                ranges[prop][1] = val - 1
                others[prop][0] = val
            elif op == '>':
                ranges[prop][0] = val + 1
                others[prop][1] = val
            else:
                assert False
            return others
        
        
        print(name)
        if name == 'R':
            self.rejected.append(deepcopy(in_ranges))
            return
        if name == 'A':
            self.accepted.append(deepcopy(in_ranges))
            return
        
        wf = self.workflows[name]


        ranges = deepcopy(in_ranges)
        for i, condition in enumerate(wf):
            if i < len(wf)-1:
                c, target = condition.split(':')
                others = filter(c, ranges)
                
                rating = c[0]
                if ranges[rating][0] <= ranges[rating][1]:
                    self.process(ranges, target)
                ranges = others
            else:
                target = condition
                self.process(ranges, target) 
                

    def solve(self):
        MIN, MAX = 1, 4000

        acceptable = {x: [MIN, MAX] for x in 'xmas'}

        self.accepted = []
        self.rejected = []

        self.process(acceptable, 'in')

        print(self.accepted)

        for d in self.accepted:
            cnts = 1
            for r in ['x','m','a','s']:
                n = d[r][1]-d[r][0] + 1
                cnts *= max(n, 0)
            self.answers.append(cnts)

        self.answer =  sum(self.answers)            


if __name__ == '__main__':
    # test
    filename = "input/day19test.txt"
    solution = Solution(filename)
    solution.solve()
    print("Test: ", solution.answers)
    print("Test: ", solution.answer)
    assert solution.answer == 167409079868000
    
    # real solution
    filename = "input/day19.txt"
    solution = Solution(filename)
    solution.solve()
    print("Solution: ", solution.answers)
    print("Solution: ", solution.answer)