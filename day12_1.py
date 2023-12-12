class Solution:
    def __init__(self, filename):
        self.answer = None
        self.answers = []
        self.parse_input(filename)

    def parse_input(self, filename):
        
        self.springs = []
        self.groups = []

        with open(filename, 'r') as file:
            for line in file:
                s, g = line.split()
                self.springs.append(s)
                self.groups.append(list(map(int, g.split(','))))
    
    def decrement_g(self, g):
            g[0] -= 1
            if g[0] <= 0:
                return g[1:-1]



    def count(self, s, g):
        '''adapted from github.com/hyper-neutrino'''
        if s == "":
            return 1 if g == [] else 0
        
        if g == []:
            return 0 if '#' in s else 1

        res = 0

        if s[0] in '.?':
            res += self.count(s[1:], g)
        
        if s[0] in '#?':
            cur = s[:g[0]]

            if len(s) >= g[0] and len(cur) == g[0] and '.' not in cur and (len(s) == g[0] or s[g[0]] != '#'):
                res += self.count(s[g[0] + 1:], g[1:])

        return res

    def solve(self):
        for s, g in zip(self.springs, self.groups):
            print('----------')
            self.answers.append(self.count(s, g))


        self.answer = sum(self.answers)


if __name__ == '__main__':
    # test
    filename = "input/day12test.txt"
    solution = Solution(filename)
    solution.solve()
    print("Test: ", solution.answers)
    print("Test: ", solution.answer)
    assert solution.answer == 21
    
    # real solution
    filename = "input/day12.txt"
    solution = Solution(filename)
    solution.solve()
    print("Solution: ", solution.answers)
    print("Solution: ", solution.answer)