from  copy import deepcopy

class Solution:
    def __init__(self, filename):
        self.answer = None
        self.answers = []
        self.parse_input(filename)
        self.energized = [[set() for j in range(len(self.layout[0]))] for i in range(len(self.layout))]

    def parse_input(self, filename):
        self.layout = []
        with open(filename, 'r') as file:
            for line in file:
                self.layout.append(line.strip())
    
    def compute_energy(self):
        count = 0
        for row in self.energized:
            for el in row:
                if el:
                    count += 1
        return count
    
    def move_beams(self):
        lookup_m1 = {'u': 'r', 'd': 'l',  'l': 'd',  'r': 'u'} # /
        lookup_m2 = {'u': 'l', 'd': 'r',  'l': 'u',  'r': 'd'} # \

        iter = 0
        while len(self.beams) and iter < 1000:
            iter += 1
            dirty = []
            newbeams = []
            for i, beam in enumerate(self.beams):
                dir = beam[1]
                if dir == 'u':
                    beam[0][1] -= 1
                elif dir == 'd':
                    beam[0][1] += 1
                elif dir == 'l':
                    beam[0][0] -= 1
                elif dir == 'r':
                    beam[0][0] += 1
            
                # check ranges
                x, y = beam[0]
                if x < 0 or y < 0 or x >= len(self.layout[0]) or y >= len(self.layout):
                    dirty.append(i)
                    continue
                
                if dir not in self.energized[y][x]:
                    self.energized[y][x].add(dir)
                else:
                    dirty.append(i)
                    

                tile = self.layout[y][x]
                if tile == '.':
                    pass
                # mirrors
                elif tile == '/':
                    newdir = lookup_m1[beam[1]]
                    beam[1] =  newdir
                elif tile == '\\':
                    newdir = lookup_m2[beam[1]]
                    beam[1] =  newdir
                # splitters
                elif tile == '-':
                    if beam[1] in 'ud':
                        newbeam = deepcopy(beam)
                        beam[1] = 'l'
                        newbeam[1] = 'r'
                        newbeams.append(newbeam)
                elif tile == '|':
                    if beam[1] in 'lr':
                        newbeam = deepcopy(beam)
                        beam[1] = 'u'
                        newbeam[1] = 'd'
                        newbeams.append(newbeam)
            
            for d in sorted(dirty, reverse=True):
                    self.beams.pop(d)

            for nb in newbeams:
                self.beams.append(nb)

    def reset(self):
        self.energized = [[set() for j in range(len(self.layout[0]))] for i in range(len(self.layout))]

    def solve(self):
        W, H = len(self.layout[0]), len(self.layout)
        # north
        for i in range(W):
            self.reset()
            self.beams = [[[i, -1], 'd']]
            self.move_beams()
            self.answers.append(self.compute_energy())
        # south
        for i in range(W):
            self.reset()
            self.beams = [[[i, H], 'u']]
            self.move_beams()
            self.answers.append(self.compute_energy())
        # west
        for i in range(H):
            self.reset()
            self.beams = [[[-1, i], 'r']]
            self.move_beams()
            self.answers.append(self.compute_energy())
        # east
        for i in range(H):
            self.reset()
            self.beams = [[[W, i], 'l']]
            self.move_beams()
            self.answers.append(self.compute_energy())


        self.answer = max(self.answers)


if __name__ == '__main__':
    # test
    filename = "input/day16test.txt"
    solution = Solution(filename)
    solution.solve()
    print("Test: ", solution.answers)
    print("Test: ", solution.answer)
    assert solution.answer == 51
    
    #real solution
    filename = "input/day16.txt"
    solution = Solution(filename)
    solution.solve()
    print("Solution: ", solution.answers)
    print("Solution: ", solution.answer)