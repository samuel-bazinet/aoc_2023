from typing import Dict, List, Tuple

class Input:
    hand: str
    bid: int
    rank: int

    def __init__(self, hand: str, bid: int, rank: int):
        self.hand = hand
        self.bid = bid
        self.rank = rank

    def hand_power(self) -> List[Tuple[str, int]]:
        cards = {}
        for card in self.hand:
            if card in cards:
                cards[card] += 1
            else:
                cards[card] = 1
        return list(sorted([(k, v) for k, v in cards.items()], key = lambda x: x[1], reverse=True))
    
pow_cards = {
    'A': 13,
    'K': 12,
    'Q': 11,
    'J': 10,
    'T': 9,
    '9': 8,
    '8': 7,
    '7': 6,
    '6': 5,
    '5': 4,
    '4': 3,
    '3': 2,
    '2': 1
}

    
def compare_inputs(hand_a: Input, hand_b: Input) -> bool: 
    hand_a_power = hand_a.hand_power()
    hand_b_power = hand_b.hand_power()
    
    # print(hand_a.hand, hand_a.rank)
    # print(hand_b.hand, hand_b.rank)
    # print(hand_a_power)
    # print(hand_b_power)

    if len(hand_a_power) < len(hand_b_power):
        #print('A')
        return True
    elif len(hand_a_power) > len(hand_b_power):
        #print('B')
        return False
    
    elif len(hand_a_power) == len(hand_b_power):
        if hand_a_power[0][1] == 4: 
            if hand_b_power[0][1] != 4:
                #print('A')
                return True

        elif hand_b_power[0][1] == 4:
            #print('B')
            return False
        
        elif hand_a_power[0][1] == 3:
            if hand_b_power[0][1] == 2:
                #print('A')
                return True
            
        elif hand_b_power[0][1] == 3:
            #print('B')
            return False

    for (a, b) in zip(hand_a.hand, hand_b.hand):
        if pow_cards[a] > pow_cards[b]:
            #print('A')
            return True
        elif pow_cards[b] > pow_cards[a]:
            #print('B')
            return False
    
                    

with open('input.txt', 'r') as file:
    lines = file.readlines()
    ranks = len(lines)

    inputs: List[Input] = []

    for line in lines:
        split_line = line.split(' ')
        inputs.append(Input(split_line[0], int(split_line[1]), ranks))
    
    for val1 in inputs:
        for val2 in reversed(inputs):
            if val1 == val2:
                break
            if compare_inputs(val1, val2):
                val2.rank -= 1
            else:
                val1.rank -= 1
    
    total = 0
    for val in inputs:
        #print(val.hand, val.bid, val.rank)
        total += val.bid * val.rank

    print(total)
    


