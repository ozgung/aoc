def get_number(line):
    print(len(line))
    l, r = 0, len(line) - 1
    lfound, rfound = False, False
    print(l)
    while l <= r and not (lfound and rfound):
        #print(line, l, r)
        if not lfound:
            if line[l].isdigit():
                lnum = int(line[l])
                lfound = True
            else:
                l += 1
        if not rfound:
            if line[r].isdigit():
                rnum = int(line[r])
                rfound = True
            else:
                r += -1

    return 10*lnum + rnum
    

def trebuchet():
    filename = 'input/trebuchet.txt'
    sum = 0

    with open(filename, 'r') as file:
        for line in file:
           num = get_number(line)
           print(num)
           sum += num
    
    return sum

if __name__=='__main__':
    print(trebuchet())