class Solution:
    def __init__(self, filename):
        self.answer = None
        self.answers = []
        self.parse_input(filename)

    def parse_input(self, filename):
        self.bricks = []
        with open(filename, 'r') as file:
            for line in file:
                ends = line.strip().split('~')
                self.bricks.append([ list(map(int, e.split(','))) for e in ends])
    


    def solve(self):
        
        for brick in self.bricks:
            start, end = brick
            


if __name__ == '__main__':
    # test
    filename = "input/day22test.txt"
    solution = Solution(filename)
    solution.solve()
    print("Test: ", solution.answers)
    print("Test: ", solution.answer)
    assert solution.answer == 0
    
    # real solution
    filename = "input/day22.txt"
    solution = Solution(filename)
    solution.solve()
    print("Solution: ", solution.answers)
    print("Solution: ", solution.answer)