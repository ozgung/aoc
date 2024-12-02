class Solution:
    def __init__(self, filename):
        self.answer = None
        self.answers = []
        self.parse_input(filename)

    def parse_input(self, filename):
        
        self.reports = []
        with open(filename, 'r') as file:
            for line in file.readlines():
                self.reports.append(list(map(int, line.strip().split())))
    
    def solve(self):
        cnt = 0
        for report in self.reports:
            p = 1
            dir = (report[1] - report[0]) / abs((report[1] - report[0])) if (report[1] - report[0]) is not 0 else 0
            valid = True
            while p < len(report):
                diff = report[p] - report[p-1]
                if 3 >= (dir * diff) > 0:
                    p += 1
                else:
                    valid = False
                    break
            
            if valid:
                cnt += 1
            self.answers.append(valid)

        self.answer = cnt


if __name__ == '__main__':
    # test
    filename = "./input/day2test.txt"
    solution = Solution(filename)
    solution.solve()
    print("Test: ", solution.answers)
    print("Test: ", solution.answer)
    assert solution.answer == 2
    
    # real solution
    filename = "./input/day2.txt"
    solution = Solution(filename)
    solution.solve()
    print("Solution: ", solution.answers)
    print("Solution: ", solution.answer)