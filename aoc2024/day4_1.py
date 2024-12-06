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
        dirs = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
        letters = ['M', 'A', 'S']

        m, n = len(self.grid), len(self.grid[0])
        for i, j in product(range(m), range(n)):
            if self.grid[i][j] == 'X':
                for dir in dirs:
                    for s in range(1, 4):
                        y, x = i + dir[0] * s, j + dir[1] * s
                        if 0 <= y < m and 0 <= x < n and self.grid[y][x] == letters[s - 1]:
                            if s == 3:
                                self.answers.append((i, j))
                        else:
                            break

        self.answer = len(self.answers)

if __name__ == '__main__':
    # test
    filename = "input/day4test.txt"
    solution = Solution(filename)
    solution.solve()
    print("Test: ", solution.answers)
    print("Test: ", solution.answer)
    assert solution.answer == 18
    
    # real solution
    filename = "input/day4.txt"
    solution = Solution(filename)
    solution.solve()
    print("Solution: ", solution.answers)
    print("Solution: ", solution.answer)