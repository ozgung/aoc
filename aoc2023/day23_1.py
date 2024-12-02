class Solution:
    def __init__(self, filename):
        self.answer = None
        self.answers = []
        self.parse_input(filename)

    def print_grid(self, grid):
        print("")
        for r in grid:
            print(''.join(r))

    def parse_input(self, filename):
        self.grid = []
        with open(filename, 'r') as file:
            for line in file:
                self.grid.append(list(line.strip()))
    
    

    def solve(self):
        self.print_grid(self.grid)

        start, finish = self.grid[0].index('.'), self.grid[-1].index('.')
        start, finish = [0, start], [-1, finish]
        print(start, finish)

        self.dfs(start, finish)

if __name__ == '__main__':
    # test
    filename = "input/day23test.txt"
    solution = Solution(filename)
    solution.solve()
    print("Test: ", solution.answers)
    print("Test: ", solution.answer)
    assert solution.answer == 94
    
    # real solution
    filename = "input/day23.txt"
    solution = Solution(filename)
    solution.solve()
    print("Solution: ", solution.answers)
    print("Solution: ", solution.answer)