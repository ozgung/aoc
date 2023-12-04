

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

    return wins

def solution(filename):

    with open(filename) as file:
        cards = file.readlines()

    copies = [1] * len(cards)

    for i, card  in enumerate(cards):
        card_nums = card.split(':')[1].split('|')
        winning = map(int, card_nums[0].split())
        mynums = map(int, card_nums[1].split())

        wins = check_card(winning, mynums)

        for j in range(wins):
            if i + j + 1 < len(copies):
                copies[i + j + 1] += copies[i]

    return sum(copies)

if __name__ == '__main__':
    filename = "input/day4.txt"
    print(solution(filename))