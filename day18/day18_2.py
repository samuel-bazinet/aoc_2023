import numpy as np

file = open('input.txt', 'r')
lines = file.readlines()
file.close()

dig_plan = [(0, 0)]
pos = (0, 0)

def size_x(grid: list[tuple[int, int]]) -> tuple[int, int]:
    min = 1000000000
    max = -1000000000
    for plan in grid:
        if plan[1] < min:
            min = plan[1]
        elif plan[1] > max:
            max = plan[1]
    return min, max

def size_y(grid: list[tuple, int, int]) -> tuple[int, int]:
    min = 1000000000
    max = -1000000000
    for plan in grid:
        if plan[0] < min:
            min = plan[0]
        elif plan[0] > max:
            max = plan[0]
    return min, max

num_dir = {
    '0': 'R',
    '1': 'D',
    '2': 'L',
    '3': 'U'
}

for line in lines:
    line = line.strip().split(' ')
    direction = num_dir[line[-1][-2]]
    length = int(line[-1][2:-2], 16)

    if direction == 'R':
        new_pos = (pos[0], pos[1]+length)
    elif direction == 'L':
        new_pos = (pos[0], pos[1]-length)
    elif direction == 'U':
        new_pos = (pos[0]-length, pos[1])
    else:
        new_pos = (pos[0]+length, pos[1])
    
    dig_plan.append(new_pos)
    pos = new_pos

total = 0

for s, e in zip(dig_plan, dig_plan[1:]):
    a = np.array([[s[1], e[1]], [s[0], e[0]]])
    total += np.linalg.det(a) + abs(s[0]-e[0]) + abs(s[1]-e[1])

print(total //2+1)