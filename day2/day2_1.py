from typing import List


class Bag:
    id: int
    red: int
    blue: int
    green: int

    def __init__(self, id):
        self.id = id
        self.red = 0
        self.blue = 0
        self.green = 0

T_RED = 12
T_GREEN = 13
T_BLUE = 14

bags: List[Bag] = []

def check_bag(bag: Bag) -> bool:
    return bag.red <= T_RED and bag.green <= T_GREEN and bag.blue <= T_BLUE

with open('input.txt', 'r') as file:
    lines = list(map(lambda x: x.strip().split(' '), file.readlines()))
    for line in lines:
        id = int(line[1][:-1])
        bag = Bag(id)
        for (idx, word) in enumerate(line):
            if word[-1] == ';':
                if check_bag(bag):
                    bag = Bag(id)
                else: 
                    break
            if idx +1 < len(line):
                if line[idx+1][0] == 'r':
                    bag.red += int(line[idx])
                elif line[idx+1][0] == 'b':
                    bag.blue += int(line[idx])
                elif line[idx+1][0] == 'g':
                    bag.green += int(line[idx])
        if check_bag(bag):
            print(bag.id, bag.red, bag.green, bag.blue)
            bags.append(bag)
        else:
            print(f'BAD: {bag.id}, {bag.red}, {bag.green}, {bag.blue}')

total = 0
for bag in bags:
    print(bag.id, bag.red, bag.green, bag.blue)
    if bag.red <= T_RED and bag.green <= T_GREEN and bag.blue <= T_BLUE:
        total += bag.id


print(f'total: {total}')
