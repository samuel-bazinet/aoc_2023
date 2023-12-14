file = open('input.txt', 'r')
lines = file.readlines()
file.close()

def roll_north(cols: list[list[str]]) -> list[list[str]]:
    for col in cols:
        for i, _ in enumerate(col):
            while col[i] == 'O' and i > 0 and col[i-1] == '.':
                col[i-1], col[i] = col[i], col[i-1]
                i -= 1
    return cols

lines = [line.strip() for line in lines]

load = lambda x: len(lines)-x

cols = [[line[i] for line in lines] for i in range(len(lines))]

total_load = 0

for col in roll_north(cols):
    for i, element in enumerate(col):
        if element == 'O':
            total_load += load(i)

print(total_load)