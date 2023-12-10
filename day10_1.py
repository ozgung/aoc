class Solution:
    def __init__(self, filename):
        self.answer = None
        self.answers = []
        self.parse_input(filename)

    def parse_input(self, filename):
        self.grid = []
        with open(filename, 'r') as file:
            for i, line in enumerate(file):
                s = line.find('S')
                if s >= 0:
                    self.start = [i, s]
                self.grid.append(list(line))
    
    outdirs = ['u', 'd', 'l', 'r']
    indirs  = ['d', 'u', 'r', 'l']
    tiles = {'|': ('u', 'd'),
             '-': ('l', 'r'),
             'L': ('u', 'r'),
             'J': ('u', 'l'),
             '7': ('l', 'd'),
             'F': ('r', 'd'),
             '.': ('', ''),
             'S': ('*', '*')}

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
        return True


        

    def solve(self):
        MAX_STEPS = 100000
        for outdir in self.outdirs:
            self.outdir = outdir
            print('trying', outdir)
            self.cur = self.start
            steps = 0
            while self.move() and steps < MAX_STEPS:
                steps += 1
                #print('steps', steps, self.grid[self.cur[0]][self.cur[1]])
                if self.grid[self.cur[0]][self.cur[1]] == 'S':
                    print('loop found')
                    self.answer = steps // 2
                    return



if __name__ == '__main__':
    # test
    filename = "input/day10test.txt"
    solution = Solution(filename)
    solution.solve()
    print("Test: ", solution.answers)
    print("Test: ", solution.answer)
    assert solution.answer == 4
    
    # test
    filename = "input/day10test2.txt"
    solution = Solution(filename)
    solution.solve()
    print("Test: ", solution.answers)
    print("Test: ", solution.answer)
    assert solution.answer == 8

    # real solution
    filename = "input/day10.txt"
    solution = Solution(filename)
    solution.solve()
    print("Solution: ", solution.answers)
    print("Solution: ", solution.answer)