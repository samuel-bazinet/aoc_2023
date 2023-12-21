from collections import deque

file = open('input.txt', 'r')
lines = file.readlines()
file.close()

lines = [[char for char in line.strip()] for line in lines]

starting_point = (-1, -1)

H = len(lines)
W = len(lines[0])

def is_valid(coord: tuple[int, int]) -> bool:
    return 0 <= coord[0] <H and 0 <= coord[1] < W and lines[coord[0]][coord[1]] != "#" 

def get_neighbours(coord: tuple[int, int]) -> list[tuple[int, int]]:
    for i in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_coord = (coord[0] + i[0], coord[1] + i[1])
        if is_valid(new_coord):
            yield new_coord

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == 'S':
            starting_point = (i, j)

# Idea: use bfs and a new queue for each step
new_queue = deque()
new_queue.append(starting_point)


for i in range(64):
    queue = new_queue
    new_queue = deque()
    while len(queue) > 0:
        el = queue.pop()
        for coord in get_neighbours(el):
            if coord not in new_queue:
                new_queue.append(coord)

print(len(new_queue))
