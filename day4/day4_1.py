with open('input.txt', 'r') as file:
    lines = file.readlines()
    total = 0
    for line in lines:
        matching = -1
        cards = line.split(':')[1].split('|')
        winnings = list(map(lambda x: int(x) if len(x) > 0 else -1, cards[0].strip().split(' ')))
        have = list(map(lambda x: int(x) if len(x) > 0 else -2, cards[1].strip().split(' ')))
        for n in have:
            if n in winnings:
                matching += 1
        
        if matching >= 0:
            total += 2**matching

    print(total)