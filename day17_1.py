from collections import deque
from dataclasses import dataclass
from queue import PriorityQueue
import math


class Solution:
    def __init__(self, filename):
        self.answer = None
        self.answers = []
        self.parse_input(filename)

    def parse_input(self, filename):
        self.maze = []
        with open(filename, 'r') as file:
            for line in file:
                self.maze.append([int(i) for i in line.strip()])


    def print_maze(self, maze):
        for row in maze:
            print(''.join([str(i) for i in row]))

    def solve(self):
        def opposite(d):
            dirs = ['', 'u', 'd', 'l', 'r']
            opposites = ['', 'd', 'u', 'r', 'l']
            return opposites[dirs.index(d)]
        def draw(d):
            dirs = ['', 'u', 'd', 'l', 'r']
            icons = ['', '^', 'v', '<', '>']
            return icons[dirs.index(d)]


        self.print_maze(self.maze)

        W, H = len(self.maze), len(self.maze[0])
        start, finish = (0, 0), (H-1, W-1)
        
        self.costs = [[float('inf')] * W for i in range(H)]
        
        q = PriorityQueue()
        
        q.put((0, start, 0, '', (0,0))) # cost, coor, straight, lastdir, prevcoor

        cache = {}

        finishcost = float('inf')
        while not q.empty():
            
            cost, coor, straight, lastdir, prevcoor = q.get()
            i, j = coor


            if (coor, straight, lastdir) in cache:
                oldcst = cache[(coor, straight, lastdir)]
                if oldcst <= cost:
                    continue
                else:
                    cache[(coor, straight, lastdir)] = cost     
            else:
               cache[(coor, straight, lastdir)] = cost

            if coor == finish:
                finishcost = min(finishcost, cost)
                continue

            for dir, offset in zip(['u', 'd', 'l', 'r'], [[-1, 0],[1, 0],[0, -1],[0, 1]]):
                
                i_new, j_new = (coor[0]+offset[0], coor[1]+offset[1])
                
                if  dir != opposite(lastdir):
                    
                    if i_new >= 0 and j_new >= 0 and i_new < H and j_new < W:

                        newstraight = 1 if dir != lastdir else straight + 1
                
                        if newstraight <= 3:
                            
                            newcost = cost + self.maze[i_new][j_new]

                            q.put((newcost, (i_new, j_new), newstraight, dir, coor))

        

        self.answer = finishcost
        #print(prev)
        c = finish
        # while c != start:
        #     print(c)
        #     self.maze[c[0]][c[1]] = '*'
        #     c = prev[c]

        self.print_maze(self.maze)


if __name__ == '__main__':
    # test
    filename = "input/day17test.txt"
    solution = Solution(filename)
    solution.solve()
    print("Test: ", solution.answers)
    print("Test: ", solution.answer)
    assert solution.answer == 102
    
    # real solution
    filename = "input/day17.txt"
    solution = Solution(filename)
    solution.solve()
    print("Solution: ", solution.answers)
    print("Solution: ", solution.answer)