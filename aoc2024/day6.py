from itertools import product


class Solution:
    def __init__(self, filename):
        self.answer = None
        self.answers = []
        self.parse_input(filename)

    def parse_input(self, filename):
        self.grid = []
        with open(filename, 'r') as file:
            for line in file:
                self.grid.append(list(line.strip()))
    
    def solve(self):
        # find the start pos
        dirs = ['U', 'R', 'D', 'L']
        steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        cnt = 0
        dir = 0
        m, n = len(self.grid), len(self.grid[0])
        for i, j in product(range(m), range(n)):
            if self.grid[i][j] == '^':
                pos = (i, j)
                cnt = 1
                self.grid[i][j] = 'U'
                break
        
        # find the path
        # walk
        while 0 <= pos[0] < m and 0 <= pos[1] < n:
            nextpos = pos[0] + steps[dir][0], pos[1] + steps[dir][1]
            print(nextpos)
            if 0 <= nextpos[0] < m and 0 <= nextpos[1] < n:
                if self.grid[nextpos[0]][nextpos[1]] == '#':
                    dir = (dir + 1) % 4
                    continue
                else:
                    if self.grid[nextpos[0]][nextpos[1]] == '.':
                        cnt += 1
                        self.grid[nextpos[0]][nextpos[1]] = 'X'
            pos = nextpos
        for r in self.grid:
            print(r)
        self.answer = cnt


if __name__ == '__main__':
    # test
    filename = "input/day6test.txt"
    solution = Solution(filename)
    solution.solve()
    print("Test: ", solution.answers)
    print("Test: ", solution.answer)
    assert solution.answer == 41
    
    # real solution
    filename = "input/day6.txt"
    solution = Solution(filename)
    solution.solve()
    print("Solution: ", solution.answers)
    print("Solution: ", solution.answer)