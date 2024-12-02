from itertools import cycle
from re import search
from functools import reduce

class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

class Solution:
    def __init__(self, filename):
        self.nodes = {}
        self.answer = None
        self.answers = []
        self.starts = set()
        self.ends = set()
        self.parse_input(filename)

    def parse_input(self, filename):
        with open(filename, 'r') as file:
            self.directions = list(file.readline().strip())
            _ = file.readline()
            
            pattern = r"(\w+) = \((\w+), (\w+)\)"
            for line in file:
                matched = search(pattern, line)
                if matched:
                    name, left, right = matched.group(1).strip(), matched.group(2).strip(), matched.group(3).strip()
                    self.nodes[name] = Node(name, left, right)
                    if name[2] == 'A':
                        self.starts.add(name)
                    if name[2] == 'Z':
                        self.ends.add(name)

    def solve_cycles(self):
        nums = [x[0] for x in self.cycles]
        
        def gcd(a, b):
            l = max(a, b)
            s = min(a, b)
            if l%s == 0:
                return s
            else:
                return gcd(s, l%s)

        def lcm(a, b):
            return a * b / gcd(a, b)

        # find least common multiplier
        self.answer = int(reduce(lcm, nums))


    def solve(self):
        self.cycles = []
        
        for start in self.starts:
            begin, cyc = -1, -1
            cur = start
            for i, dir in enumerate(cycle(self.directions)):    
                if dir == 'L':
                    cur = self.nodes[cur].left
                elif dir == 'R':
                    cur = self.nodes[cur].right

                if cur in self.ends:
                    if begin < 0:
                        begin = i + 1
                    else:
                        cyc = i + 1 - begin
                        self.cycles.append((begin, cyc))
                        break

        print(self.cycles)
        self.solve_cycles()


if __name__ == '__main__':
    #test
    filename = "input/day8test3.txt"
    solution = Solution(filename)
    solution.solve()
    print("Test: ", solution.answers)
    print("Test: ", solution.answer)
    assert solution.answer == 6

    # real solution
    filename = "input/day8.txt"
    solution = Solution(filename)
    solution.solve()
    print("Solution: ", solution.answers)
    print("Solution: ", solution.answer)