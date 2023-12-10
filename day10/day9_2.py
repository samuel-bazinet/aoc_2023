from typing import Tuple, List

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


with open('practice4.txt', 'r') as file:
    lines = file.readlines()
    c_pos_str = '000|000'
    s_pos = (0, 0)
    found = False
    max_y = len(lines) - 1
    max_x = len(lines[0]) - 1
    n_lines = [0 for _ in range(max_y)]
    vertices: List[Tuple[int, int]] = []
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
    vertices.append(current)
    started = False
    direction = ''

    if s_pos[0] > 0:
        if lines[s_pos[0]-1][s_pos[1]] == '|' or lines[s_pos[0]-1][s_pos[1]] == '7' or lines[s_pos[0]-1][s_pos[1]] == 'F':
            current = (current[0]-1, current[1])
            direction = 'u'
            started = True
    if not started and s_pos[0] < max_x:
        if lines[s_pos[0]+1][s_pos[1]] == '|' or lines[s_pos[0]+1][s_pos[1]] == 'L' or lines[s_pos[0]+1][s_pos[1]] == 'J':
            current = (current[0]+1, current[1])
            direction = 'd'
            started = True
    if not started and s_pos[1] > 0:
        if lines[s_pos[0]][s_pos[1]-1] == '-' or lines[s_pos[0]][s_pos[1]-1] == 'F' or lines[s_pos[0]][s_pos[1]-1] == 'L':
            current = (current[0], current[1]-1)
            direction = 'l'
            started = True
    if not started and s_pos[0] < max_y:
        if lines[s_pos[0]][s_pos[1]+1] == '-' or lines[s_pos[0]][s_pos[1]+1] == '7' or lines[s_pos[0]][s_pos[1]+1] == 'J':
            current = (current[0], current[1]+1)
            direction = 'r'
            started = True

    vertices.append(current)

    next_coord = (-1, -1)
    #print(coord_str(s_pos))
    #print(direction)
    #print(coord_str(current))
    while next_coord != s_pos:
        direction = dir(direction, lines[current[0]][current[1]])
        #print(direction)
        next_coord = option_increment(current, direction)
        #print(lines[next_coord[0]][next_coord[1]])
        if next_coord != s_pos:
            vertices.append(next_coord)
        current = next_coord
        #print(coord_str(current))

    #print(vertices)

    enclosed = 0

    for i in range(max_y):
        l_cross = 0
        for j in range(max_x):
            if (i, j) in vertices:
                if (lines[i][j] == 'S' and lines[i][j+1] == '-') or lines[i][j] in ['F', 'L']:
                    n_lines[i] += 1
                elif lines[i][j] in ['J', '7']:
                    n_lines[i] += 1
                elif lines[i][j] == '|':
                    n_lines[i] += 1
                continue
        for j in range(max_x):
            if (i, j) in vertices:
                print('ol', i, j)
                if (lines[i][j] == 'S' and lines[i][j+1] == '-') or lines[i][j] in ['F', 'L']:
                    l_cross += 1
                elif lines[i][j] in ['J', '7']:
                    l_cross += 1
                elif lines[i][j] == '|':
                    l_cross += 1
                continue
            else:
                if l_cross % 2 != 0 and l_cross != n_lines[i]:
                    if n_lines[i]//2 % 2 == 0:
                        print(i, j)
                        enclosed += 1
                    else:
                        if not (l_cross +1) % 4 == 0:
                            enclosed += 1
    print(enclosed)