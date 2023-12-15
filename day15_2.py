class Solution:
    def __init__(self, filename):
        self.answer = None
        self.answers = []
        self.parse_input(filename)

    def parse_input(self, filename):
        with open(filename, 'r') as file:
            self.codes = file.read().strip().split(',')
    
    def hash(self, code):
        cur = 0
        for c in code:
            cur += ord(c)
            cur *= 17
            cur = cur % 256

        return cur

    def insert(self, idx, label, f):
        box = self.boxes[idx]
        for i in range(len(box)):
            if box[i][0] == label:
                box[i][1] = f
                return
        # not found
        box.append([label, f])

    def remove(self, idx, label):
        box = self.boxes[idx]
        for i in range(len(box)):
            if box[i][0] == label:
                box.pop(i)
                return

    def compute_focal(self, ):
        
        for b in range(len(self.boxes)):
            for s  in range(len(self.boxes[b])):
                f = self.boxes[b][s][1]
                fpower = (b+1) * (s+1) * f
                self.answers.append(fpower)

        self.answer = sum(self.answers)
            
    def solve(self):
        
        self.boxes = [[] for _ in range(256)]
        
        for code in self.codes:
            if code[-1] == '-':
                label = code[:-1]
                boxidx = self.hash(label)
                self.remove(boxidx, label)
            else:
                label, f = code.split('=')
                boxidx = self.hash(label)
                self.insert(boxidx, label, int(f))
        self.compute_focal()



if __name__ == '__main__':
    # test
    filename = "input/day15test.txt"
    solution = Solution(filename)
    solution.solve()
    print("Test: ", solution.answers)
    print("Test: ", solution.answer)
    assert solution.answer == 145
    
    # real solution
    filename = "input/day15.txt"
    solution = Solution(filename)
    solution.solve()
    print("Solution: ", solution.answers)
    print("Solution: ", solution.answer)