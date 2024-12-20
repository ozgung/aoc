class Solution:
    def __init__(self, filename):
        self.answer = None
        self.answers = []
        self.parse_input(filename)

    def parse_input(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()

        self.lefts = []
        self.rights = []
        for line in lines:
            l, r = line.strip().split()
            self.lefts.append(int(l))
            self.rights.append(int(r))
    
    def solve(self):
        self.lefts.sort()
        self.rights.sort()
        self.answer = sum([abs(a-b) for a,b in zip(self.lefts, self.rights)])


if __name__ == '__main__':
    # test
    filename = "./input/day1test.txt"
    solution = Solution(filename)
    solution.solve()
    print("Test: ", solution.answers)
    print("Test: ", solution.answer)
    assert solution.answer == 11
    
    # real solution
    filename = "./input/day1.txt"
    solution = Solution(filename)
    solution.solve()
    print("Solution: ", solution.answers)
    print("Solution: ", solution.answer)