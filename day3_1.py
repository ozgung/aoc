import string


def extract_number(matrix, loc):
    row = matrix[loc[0]]
    start, end = loc[1], loc[1]
    while start - 1 >= 0 and row[start - 1].isdigit():
        start -= 1
    while end + 1 < len(row) and row[ end + 1].isdigit():
        end += 1
    num = int(''.join(row[start:end+1]))

    row[start:end+1] = '.' * (end + 1 - start)

    return num


def search_loc(matrix, loc) -> list:
    nums = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                if matrix[loc[0]+i][loc[1]+j].isdigit():
                    num = extract_number(matrix, (loc[0]+i, loc[1]+j))
                    nums.append(num)

    return nums


def find_symbol(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] in string.punctuation and matrix[i][j] != '.':
                yield (i, j)

def parse_data(fname):
    with open(fname) as file:
        lines = file.read().split('\n')

    matrix = [list(line) for line in lines]
    return matrix


def solution():
    matrix = parse_data('input/day3.txt')

    total = 0
    for loc in find_symbol(matrix):
        nums = search_loc(matrix, loc)
        locsum = sum(nums)
        print(nums, locsum)
        total += locsum

    return total


if __name__ == '__main__':
    print("soln", solution())
