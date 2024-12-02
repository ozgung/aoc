from itertools import product

EXPANSION_FACTOR = 1000000

class Solution:
    def __init__(self, filename):
        self.answer = None
        self.answers = []
        self.parse_input(filename)

    def parse_input(self, filename):
        self.space = []
        self.galaxies = []
        with open(filename, 'r') as file:
            for line in file:
                row = list(line.strip())
                self.space.append(row)

        self.size = (len(self.space), len(self.space[0])) # H, W

    def print_space(self):
        for row in self.space:
            print(''.join(row))

    def find_galaxies(self):

        self.galaxies = []
        self.expansion_rows = [1] * self.size[0]
        self.expansion_cols = [1] * self.size[1]
        for i, j in product(range(self.size[0]), range(self.size[1])):
            if self.space[i][j] == '#':
                self.galaxies.append([i, j])
                self.expansion_rows[i] = 0
                self.expansion_cols[j] = 0

    def find_pairs(self):
        self.pairs = []
        for i in range(len(self.galaxies)):
            for j in range(i+1, len(self.galaxies)):
                self.pairs.append((self.galaxies[i], self.galaxies[j]))


    def find_distances(self):
        def dist(p1, p2):
            '''Manhattan Distance'''
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        self.distances = []
        for pair in self.pairs:
            rexp = sum(self.expansion_rows[min(pair[0][0], pair[1][0]): max(pair[0][0], pair[1][0])])
            cexp = sum(self.expansion_cols[min(pair[0][1], pair[1][1]): max(pair[0][1], pair[1][1])])

            self.distances.append(dist(*pair) + (rexp + cexp) * (EXPANSION_FACTOR - 1))

    def solve(self):
        self.print_space()
        self.find_galaxies()
        self.find_pairs()
        self.find_distances()

        self.answers = self.distances
        self.answer = sum(self.answers)

if __name__ == '__main__':
    # test
    filename = "input/day11test.txt"
    solution = Solution(filename)
    solution.solve()
    print("Test: ", solution.answers)
    print("Test: ", solution.answer)
    if EXPANSION_FACTOR == 2:
        assert solution.answer == 374
    if EXPANSION_FACTOR == 10:
        assert solution.answer == 1030
    if EXPANSION_FACTOR == 100:
        assert solution.answer == 8410
    
    # real solution
    filename = "input/day11.txt"
    solution = Solution(filename)
    solution.solve()
    print("Solution: ", solution.answers)
    print("Solution: ", solution.answer)