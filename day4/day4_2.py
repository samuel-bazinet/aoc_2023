with open('input.txt', 'r') as file:
    lines = file.readlines()
    total = 0
    scratchcards = [1 for i in range(len(lines))]
    for (idx, line) in enumerate(lines):
        matching = 0
        cards = line.split(':')[1].split('|')
        winnings = list(map(lambda x: int(x) if len(x) > 0 else -1, cards[0].strip().split(' ')))
        have = list(map(lambda x: int(x) if len(x) > 0 else -2, cards[1].strip().split(' ')))
        for n in have:
            if n in winnings:
                matching += 1
        print(matching, scratchcards[idx])
        for i in range(idx+1, idx+matching+1):
            scratchcards[i] += 1*scratchcards[idx]

    print(sum(scratchcards))