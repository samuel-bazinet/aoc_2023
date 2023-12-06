from typing import List


def process(lines: List[str], seeds: List[int], line_num: int, f_char: str):
    
    while f_char not in lines[line_num]:
        line_num += 1
    line_num += 1
    saved_line = line_num
    for j in range(len(seeds)):
        line_num = saved_line
        while line_num < len(lines) and len(lines[line_num].strip()) > 1:
            line_vals = list(map(lambda x: int(x), lines[line_num].split(' ')))
            print(line_vals)

            if seeds[j] in range(line_vals[1], line_vals[1] + line_vals[-1]):
                #print('match')
                #print(seeds[j], line_vals[1])
                seeds[j] = line_vals[0] + (seeds[j] - line_vals[1])
                break
            line_num += 1

with open('input.txt', 'r') as file:
    lines = file.readlines()
    seeds = list(map(lambda x: int(x), lines[0].strip().split(':')[1].strip().split(' ')))

    line_num = 1
    
    process(lines, seeds, line_num, 'seed-')
    process(lines, seeds, line_num, 'soil-')
    process(lines, seeds, line_num, 'zer-')
    process(lines, seeds, line_num, 'ter-')
    process(lines, seeds, line_num, 'ght-')
    process(lines, seeds, line_num, 'ure-')
    process(lines, seeds, line_num, 'ity-')

    print(min(seeds))
