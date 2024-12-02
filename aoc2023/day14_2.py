from collections import Counter

NITERS = 1000000000

class Solution:
    def __init__(self, filename):
        self.answer = None
        self.answers = []
        self.parse_input(filename)

    def parse_input(self, filename):
        self.grid = []
        with open(filename, 'r') as file:
            for line in file:
                self.grid.append(list(line.strip()))

    def move_rocks_for_line(self, arr):
        for i in range(len(arr)):
            if arr[i] == '.':
                for j in range(i+1, len(arr)):
                    if arr[j] == 'O':
                        arr[j], arr[i] = arr[i], arr[j]
                        break
                    elif arr[j] == '#':
                        break
                    else:
                        continue
        
        return arr

    def compute_score(self):
        H = len(self.grid)
        self.answers = []
        for i, row in enumerate(self.grid):
            c = Counter(row)
            self.answers.append((H-i) * c['O'])

        self.answer = sum(self.answers)

    def print_grid(self):
        for r in self.grid:
            print(''.join(r))

    def tilt(self, dir):
        if dir in ['S', 'N']:
            cols = []
            for col in zip(*self.grid):
                arr = list(col)
                if dir == 'S':
                    arr.reverse()
                newcol = self.move_rocks_for_line(arr)
                if dir == 'S':
                    newcol = reversed(newcol)
                cols.append(newcol)
            # merge
            self.grid = [list(row) for row in zip(*cols)]
        else:
            rows = []
            for row in self.grid:
                arr = row
                if dir == 'E':
                    arr.reverse()
                newrow = self.move_rocks_for_line(arr)
                if dir == 'E':
                    newrow = reversed(newrow)
                rows.append(newrow)
            # merge
            self.grid = [list(row) for row in rows]

    
    def solve(self):
        print('original')
        self.print_grid()
        
        slow, fast = [0, 0], [0, 0]
        scores = []
        testiter = 200
        for it in range(testiter):
            for d in ['N', 'W', 'S', 'E']:
                self.tilt(d)
                
            self.compute_score()
            scores.append(self.answer)
            print(it, self.answer)

        # find loop in scores
        p = testiter - 2
        for i in range(testiter-3, 1, -1):
            if scores[i] == scores[p] and scores[i-1] == scores[p-1] and scores[i+1] == scores[p+1]:
                loop = p-i
                break
        print('loop', loop, p)
        offset = (NITERS -p-1) % loop
        print('offset', offset)
        self.answer = scores[p-loop+offset]


if __name__ == '__main__':
    # test
    filename = "input/day14test.txt"
    solution = Solution(filename)
    solution.solve()
    print("Test: ", solution.answers)
    print("Test: ", solution.answer)
    assert solution.answer == 64
    
    # real solution
    filename = "input/day14.txt"
    solution = Solution(filename)
    solution.solve()
    print("Solution: ", solution.answers)
    print("Solution: ", solution.answer)