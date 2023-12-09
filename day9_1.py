class Solution:
    def __init__(self, filename):
        self.answer = None
        self.answers = []
        self.parse_input(filename)

    def parse_input(self, filename):
        self.sequences = []
        with open(filename, 'r') as file:
            for line in file:
                self.sequences.append(list(map(int, line.split())))


    def compute_differences(self, arr):
        result = []
        for i in range(len(arr) - 1):
            result.append(arr[i + 1]- arr[i])
        return result

    def solve(self):
        
        for seq in self.sequences:
            diffs = [seq]
            while not all([x == 0 for x in diffs[-1]]):
                diffs.append(self.compute_differences(diffs[-1]))

            # compute new elements
            for i in range(len(diffs)-1, 0, -1):
                newel = diffs[i-1][-1] + diffs[i][-1]
                diffs[i-1].append(newel)
            
            self.answers.append(diffs[0][-1])

        self.answer = sum(self.answers)

if __name__ == '__main__':
    # test
    filename = "input/day9test.txt"
    solution = Solution(filename)
    solution.solve()
    print("Test: ", solution.answers)
    print("Test: ", solution.answer)
    assert solution.answer == 114
    
    # real solution
    filename = "input/day9.txt"
    solution = Solution(filename)
    solution.solve()
    print("Solution: ", solution.answers)
    print("Solution: ", solution.answer)