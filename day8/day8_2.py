from typing import Dict, List

from math import lcm

class Options:
    left: str
    right: str

    def __init__(self, left: str, right: str):
        self.left = left
        self.right = right

def all_ends_z(l: List[str]) -> bool:
    for i in l:
        if i[-1] != 'Z':
            return False
    return True

def matching(s: Options, e: Options) -> bool:
    return (s.left == e.left or s.right == e.right) or (s.right == e.left or s.left == e.right)

with open('input.txt', 'r') as file:
    lines = file.readlines()

    option_map: Dict[str, Options] = {}

    pattern = lines[0].strip()

    for line in lines[2:]:
        option = line.strip().split(' ')
        option_map[option[0]] = Options(option[2][1:-1], option[3][:-1])

    length = 0

    current_options = list(filter(lambda x: x[-1] == 'A', list(option_map.keys())))
    

    ending_points = list(filter(lambda x: x[-1] == 'Z', list(option_map.keys())))

    matching_s_e = []

    for i in current_options:
        current_option = option_map[i]
        for j in ending_points:
            end_point = option_map[j]
            if matching(current_option, end_point):
                matching_s_e.append((i, j))

    print(matching_s_e)

    cycle_lengths = []

    state = True

    for (s, e) in matching_s_e:
        current_option = s
        state = True
        while state:
            for direction in pattern:
                if direction == 'L':
                    current_option = option_map[current_option].left
                else:
                    current_option = option_map[current_option].right
                    
                length += 1
                state = not (current_option == e)
                if not state:
                    cycle_lengths.append(length)
                    length = 0
                    break

    c_lcm = cycle_lengths[0]
    for i in cycle_lengths:
        c_lcm = lcm(c_lcm, i)

    print(cycle_lengths)
    print(c_lcm)


