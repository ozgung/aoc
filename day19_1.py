from dataclasses import dataclass

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

    

    def process(self, part, wf):
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

    
    def solve(self):
        self.accepted = []
        self.rejected = []

        for part in self.parts:
            
            cur_nm = 'in'
            while cur_nm not in 'RA':
                cur_wf = self.workflows[cur_nm]
                cur_nm = self.process(part, cur_wf)

            if cur_nm == 'A':
                self.accepted.append(part)
            elif cur_nm == 'R':
                self.rejected.append(part)
            else:
                print("prob")

        self.answer = sum((p.x + p.m + p.a + p.s) for p in self.accepted)



if __name__ == '__main__':
    # test
    filename = "input/day19test.txt"
    solution = Solution(filename)
    solution.solve()
    print("Test: ", solution.answers)
    print("Test: ", solution.answer)
    assert solution.answer == 19114
    
    # real solution
    filename = "input/day19.txt"
    solution = Solution(filename)
    solution.solve()
    print("Solution: ", solution.answers)
    print("Solution: ", solution.answer)