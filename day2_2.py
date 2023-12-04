
def check_num_cube(num, cube):
    print(num, cube)
    return cubes[cube] >= int(num)

def update_cube(num, cube, dict):
    print(num, cube)
    if dict[cube] < int(num):
        dict[cube] = int(num)

def compute_power(cube):
    return cube['red'] * cube['green'] * cube['blue']

def make_possible(line):
    draws = line.split(':')[1].split(';')
    draws = [s.strip() for s in draws]
    print(draws)
    
    min_cube = {'red': 0, 'green': 0, 'blue': 0}

    for draw in draws:
        cube_nums = draw.split(',')
        for cube in cube_nums:
            num_cube = cube.strip().split(" ")
            update_cube(*num_cube, min_cube)

    return compute_power(min_cube)


def solution():
    sum = 0
    with open('input/day2.txt', 'r') as file:
        for g, line in enumerate(file):
            power = make_possible(line)
            sum += power

    print (sum)

if __name__ == '__main__':
    solution()