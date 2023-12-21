import cmath
from queue import Queue
import math

class Solution:
    def __init__(self, filename):
        self.answer = None
        self.answers = []
        self.parse_input(filename)

    def parse_input(self, filename):
        self.plan = []
        with open(filename, 'r') as file:
            for line in file:
                move = line.strip().split()
                move[1] = int(move[1])
                move[2] = move[2][2:-1]
                self.plan.append(move)
    
    def print_grid(self, grid):
        for row in grid:
            print(''.join(row))

    def decode_hex(self, hex):
        steps = int(hex[:-1], 16)
        dir = ['R', 'D', 'L', 'U'][int(hex[-1])]
        return dir, steps

    def solve(self):
        def det(p1, p2):
            return p1.real*p2.imag - p2.real*p1.imag


        start = complex(0,0)
        self.chain = [start]
        dirs = ['L', 'R', 'U', 'D']
        offsets = [complex(-1,0), complex(1,0), complex(0,-1), complex(0,1)]

        pnt = start
        border = 0

        for _, _, hex in self.plan:
            dir, steps = self.decode_hex(hex)
            
            pnt = pnt + offsets[dirs.index(dir)]*steps
            self.chain.append(pnt)
            border += steps

        
        # shoelace formula
        total = 0
        for i in range(0, len(self.chain)-1):
            d = det(self.chain[i], self.chain[i+1])
            total += d/2
        
        A = int(total)


        self.answer = int(A + border/2 + 1)


if __name__ == '__main__':
    # test
    filename = "input/day18test.txt"
    solution = Solution(filename)
    solution.solve()
    print("Test: ", solution.answers)
    print("Test: ", solution.answer)
    print(952408144115 - solution.answer)
    assert solution.answer == 952408144115
    
    # real solution
    filename = "input/day18.txt"
    solution = Solution(filename)
    solution.solve()
    print("Solution: ", solution.answers)
    print("Solution: ", solution.answer)