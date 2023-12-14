import functools

file = open('input.txt', 'r')
lines = file.readlines()
file.close()

@functools.cache
def roll_north(lines: str) -> str:
    lines = [[char for char in line.strip()] for line in lines.split('\n')]
    for col in range(len(lines[0])):
        for i in range(len(lines)):
            while lines[i][col] == 'O' and i > 0 and lines[i-1][col] == '.':
                lines[i-1][col], lines[i][col]  = lines[i][col] , lines[i-1][col]
                i -= 1
    return '\n'.join([''.join(line) for line in lines])

@functools.cache
def roll_south(lines: str) -> str:
    
    lines = [[char for char in line.strip()] for line in lines.split('\n')]
    for col in range(len(lines[0])):
        for i in range(len(lines), -1, -1):
            while i < len(lines[0])-1 and lines[i][col] == 'O' and lines[i+1][col] == '.':
                lines[i+1][col], lines[i][col]  = lines[i][col] , lines[i+1][col]
                i += 1
    return '\n'.join([''.join(line) for line in lines])

@functools.cache
def roll_west(lines: str) -> str:
    
    lines = [[char for char in line.strip()] for line in lines.split('\n')]
    for row in lines:
        for i in range(len(row)):
            while row[i] == 'O' and i > 0 and row[i-1] == '.':
                row[i-1], row[i] = row[i], row[i-1]
                i -= 1
    return '\n'.join([''.join(line) for line in lines])

@functools.cache
def roll_east(lines: str) -> str:
    
    lines = [[char for char in line.strip()] for line in lines.split('\n')]
    for row in lines:
        for i in range(len(row), -1, -1):
            while i < len(row)-1 and row[i] == 'O' and row[i+1] == '.':
                row[i+1], row[i] = row[i], row[i+1]
                i += 1
    return '\n'.join([''.join(line) for line in lines])

@functools.cache
def cycle(lines: str) -> str:
    return roll_east(roll_south(roll_west(roll_north(lines))))

def print_map(lines: str):
    print(lines)

max_load = len(lines)
load = lambda x: max_load-x
lines = '\n'.join([line.strip() for line in lines])

# print('North')
# print_map(roll_north(lines))
# print()
# print('South')
# print_map(roll_south(lines))
# print()
# print('West')
# print_map(roll_west(lines))
# print()
# print('East')
# print_map(roll_east(lines))

for i in range(1000000000):
    lines = cycle(lines)

print_map(lines)

total_load = 0
lines = [[char for char in line.strip()] for line in lines.split('\n')]

for i, line in enumerate(lines):
    for char in line:
        if char == 'O':
            total_load += load(i)

print(total_load)