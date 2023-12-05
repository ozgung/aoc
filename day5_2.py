def solution(filename):
    scores = [] 

    with open(filename) as file:
        for card  in file:
            card_nums = card.split(':')[1].split('|')
            winning = map(int, card_nums[0].split())
            mynums = map(int, card_nums[1].split())


    return sum(scores)

if __name__ == '__main__':
    filename = "input/day5test.txt"
    print(solution(filename))