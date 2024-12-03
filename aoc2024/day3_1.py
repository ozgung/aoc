import re

class Solution:
    def __init__(self, filename):
        self.answer = None
        self.answers = []
        self.parse_input(filename)

    def parse_input(self, filename):
        with open(filename, 'r') as file:
            self.input = file.read()    
    def solve(self):
        print(self.input)
        
        reg = r"mul\((\d+),(\d+)\)"
        for mul in re.finditer(reg, self.input):
            a, b = int(mul.group(1)), int(mul.group(2))
            self.answers.append(a * b)
            print(a, b)
        self.answer = sum(self.answers)

if __name__ == '__main__':
    # test
    filename = "input/day3test.txt"
    solution = Solution(filename)
    solution.solve()
    print("Test: ", solution.answers)
    print("Test: ", solution.answer)
    assert solution.answer == 161
    
    # real solution
    filename = "input/day3.txt"
    solution = Solution(filename)
    solution.solve()
    print("Solution: ", solution.answers)
    print("Solution: ", solution.answer)