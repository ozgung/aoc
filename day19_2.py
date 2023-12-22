from dataclasses import dataclass
from copy import deepcopy

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

    

    def soft_process(self, part, wf, rating='s'):
        def check_cond(c):
            prop = c[0]
            op = c[1]
            val = int(c[2:])
            
            if op == '<':
                return getattr(part, prop) < val
            elif op == '>':
                return getattr(part, prop) > val
            else:
                assert False
        
        for i, condition in enumerate(wf):
            if i < len(wf)-1:
                a, b = condition.split(':')
                if check_cond(a):
                    return b
            else:
                # last cond
                return condition

    
    def process(self, in_ranges, name):
        def filter(c):
            prop = c[0]
            op = c[1]
            val = int(c[2:])
            
            if op == '<':
                in_ranges[prop][1] = val - 1
            elif op == '>':
                in_ranges[prop][0] = val - 1
            else:
                assert False

        if name == 'R':
            self.rejected.append(deepcopy(in_ranges))
            return
        if name == 'A':
            self.accepted.append(deepcopy(in_ranges))
            return
        
        wf = self.workflows[name]

        for i, condition in enumerate(wf):
            if i < len(wf)-1:
                c, target = condition.split(':')
                
                filter(c)
                rating = c[0]
                if in_ranges[rating][0] <= in_ranges[rating][1]:
                    
                    self.process(deepcopy(in_ranges), target)
                else:
                    continue
            else:
                target = condition
                self.process(deepcopy(in_ranges), target) 
                

    def solve(self):
        MIN, MAX = 1, 4000

        acceptable = {'x': [1, 4000],'m': [1, 4000],'a': [1, 4000],'s' : [1, 4000]}

        self.accepted = []
        self.rejected = []

        self.process(acceptable, 'in')


        for d in self.accepted:
            cnts = 1
            for r in ['x','m','a','s']:
                n = d[r][1]-d[r][0] + 1
                cnts *= max(n, 0)
            self.answers.append(cnts)
        print('R', self.answers)

        for d in self.rejected:
            cnts = 1
            for r in ['x','m','a','s']:
                n = d[r][1]-d[r][0] + 1
                cnts *= max(n, 0)
            self.answers.append(cnts)

        print(4000**4)
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