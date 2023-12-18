from functools import cache
import heapq

file = open('practice.txt', 'r')
lines = file.readlines()
file.close()

lines = [[int(i) for i in line.strip()] for line in lines]

class Node:
    pos: tuple[int, int]
    f_score: float
    g_score: float
    value: int
    source: str

    def __init__(self, pos: tuple[int, int], value: int, f_score = float('inf'), g_score = float('inf'), source = ''):
        self.pos = pos
        self.value = value
        self.f_score = f_score
        self.g_score = g_score
        self.source = source

    def __lt__(self, other):
        return self.f_score < other.f_score
    
    def __gt__(self, other):
        return self.f_score > other.f_score
    
    def __eq__(self, other):
        return self.pos == other.pos

    def __repr__(self) -> str:
        return f'{self.pos} {self.value}'

    def __hash__(self):
        return hash(self.pos)


def answer_grid(visited: set[tuple[int, int]]):
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if (i, j) in visited:
                print('H', end='')
            else:
                print('.', end='')
        print()

def get_neighbors(current_pos: tuple[int, int], came_from: dict[tuple[int, int], tuple[int, int]]) -> list[tuple[int, int]]:
    neighbors = []
    if current_pos not in came_from:
        if current_pos[1] < len(lines[0])-1:
            neighbors.append((current_pos[0], current_pos[1]+1))
        if current_pos[0] < len(lines)-1:
            neighbors.append((current_pos[0]+1, current_pos[1]))
        if current_pos[0] > 0:
            neighbors.append((current_pos[0]-1, current_pos[1]))
        if current_pos[1] > 0:
            neighbors.append((current_pos[0], current_pos[1]-1))
    else:
        if current_pos[1] < len(lines[0])-1 and (current_pos[0], current_pos[1]+1) != came_from[current_pos]:
            neighbors.append((current_pos[0], current_pos[1]+1))
        if current_pos[0] < len(lines)-1 and (current_pos[0]+1, current_pos[1]) != came_from[current_pos]:
            neighbors.append((current_pos[0]+1, current_pos[1]))
        if current_pos[0] > 0 and (current_pos[0]-1, current_pos[1]) != came_from[current_pos]:
            neighbors.append((current_pos[0]-1, current_pos[1]))
        if current_pos[1] > 0 and (current_pos[0], current_pos[1]-1) != came_from[current_pos]:
            neighbors.append((current_pos[0], current_pos[1]-1))
    return neighbors

def does_path_have_three_ir(current: tuple[int, int], came_from: dict[tuple[int, int], tuple[int, int]], lr: tuple[int, int] = (-1, -1)) -> bool:
    if lr[0] == 4:
        return True
    elif lr[1] == 4:
        return True
    
    if current in came_from.keys():
        next = came_from[current]
        if next[0] == current[0]:
            return does_path_have_three_ir(next, came_from, (lr[0]+1, 0))
        elif next[1] == current[1]:
            return does_path_have_three_ir(next, came_from, (0, lr[1] + 1))
    return False

@cache
def h(goal: Node, current: tuple[int, int]) -> int:
    v_dist = goal.pos[0] - current[0]
    h_dist = goal.pos[1] - current[1]
    score = 0
    for j in range(current[1], goal.pos[1]):
        score += lines[current[0]][j]
    for i in range(current[0], goal.pos[1]):
        score += lines[i][-1]
    return score

def reconstruct_path(came_from: dict[tuple[int, int], tuple[int, int]], current: tuple[int, int]):
    total_path = []
    while current in came_from.keys() and current not in total_path:
        
        total_path.insert(0, current)
        current = came_from[current]
    answer_grid(total_path)

def a_star(start: Node, goal: Node) -> float:
    open_set = [start]
    heapq.heapify(open_set)

    came_from: dict[tuple[int, int], tuple[int, int]] = {}

    options = [[Node((i, j), lines[i][j]) for j in range(len(lines[0]))] for i in range(len(lines))]

    while open_set != []:
        current = heapq.heappop(open_set)
        
        if current == goal:
            reconstruct_path(came_from, current.pos)
            return current.g_score
        
        # each neighbors
        for neighbor in get_neighbors(current.pos, came_from):
            tent_g_score = current.g_score + lines[neighbor[0]][neighbor[1]]
            if tent_g_score < options[neighbor[0]][neighbor[1]].g_score:
                came_from[neighbor] = current.pos
                if does_path_have_three_ir(neighbor, came_from):
                    continue
                options[neighbor[0]][neighbor[1]].g_score = tent_g_score
                options[neighbor[0]][neighbor[1]].f_score = tent_g_score + h(goal, neighbor)
                if options[neighbor[0]][neighbor[1]] not in open_set:
                    heapq.heappush(open_set, options[neighbor[0]][neighbor[1]])

    print("failed")
    return 0


visited: set[tuple[int, int]] = set()
visited.add((0,0))
cost = 0
current_pos = (0, 0)

print(a_star(Node((0,0), 0, 0, 0), Node((len(lines)-1, len(lines[0])-1), lines[-1][-1])))