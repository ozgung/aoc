from collections import Counter

class Solution:
    def __init__(self, filename):
        self.answer = None
        self.answers = []
        self.looplength = -1
        self.moves = []
        self.insides = 0
        self.parse_input(filename)

    def parse_input(self, filename):
        self.grid = []
        with open(filename, 'r') as file:
            for i, line in enumerate(file):
                s = line.find('S')
                if s >= 0:
                    self.start = [i, s]
                self.grid.append(list(line.strip()))
    
    outdirs = ['u', 'd', 'l', 'r']
    indirs  = ['d', 'u', 'r', 'l']
    tiles = {'|': ('u', 'd'),
             '-': ('l', 'r'),
             'L': ('u', 'r'),
             'J': ('u', 'l'),
             '7': ('l', 'd'),
             'F': ('r', 'd')}

    def move(self):
        dir = self.outdir
        p = self.cur.copy()
        if dir == 'u':
            indir = 'd'
            p[0] -= 1
        elif dir == 'd':
            p[0] += 1
            indir = 'u'
        elif dir == 'l':
            p[1] -= 1
            indir = 'r'
        elif dir == 'r':
            p[1] += 1
            indir = 'l'
        
        if p[0] < 0 or p[1] < 0 or p[0] >= len(self.grid) or p[1] >= len(self.grid[0]):
            return False
        
        next = self.grid[p[0]][p[1]]
        if next == '.':
            return False
        
        # move and update
        if next == 'S':
            self.cur = p
            self.indir = indir
            self.outdir = None
            return True
        
        nexttile = self.tiles[next]
        if indir not in nexttile:
            return False

        if indir == nexttile[0]:
            self.outdir = nexttile[1]
        elif indir == nexttile[1]:
            self.outdir = nexttile[0]
        else:
            return False
        self.cur = p
        self.indir = indir
        return True

    CCW = {('l', 'u'), 
           ('u', 'r'),
           ('r', 'd'),
           ('d', 'l')}
    CW =  {('l', 'd'), 
           ('u', 'l'),
           ('r', 'u'),
           ('d', 'r')}

    def add_bend(self):
        '''+1: CW, -1: CCW'''
        mv = (self.indir, self.outdir)
        if mv in self.CCW:
            self.bend -= 1
        elif mv in self.CW:
            self.bend += 1

    def find_loop(self):
        '''First Part'''
        # find loop
        MAX_STEPS = 100000
        self.counter = Counter()
        for startdir in self.outdirs:
            self.outdir = startdir
            self.cur = self.start
            steps = 0
            self.bend = 0
            self.path = []
            while self.move() and steps < MAX_STEPS:
                steps += 1
                char = self.grid[self.cur[0]][self.cur[1]]
                if char == 'S':
                    self.outdir = startdir
                    self.looplength = steps
                    self.path.append((self.indir, self.outdir, self.cur.copy()))
                    self.add_bend()
                    return
                self.path.append((self.indir, self.outdir, self.cur.copy()))
                self.add_bend()

    def print_grid(self):
        for row in self.grid:
            print(''.join(row))


    def charat(self, p):
        if p[0] < 0 or p[1] < 0 or p[0] >= len(self.grid) or p[1] >= len(self.grid[0]):
            return None
        else:
            return self.grid[p[0]][p[1]]
    def setcharat(self, p, c):
        if p[0] < 0 or p[1] < 0 or p[0] >= len(self.grid) or p[1] >= len(self.grid[0]):
            return
        else:
            self.grid[p[0]][p[1]] = c

    def flood_fill(self, start, mark='.', replace='I'):
        if self.charat(start) == mark:
            self.setcharat(start, replace)
                
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if not (i == 0 and j == 0):
                        testpos = [start[0]+i, start[1]+j]
                        if self.charat(testpos) == mark:
                            self.flood_fill(testpos, mark, replace)

    def clean_grid(self):
        newgrid = []
        for r in range(len(self.grid)):
            newrow = ['.'] * len(self.grid[r])
            newgrid.append(newrow)
        
        for r, c in self.pathpos:
            newgrid[r][c] = self.grid[r][c]

        self.grid = newgrid

    def find_enclosed(self):

        sign = 1 if self.bend > 0 else -1

        for i, o, pos in self.path:
            #char = charat(pos)
            
            if i == 'u':
                testpos = [pos[0], pos[1]-sign]
                outtestpos = [pos[0], pos[1]+sign]
            elif i == 'd':
                testpos = [pos[0], pos[1]+sign]
                outtestpos = [pos[0], pos[1]-sign]
            elif i == 'l':
                testpos = [pos[0]+sign, pos[1]]
                outtestpos = [pos[0]-sign, pos[1]]
            elif i == 'r':
                testpos = [pos[0]-sign, pos[1]]
                outtestpos = [pos[0]+sign, pos[1]]
            self.flood_fill(testpos)
            self.flood_fill(outtestpos, replace='O')


            if o == 'd':
                testpos = [pos[0], pos[1]-sign]
                outtestpos = [pos[0], pos[1]+sign]
            elif o == 'u':
                testpos = [pos[0], pos[1]+sign]
                outtestpos = [pos[0], pos[1]-sign]
            elif o == 'r':
                testpos = [pos[0]+sign, pos[1]]
                outtestpos = [pos[0]-sign, pos[1]]
            elif o == 'l':
                testpos = [pos[0]-sign, pos[1]]
                outtestpos = [pos[0]+sign, pos[1]]
            self.flood_fill(testpos)
            self.flood_fill(outtestpos, replace='O')

    def find_outside(self):        
        i, j = 0, 0
        while self.grid[i][j] != '.':
            j += 1
            if j >= len(self.grid[i]):
                j = 0
                i += 1
        self.flood_fill([i,j], mark = '.', replace='O')
        
    def count(self):
        self.counter = Counter()
        for row in self.grid:
            self.counter += Counter(row)

    def solve(self):
        import sys
        sys.setrecursionlimit(15000)

        self.find_loop()
        self.pathpos = [p for _, _, p in self.path]
        self.clean_grid()
        self.find_outside()
        self.find_enclosed()
        self.count()
        self.print_grid()
        self.answer = self.counter['I']

if __name__ == '__main__':
    # test
    filename = "input/day10test3.txt"
    solution = Solution(filename)
    solution.solve()
    print("Test: ", solution.answers)
    print("Test: ", solution.answer)
    assert solution.answer == 4
    
    # test
    filename = "input/day10test4.txt"
    solution = Solution(filename)
    solution.solve()
    print("Test: ", solution.answers)
    print("Test: ", solution.answer)
    assert solution.answer == 8

    # test
    filename = "input/day10test5.txt"
    solution = Solution(filename)
    solution.solve()
    print("Test: ", solution.answers)
    print("Test: ", solution.answer)
    assert solution.answer == 10

    # real solution
    filename = "input/day10.txt"
    solution = Solution(filename)
    solution.solve()
    print("Solution: ", solution.answers)
    print("Solution: ", solution.answer)