file = open('input.txt', 'r')
lines = file.readlines()
file.close()

lines = [[char for char in line.strip()] for line in lines]

starting_point = (-1, -1)

H = len(lines)
W = len(lines[0])

def is_valid(tent_coord: tuple[int, int]) -> bool:
    return lines[tent_coord[0]][tent_coord[1]] != "#" 

def update_bounds(tent_coord):
    v, h = tent_coord
    while v < 0:
        v = v + H
    while v > H-1:
        v -= H

    while h < 0:
        h += W
    while h > W-1:
        h -= W
    return (v, h)

def get_neighbours(coord: tuple[int, int]) -> list[tuple[int, int]]:
    for i in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_coord = (coord[0] + i[0], coord[1] + i[1])
        new_coord_tc = update_bounds(new_coord)
        if is_valid(new_coord_tc):
            yield new_coord

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == 'S':
            starting_point = (i, j)

# Idea: use bfs and a new queue for each step
new_queue = set()
new_queue.add(starting_point)

def f(n):
    a0 = 3893
    a1 = 34785
    a2 = 96471

    b0 = a0
    b1 = a1-a0
    b2 = a2-a1
    return b0 + b1*n + (n*(n-1)//2)*(b2-b1)

for i in range(1):
    queue = new_queue
    new_queue = set()
    while len(queue) > 0:
        el = queue.pop()
        for next_coord in get_neighbours(el):
            new_queue.add(next_coord)
    if i == 64 or i == ((131+65)-1) or i == ((65+(131)*2)-1):
        print(len(new_queue))

print(f(26501365//H))