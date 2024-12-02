from collections import Counter

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

        for i, row in enumerate(self.grid):
            c = Counter(row)
            self.answers.append((H-i) * c['O'])

        self.answer = sum(self.answers)

    def print_grid(self):
        for r in self.grid:
            print(''.join(r))

    def solve(self):
        self.print_grid()
        # tilt North        

        cols = []
        for j, col in enumerate(zip(*self.grid)):

            newcol = self.move_rocks_for_line(list(col))
            print(col, newcol)
            # replace col
            # for i in range(len(self.grid)):
            #     self.grid[i][j] = newcol[j]
            cols.append(newcol)
        # merge
        self.grid = [list(row) for row in zip(*cols)]

        self.compute_score()
        print()
        self.print_grid()

if __name__ == '__main__':
    # test
    filename = "input/day14test.txt"
    solution = Solution(filename)
    solution.solve()
    print("Test: ", solution.answers)
    print("Test: ", solution.answer)
    assert solution.answer == 136
    
    # real solution
    filename = "input/day14.txt"
    solution = Solution(filename)
    solution.solve()
    print("Solution: ", solution.answers)
    print("Solution: ", solution.answer)