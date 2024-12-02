cubes = {'red': 12, 'green': 13, 'blue': 14}

def check_num_cube(num, cube):
    print(num, cube)
    return cubes[cube] >= int(num)

def is_possible(line):
    draws = line.split(':')[1].split(';')
    draws = [s.strip() for s in draws]
    print(draws)
    for draw in draws:
        cube_nums = draw.split(',')
        for cube in cube_nums:
            num_cube = cube.strip().split(" ")
            if not check_num_cube(*num_cube):
                return False

    return True

def solution():
    sum = 0
    with open('input/day2.txt', 'r') as file:
        for g, line in enumerate(file):
            if is_possible(line):
                sum += g+1

    print (sum)

if __name__ == '__main__':
    solution()