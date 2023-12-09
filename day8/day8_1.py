from typing import Dict


class Options:
    left: str
    right: str

    def __init__(self, left: str, right: str):
        self.left = left
        self.right = right

with open('input.txt', 'r') as file:
    lines = file.readlines()

    option_map: Dict[str, Options] = {}

    pattern = lines[0].strip()

    for line in lines[2:]:
        option = line.strip().split(' ')
        option_map[option[0]] = Options(option[2][1:-1], option[3][:-1])

    current_option = 'AAA'
    length = 0

    while current_option != 'ZZZ':
        for direction in pattern:
            
            if direction == 'L':
                current_option = option_map[current_option].left
            else:
                current_option = option_map[current_option].right
            
            length += 1
            if current_option == 'ZZZ':
                break

    print(length)


