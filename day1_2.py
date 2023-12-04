numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numbers_rev = [s[::-1] for s in numbers]

def check_at(line, nums, start):
    if line[start].isdigit():
        return int(line[start])
    
    for i, w in enumerate(nums):
        # check if w starts at start
        cur = 0
        while start+cur < len(line) and cur < len(w):
            if line[start+cur] != w[cur]:
                break
            else:
                cur += 1
                if cur == len(w):
                    return i
        
    return -1

def get_number(line):
    
    l, r = 0, 0
    lfound, rfound = False, False
    line_rev = line[::-1]

    while l < len(line) and not lfound:
        numl = check_at(line, numbers, l)
        if numl >= 0:
            lnum = numl
            lfound = True
        else:
            l += 1

    while r < len(line_rev) and not rfound:
        numr = check_at(line_rev, numbers_rev, r)
        if numr >= 0:
            rnum = numr
            rfound = True
        else:
            r += 1
    
    print(line, lnum, rnum)

    return 10*lnum + rnum
    

def trebuchet():
    filename = 'input/trebuchet.txt'
    sum = 0

    with open(filename, 'r') as file:
        for line in file:
           num = get_number(line)
           #print(num)
           sum += num
    
    return sum

if __name__=='__main__':
    print(trebuchet())
    print(numbers_rev)