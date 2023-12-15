class Solution:
    def __init__(self, filename):
        self.answer = None
        self.answers = []
        self.parse_input(filename)

    def parse_input(self, filename):
        with open(filename, 'r') as file:
            self.codes = file.read().strip().split(',')
    
    def hash(self, code):
        cur = 0
        for c in code:
            cur += ord(c)
            cur *= 17
            cur = cur % 256

        return cur

    def solve(self):
        for code in self.codes:
            self.answers.append(self.hash(code))

        self.answer = sum(self.answers)


if __name__ == '__main__':
    
    
    # test
    filename = "input/day15test.txt"
    solution = Solution(filename)
    solution.hash('HASH')
    solution.solve()
    print("Test: ", solution.answers)
    print("Test: ", solution.answer)
    assert solution.answer == 1320
    
    # real solution
    filename = "input/day15.txt"
    solution = Solution(filename)
    solution.solve()
    print("Solution: ", solution.answers)
    print("Solution: ", solution.answer)