from functools import cache
import heapq
from typing import Iterable

file = open('input.txt', 'r')
lines = file.readlines()
file.close()

lines = [[int(i) for i in line.strip()] for line in lines]

W = len(lines[0])-1
H = len(lines)-1


def answer_grid(visited: set[tuple[int, int]]):
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if (i, j) in visited:
                print('H', end='')
            else:
                print('.', end='')
        print()

def in_range(pos: tuple[int, int]) -> bool:
    return  0 <= pos[0] <= H and 0 <= pos[1] <= W

def get_neighbors(current_pos: tuple[int, int, int, tuple[int, int]]) -> Iterable[tuple[int, int, tuple[int, int]]]:
    for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if (-i, -j) == current_pos[3]:
            continue
        to_check = (current_pos[0] + i, current_pos[1] + j)
        if in_range(to_check):
            if current_pos[3] == (i, j):
                if current_pos[2] < 10:
                    yield (to_check[0], to_check[1], current_pos[2]+1, (i,j))
            else:
                if current_pos[2] > 3:
                    yield (to_check[0], to_check[1], 1, (i,j))

def reconstruct_path(came_from: dict[tuple[int, int], tuple[int, int]], current: tuple[int, int]):
    total_path = []
    while current in came_from.keys() and current not in total_path:
        
        total_path.insert(0, current)
        current = came_from[current]
    answer_grid(total_path)

def get_val(node: tuple[int, int, int, tuple[int, int]]) -> int:
    return lines[node[0]][node[1]]

def djikstra(target: tuple[int, int]) -> tuple[list[list[tuple[int, int, int, tuple[int, int]]]], dict[tuple[int, int], tuple[int, int]]]:
    start1 = (0, 0, 0, (1, 0))
    start2 = (0, 0, 0, (0, 1))
    visited = set()
    dist: dict[tuple[int, int, int, tuple[int, int]], int] = {start1: 0, start2:0}

    queue: list[tuple[int, int, int, tuple[int, int]]] = [(0, start1), (0, start2)]
    heapq.heapify(queue)
    
    while queue != []:
        _, u = heapq.heappop(queue)
        if u in visited:
            continue
        visited.add(u)
        if u[:2] == target:
            target = u
            break
        for neighbor in get_neighbors(u):
            if neighbor in visited:
                continue
            alt = dist[u] + get_val(neighbor[:2])
            if neighbor not in dist or alt < dist[neighbor]:
                dist[neighbor] = alt
                heapq.heappush(queue, (alt, neighbor))
    return dist[target]


result = djikstra((H, W))

print(result)
