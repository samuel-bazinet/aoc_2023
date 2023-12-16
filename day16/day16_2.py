import sys
from functools import cache


class Tile:
    content: str
    visited: int
    last_s_d: list[str]

    def __init__(self, content: str):
        self.content = content
        self.visited = 0
        self.last_s_d = []

    def __repr__(self):
        return f"{self.content} {self.visited}"

    def hit(self, source_dir: str) -> list[str]:
        self.visited += 1
        if source_dir in self.last_s_d:
            return ['e']
        self.last_s_d.append(source_dir)
        if self.content == '-':
            if source_dir in ['u', 'd']:
                return ['l', 'r']
        elif self.content == '|':
            if source_dir in ['l', 'r']:
                return ['u', 'd']
        elif self.content == '/':
            return [handle_slash(source_dir)]
        elif self.content == '\\':
            return [handle_backslash(source_dir)]
        return [source_dir]


@cache
def handle_slash(source_dir: str) -> str:
    if source_dir == 'u':
        return 'r'
    elif source_dir == 'd':
        return 'l'
    elif source_dir == 'l':
        return 'd'
    else:
        return 'u'


@cache
def handle_backslash(source_dir: str) -> str:
    if source_dir == 'u':
        return 'l'
    elif source_dir == 'd':
        return 'r'
    elif source_dir == 'l':
        return 'u'
    else:
        return 'd'


sys.setrecursionlimit(100000000)

file = open('practice.txt', 'r')
lines = file.readlines()
file.close()

tiles: list[list[Tile]] = [[] for _ in range(len(lines))]

for i, line in enumerate(lines):
    for char in line.strip():
        tiles[i].append(Tile(char))


def reset_and_go(direction: str, pos: tuple[int, int]) -> int:
    for i in tiles:
        for tile in i:
            tile.visited = 0
            tile.last_s_d = []
    main_recurse(direction, pos)

    visited = 0

    for i in tiles:
        for tile in i:
            if tile.visited > 0:
                visited += 1
    return visited


def main_recurse(direction: str, pos: tuple[int, int]):
    # (row, col)
    next_dir = tiles[pos[0]][pos[1]].hit(direction)
    if next_dir[0] == 'e':
        return
    for dir in next_dir:
        if dir == 'u' and pos[0] > 0:
            main_recurse(dir, (pos[0]-1, pos[1]))
        elif dir == 'd' and pos[0] < len(tiles)-1:
            main_recurse(dir, (pos[0]+1, pos[1]))
        elif dir == 'l' and pos[1] > 0:
            main_recurse(dir, (pos[0], pos[1]-1))
        elif dir == 'r' and pos[1] < len(tiles[0]) - 1:
            main_recurse(dir, (pos[0], pos[1]+1))

best = 0

for i in range(len(tiles[0])-1):
    best = max(best, reset_and_go('d', (0,i)))
    best = max(best, reset_and_go('u', (len(tiles)-1, i)))

for i in range(len(tiles[0])-1):
    best = max(best, reset_and_go('r', (i,0)))
    best = max(best, reset_and_go('l', (i, len(tiles)-1)))

print(best)
