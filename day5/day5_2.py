from typing import List


def process(lines: List[str], seeds: List[int], line_num: int, f_char: str):
    
    while f_char not in lines[line_num]:
        line_num += 1
    line_num += 1
    saved_line = line_num
    len_seeds = len(seeds)
    for j in range(0, len_seeds, 2):  
        print()      
        start = seeds[j]
        end = seeds[j] + seeds[j+1] - 1
        line_num = saved_line
        while line_num < len(lines) and len(lines[line_num].strip()) > 1:
            line_vals = list(map(lambda x: int(x), lines[line_num].split(' ')))
            if line_vals[1] <= start and (line_vals[1] + line_vals[-1]) >= start:
                if (line_vals[1] + line_vals[-1]) <= end:
                    print('c1', start, end, line_vals, end-start +1 )
                    seeds.append(line_vals[0] + (start-line_vals[1]))
                    seeds.append(line_vals[1] + line_vals[-1] - start + 1)
                    seeds[j] = line_vals[1] + line_vals[-1]
                    seeds[j+1] = end - seeds[j]
                    print('result:', seeds[j], seeds[j] + seeds[j+1] - 1, seeds[j+1])
                    print('new:', line_vals[0] + (start-line_vals[1]), line_vals[0] + line_vals[-1], seeds[-1])
                else:
                    print('c2', start, end, line_vals, end-start + 1)
                    seeds[j] = start + (line_vals[0] - line_vals[1])
                    print('result:', seeds[j], end + (line_vals[0] - line_vals[1]) , seeds[j+1])
                break
            elif line_vals[1] <= end and (line_vals[1] + line_vals[-1]) >= end:
                print('c3', start, end, line_vals, end-start +1 )
                seeds[j+1] = line_vals[1] - start
                seeds.append(line_vals[0])
                seeds.append((end - line_vals[1]) + 1)
                print('result:', seeds[j], seeds[j] + seeds[j+1] - 1, seeds[j+1])
                print('new:', line_vals[0], line_vals[0] + seeds[-1] - 1, seeds[-1])
                break
            elif line_vals[1] > start and (line_vals[1] + line_vals[-1]) < end:
                print('c4', start, end, line_vals, end-start +1)
                seeds[j+1] = line_vals[1] - start
                seeds.append(line_vals[0])
                seeds.append(line_vals[-1])
                seeds.append(line_vals[1] + line_vals[-1])
                seeds.append(end - (line_vals[1] + line_vals[-1]) + 1)
                print('result:', seeds[j], seeds[j] + seeds[j+1] - 1, seeds[j+1])
                print('new:', line_vals[0], line_vals[0] + line_vals[-1] - 1, seeds[-3])
                print('new:', line_vals[1] + line_vals[-1],  end, seeds[-1])
                print( seeds[j+1] + seeds[-3] + seeds[-1])
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

    mini = seeds[0]
    print(seeds)
    for idx, seed in enumerate(seeds):
        if idx % 2 == 0:
            mini = min(mini, seed)

    print(mini)
    print(len(seeds))
