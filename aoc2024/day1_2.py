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

        right = 0
        prev = None
        for left in self.lefts:
            if prev == left:
                self.answers.append(self.answers[-1])
                continue
            cnt = 0
            while right < len(self.rights):
                if self.rights[right] == left:
                    cnt += 1
                    right += 1
                elif self.rights[right] < left:
                    right += 1
                else:
                    break
            self.answers.append(cnt * left)
            prev = left

        self.answer = sum(self.answers)


if __name__ == '__main__':
    # test
    filename = "./input/day1test.txt"
    solution = Solution(filename)
    solution.solve()
    print("Test: ", solution.answers)
    print("Test: ", solution.answer)
    assert solution.answer == 31
    
    # real solution
    filename = "./input/day1.txt"
    solution = Solution(filename)
    solution.solve()
    print("Solution: ", solution.answers)
    print("Solution: ", solution.answer)