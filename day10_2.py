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
        print(self.cur, p, next)
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
            print('trying', startdir)
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

    def flood_fill(self, start, mark='.', replace='I'):
        def charat(p):
            if p[0] < 0 or p[1] < 0 or p[0] >= len(self.grid) or p[1] >= len(self.grid[0]):
                return None
            else:
                return self.grid[p[0]][p[1]]
        def setcharat(p, c):
            if p[0] < 0 or p[1] < 0 or p[0] >= len(self.grid) or p[1] >= len(self.grid[0]):
                return
            else:
                self.grid[p[0]][p[1]] = c
        
        #if charat(start) == mark:
        if start not in self.pathpos and charat(start) != replace:   
            print("dot found")
            setcharat(start, replace)
            self.insides += 1
            
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if not (i == 0 and j == 0):
                        testpos = [start[0]+i, start[1]+j]
                        self.flood_fill(testpos)


    def find_enclosed(self):
        def charat(p):
            if p[0] < 0 or p[1] < 0 or p[0] >= len(self.grid) or p[1] >= len(self.grid[0]):
                return None
            else:
                return self.grid[p[0]][p[1]]

        sign = 1 if self.bend > 0 else -1

        for i, o, pos in self.path:
            char = charat(pos)
            
            if i == 'u':
                testpos = [pos[0], pos[1]-sign]
            elif i == 'd':
                testpos = [pos[0], pos[1]+sign]
            elif i == 'l':
                testpos = [pos[0]+sign, pos[1]]
            elif i == 'r':
                testpos = [pos[0]-sign, pos[1]]
            self.flood_fill(testpos)
            


        
    def solve(self):
        self.find_loop()
        print(self.bend, self.path)
        self.pathpos = [p for _, _, p in self.path]
        print(self.pathpos)
        self.print_grid()
        self.find_enclosed()
        self.print_grid()
        self.answer = self.insides
        


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