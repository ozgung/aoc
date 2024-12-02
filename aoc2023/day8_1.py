from itertools import cycle
from re import search

class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

class Solution:
    def __init__(self, filename):
        self.nodes = {}
        self.answer = None
        self.answers = []
        self.parse_input(filename)

    def parse_input(self, filename):
        with open(filename, 'r') as file:
            self.directions = list(file.readline().strip())
            _ = file.readline()
            
            
            pattern = r"(\w+) = \((\w+), (\w+)\)"
            for line in file:
                print(line)
                matched = search(pattern, line)
                if matched:
                    name, left, right = matched.group(1).strip(), matched.group(2).strip(), matched.group(3).strip()
                    self.nodes[name] = Node(name, left, right)

    def solve(self):
        start = 'AAA'
        dest = 'ZZZ'
        
        curnode = self.nodes[start]
        for i, dir in enumerate(cycle(self.directions)):
            if curnode.name == dest:
                self.answer = i
                return
            
            if dir == 'L':
                if curnode.left == dest:
                    self.answer = i + 1
                    return
                curnode = self.nodes[curnode.left]
            elif dir == 'R':
                if curnode.right == dest:
                    self.answer = i + 1
                    return
                curnode = self.nodes[curnode.right]



if __name__ == '__main__':
    #test
    filename = "input/day8test.txt"
    solution = Solution(filename)
    solution.solve()
    print("Test: ", solution.answers)
    print("Test: ", solution.answer)
    assert solution.answer == 2
    
    # test
    filename = "input/day8test2.txt"
    solution = Solution(filename)
    solution.solve()
    print("Test: ", solution.answers)
    print("Test: ", solution.answer)
    assert solution.answer == 6

    # real solution
    filename = "input/day8.txt"
    solution = Solution(filename)
    solution.solve()
    print("Solution: ", solution.answers)
    print("Solution: ", solution.answer)