

def check_card(winning, card):
    
    p1, p2 = 0, 0
    winning = sorted(winning)
    card = sorted(card)
    wins = 0

    while p1 < len(winning) and p2 < len(card):
        if winning[p1] == card[p2]:
            wins += 1
            p1 += 1
            p2 += 1
        elif winning[p1] < card[p2]:
            p1 += 1
        else:
            p2 += 1

    return 0 if wins == 0 else 2**(wins-1)

def solution(filename):
    scores = [] 

    with open(filename) as file:
        for card  in file:
            card_nums = card.split(':')[1].split('|')
            winning = map(int, card_nums[0].split())
            mynums = map(int, card_nums[1].split())

            score = check_card(winning, mynums)
            scores.append(score)
    return sum(scores)

if __name__ == '__main__':
    filename = "input/day4.txt"
    print(solution(filename))