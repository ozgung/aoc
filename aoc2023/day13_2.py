from itertools import product

class Solution:
    def __init__(self, filename):
        self.answer = None
        self.answers = []
        self.parse_input(filename)

    def parse_input(self, filename):
        with open(filename, 'r') as file:
            self.grids = []
            grid = []
            for line in file:
                line = line.strip()
                if line == "":
                    self.grids.append(grid)
                    grid = []
                else:
                    grid.append(line)
            if grid != []:
                self.grids.append(grid)
    
    @staticmethod
    def print_grid(grid):
        for r in grid:
            print(''.join(r))

    @classmethod
    def stringify(cls, l):
        res = []

        for i, n in enumerate(l):
            if i % 2 == 0:
                res.append('#'*n)
            else:
                res.append('.'*n)

        return ''.join(res)

    @classmethod
    def distance(cls, a, b):
        a = Solution.stringify(a)
        b = Solution.stringify(b)

        count = 0
        for c in zip(a, b):
            if c[0] != c[1]:
                count += 1

        if count == 1:
            print(count)

        return count


    @staticmethod
    def find_mirror(sums):

        found = False

        for i in range(0, len(sums)-1):
            smudge = 0
            dst = Solution.distance(sums[i], sums[i+1])
        
            found = True
            for j in range(i, -1, -1):
                r = 2*i-j+1 
                if r < len(sums):
                    dst = Solution.distance(sums[j], sums[r])
                    if dst > 1:
                        found = False
                        break
                    else:
                        smudge += dst
            
            if found and smudge == 1:
                break
                

        return i + 1 if (found and smudge == 1) else 0

    @staticmethod
    def summarize(grid, cols=False):
        run = '#'
        
        rsums = []
        for i in range(len(grid)):
            rsum = [0]
            run = '#'
            for j in range(len(grid[0])):
                
                cur = grid[i][j]
                
                if cur == run[0]:
                    rsum[-1] += 1
                else:
                    run = cur
                    rsum.append(1)
            rsums.append(tuple(rsum))
        
        csums = []
        for j in range(len(grid[0])):
            csum = [0]
            run = '#'
            for i in range(len(grid)):
                
                cur = grid[i][j]
                
                if cur == run[0]:
                    csum[-1] += 1
                else:
                    run = cur
                    csum.append(1)
            csums.append(tuple(csum))
        
        return rsums, csums
        


    def solve(self):

        for grid in self.grids:
            
            self.print_grid(grid)

            rsums, csums = self.summarize(grid)
            
            # check mirrors
            v = self.find_mirror(csums)
            h = self.find_mirror(rsums)
            self.answers.append((v, h))

        self.answer = sum([v+100*h for v,h in self.answers])


if __name__ == '__main__':
    # test
    filename = "input/day13test.txt"
    solution = Solution(filename)
    solution.solve()
    print("Test: ", solution.answers)
    print("Test: ", solution.answer)
    assert solution.answer == 400
    
    # real solution
    filename = "input/day13.txt"
    solution = Solution(filename)
    solution.solve()
    print("Solution: ", solution.answers)
    print("Solution: ", solution.answer)