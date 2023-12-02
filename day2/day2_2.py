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


bags: List[Bag] = []


with open('input.txt', 'r') as file:
    lines = list(map(lambda x: x.strip().split(' '), file.readlines()))
    for line in lines:
        id = int(line[1][:-1])
        bag = Bag(id)
        for (idx, word) in enumerate(line):
            if idx +1 < len(line):
                if line[idx+1][0] == 'r':
                    bag.red = max(bag.red, int(word))
                elif line[idx+1][0] == 'b':
                    bag.blue = max(bag.blue, int(word))
                elif line[idx+1][0] == 'g':
                    bag.green = max(bag.green, int(word))
        bags.append(bag)

total = 0
for bag in bags:
    print(bag.red * bag.green * bag.blue)
    total += (bag.red * bag.green * bag.blue)


print(f'total: {total}')
