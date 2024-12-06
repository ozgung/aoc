class Solution:
    def __init__(self, filename):
        self.answer = None
        self.answers = []
        self.parse_input(filename)

    def parse_input(self, filename):
        self.rules = set()
        self.updates = []
        rules = True
        with open(filename, 'r') as file:
            for line in file:
                if line == "\n":
                    rules = False
                    continue
                if rules:
                    self.rules.add(tuple(map(int, line.split('|'))))
                else:
                    self.updates.append(list(map(int, line.strip().split(','))))
    
    def solve(self):
        def check(update):
            for i in range(len(update)):
                for j in range(i + 1, len(update)):
                    if (update[j],update[i]) in self.rules:
                        return False
            return True
            
        for update in self.updates:
            if check(update):
                self.answers.append(update[len(update) // 2])

        self.answer = sum(self.answers)

if __name__ == '__main__':
    # test
    filename = "input/day5test.txt"
    solution = Solution(filename)
    solution.solve()
    print("Test: ", solution.answers)
    print("Test: ", solution.answer)
    assert solution.answer == 143
    
    # real solution
    filename = "input/day5.txt"
    solution = Solution(filename)
    solution.solve()
    print("Solution: ", solution.answers)
    print("Solution: ", solution.answer)