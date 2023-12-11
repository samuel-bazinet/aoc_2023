def get_col(col_idx: int, array: list[list[str]]) -> list[str]:
    return [line[col_idx] for line in array]

def add_empty_col(array: list[str], idx: int):
    for i, line in enumerate(array):
        array[i] = line[:idx] + '.' + line[idx:]

file = open('input.txt')
lines = file.readlines()
file.close()

rows_to_add = []
empty_line = '.'*(len(lines[0])-1)

for (idx, line) in enumerate(lines):
    if '#' not in line:
        rows_to_add.append(idx)

cols_to_add = []

for i in range(len(lines[0])-1):
    if "#" not in get_col(i, lines):
        cols_to_add.append(i)

for (i, idx) in enumerate(rows_to_add):
    lines.insert(idx+i, empty_line)

for i, idx in enumerate(cols_to_add):
    add_empty_col(lines, i+idx)

galaxies: list[tuple[int, int]] = []

for (y, line) in enumerate(lines):
    for (x, char) in enumerate(line):
        if char == '#':
            galaxies.append((y, x))

shortest_paths: list[int] = []

for start in galaxies:
    for end in reversed(galaxies):
        if start == end:
            break
        shortest_paths.append(abs(start[0]-end[0]) + abs(start[1]-end[1]))

print(len(shortest_paths))
print(sum(shortest_paths))