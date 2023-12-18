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

for line in lines:
    line = line.strip().split(' ')
    direction = line[0]
    length = int(line[1])

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

#print(dig_plan)

X = size_x(dig_plan)
Y = size_y(dig_plan)

dug = [['.' for _ in range(X[1]-X[0]+1)] for _ in range(Y[1]-Y[0]+1)]

min_x = abs(min(0, X[0]))
min_y = abs(min(0, Y[0]))
print(min_x, min_y)

for s, e in zip(dig_plan, dig_plan[1:]):
    if s[0] == e[0]:
        if e[1] > s[1]:
            for i in range(min_x+s[1], min_x+e[1]+1):
                dug[min_y+s[0]][i] = '#'
        else:
            for i in range(min_x+e[1], min_x+s[1]+1):
                dug[min_y+s[0]][i] = '#'
    elif s[1] == e[1]:
        if e[0] > s[0]:
            for i in range(min_y+s[0], min_y+e[0]+1):
                dug[i][min_x+s[1]] = '#'
        else:
            for i in range(min_y+e[0], min_y+s[0]+1):
                dug[i][min_x+s[1]] = '#'

total = 0

visited = set()
queue: list[tuple[int, int]] = [(min_y+1, min_x+1)]
while queue != []:
    current = queue.pop(0)
    if current in visited:
        continue
    visited.add(current)
    for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        to_check = (current[0] + i, current[1]+j)
        if dug[to_check[0]][to_check[1]] != "#" and (to_check[0], to_check[1]) not in visited:
            queue.append(to_check)

for i, j in visited:
    dug[i][j] = '#'


for line in dug:
    for char in line:
        if char == '#':
            total += 1

    

print(total)