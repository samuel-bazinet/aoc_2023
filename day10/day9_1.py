from typing import Tuple
import networkx as nx

def option_increment(current: Tuple[int, int], direction: str) -> Tuple[int, int]:
    if direction == 'l':
        return (current[0], current[1]-1)
    elif direction == 'r':
        return (current[0], current[1] + 1)
    elif direction == 'd':
        return (current[0]+1, current[1])
    else:
        return (current[0]-1, current[1])


def dir(direction: str, option: str) -> str:
    if option == '-' or option == '|':
        return direction
    elif option == 'F':
        if direction == 'u':
            return 'r'
        else:
            return 'd'
    elif option == 'L':
        if direction == 'l':
            return 'u'
        else:
            return 'r'
    elif option == 'J':
        if direction == 'r':
            return 'u'
        else:
            return 'l'
    elif option == "7":
        if direction == 'u':
            return 'l'
        else:
            return 'd'


def coord_str(coord: Tuple[int, int]) -> str:
    return f'{str(coord[0]).zfill(3)}|{str(coord[1]).zfill(3)}'


with open('input.txt', 'r') as file:
    lines = file.readlines()
    c_pos_str = '000|000'
    s_pos = (0, 0)
    found = False
    max_y = len(lines) - 1
    max_x = len(lines[0]) - 1
    G = nx.Graph()
    for (i, line) in enumerate(lines):
        for (j, char) in enumerate(line):
            if char == 'S':
                s_pos = (i, j)
                c_pos_str = f'{str(i).zfill(3)}|{str(j).zfill(3)}'
                found = True
                break
        if found:
            break

    current = s_pos

    started = False
    direction = ''

    if s_pos[0] > 0:
        if lines[s_pos[0]-1][s_pos[1]] == '|' or lines[s_pos[0]-1][s_pos[1]] == '7' or lines[s_pos[0]-1][s_pos[1]] == 'F':
            G.add_edge(c_pos_str, coord_str((current[0]-1, current[1])))
            current = (current[0]-1, current[1])
            direction = 'u'
            started = True
    if not started and s_pos[0] < max_x:
        if lines[s_pos[0]+1][s_pos[1]] == '|' or lines[s_pos[0]+1][s_pos[1]] == 'L' or lines[s_pos[0]+1][s_pos[1]] == 'J':
            G.add_edge(c_pos_str, coord_str((current[0]+1, current[1])))
            current = (current[0]+1, current[1])
            direction = 'd'
            started = True
    if not started and s_pos[1] > 0:
        if lines[s_pos[0]][s_pos[1]-1] == '-' or lines[s_pos[0]][s_pos[1]-1] == 'F' or lines[s_pos[0]][s_pos[1]-1] == 'L':
            G.add_edge(c_pos_str, coord_str((current[0], current[1]-1)))
            current = (current[0], current[1]-1)
            direction = 'l'
            started = True
    if not started and s_pos[0] < max_y:
        if lines[s_pos[0]][s_pos[1]+1] == '-' or lines[s_pos[0]][s_pos[1]+1] == '7' or lines[s_pos[0]][s_pos[1]+1] == 'J':
            G.add_edge(c_pos_str, coord_str((current[0], current[1]+1)))
            current = (current[0], current[1]+1)
            direction = 'r'
            started = True

    next_coord = (-1, -1)
    #print(coord_str(s_pos))
    #print(direction)
    #print(coord_str(current))
    while next_coord != s_pos:
        direction = dir(direction, lines[current[0]][current[1]])
        #print(direction)
        next_coord = option_increment(current, direction)
        #print(lines[next_coord[0]][next_coord[1]])
        G.add_edge(coord_str(current), coord_str(next_coord))
        current = next_coord
        #print(coord_str(current))

    #print(G.nodes)
    print(nx.diameter(G))
