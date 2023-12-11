def get_col(col_idx: int, array: list[list[str]]) -> list[str]:
    return [line[col_idx] for line in array]

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

galaxies: list[tuple[int, int]] = []

for (y, line) in enumerate(lines):
    for (x, char) in enumerate(line):
        if char == '#':
            galaxies.append((y, x))

shortest_paths: list[int] = []

### Look for number of empty rows and cols between coord and add factor

factor = 1000000-1

for start in galaxies:
    for end in reversed(galaxies):
        n_rows = 0
        n_cols = 0
        if start == end:
            break
        for row in rows_to_add:
            if (row > start[0] and row < end[0]) or (row > end[0] and row < start[0]):
                n_rows += 1
        
        for col in cols_to_add:
            if (col > start[1] and col < end[1]) or (col > end[1] and col < start[1]):
                n_cols += 1
        #print(start, end)
        #print(n_rows, n_cols)
        #print(abs(start[0]-end[0]) + abs(start[1]-end[1]))
        #print(abs(start[0]-end[0]) + abs(start[1]-end[1]) + n_rows*factor + n_cols*factor)
        shortest_paths.append(abs(start[0]-end[0]) + abs(start[1]-end[1]) + n_rows*factor + n_cols*factor)

print(len(shortest_paths))
print(sum(shortest_paths))