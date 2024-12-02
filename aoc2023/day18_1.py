import cmath
from queue import Queue

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

    def flood_fill(self, coor):
        counter = 0
        q = Queue()
        q.put(coor)

        while not q.empty():
            i, j = q.get()
            
            if self.map[i][j] == '.':
                self.map[i][j] = '-'
                counter += 1
            
            for oi, oj in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni = i + oi
                nj = j + oj
                try:   
                    if self.map[ni][nj] == '.':
                        self.map[ni][nj] = '-'
                        counter += 1
                        q.put((ni, nj))
                except IndexError:
                    pass


        return counter


    def count_inside(self):
        pass

    def solve(self):
        start = complex(0,0)
        self.chain = [start]
        dirs = ['L', 'R', 'U', 'D']
        offsets = [complex(-1,0), complex(1,0), complex(0,-1), complex(0,1)]
        cur = start
        
        tl, br = complex(0), complex(0) #borders
        
        for dir, steps, _ in self.plan:
            for i in range(1, steps+1):
                pnt = cur + offsets[dirs.index(dir)]*i
                self.chain.append(pnt)
            cur = pnt
            tl_real = min(tl.real, pnt.real)
            tl_imag = min(tl.imag, pnt.imag)
            br_real = max(br.real, pnt.real)
            br_imag = max(br.imag, pnt.imag)
            tl = complex(tl_real, tl_imag)
            br = complex(br_real, br_imag)

        

        W = int(br.real - tl.real + 1)
        H = int(br.imag - tl.imag + 1)
        print("---", tl, br, W, H)

        border = 1 # extra border

        self.map = [['.' for _ in range(W + 2*border)] for _ in range(H + 2*border)]

        self.print_grid(self.map)
        for pnt in self.chain:
            print(pnt)
            pnt = pnt - tl + border + border*1j
            print(pnt)
            self.map[int(pnt.imag)][int(pnt.real)] = '#'
        
        self.print_grid(self.map)


        print("---")
        self.print_grid(self.map)

        outside = self.flood_fill((0, 0))

        self.print_grid(self.map)

        self.answer = (W+2*border)*(H+2*border) - outside


if __name__ == '__main__':
    # test
    filename = "input/day18test.txt"
    solution = Solution(filename)
    solution.solve()
    print("Test: ", solution.answers)
    print("Test: ", solution.answer)
    assert solution.answer == 62
    
    # real solution
    filename = "input/day18.txt"
    solution = Solution(filename)
    solution.solve()
    print("Solution: ", solution.answers)
    print("Solution: ", solution.answer)