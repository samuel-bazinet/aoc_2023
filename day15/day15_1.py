file = open('input.txt', 'r')
lines = file.readlines()
file.close()

def hash_algo(cur_val: int, input: str) -> int:
    cur_val += ord(input)
    cur_val *= 17
    cur_val = cur_val % 256
    return cur_val

total = 0

line = lines[0].split(',')

for word in line:
    cur_val = 0
    for char in word.strip():
        cur_val = hash_algo(cur_val, char)
    total += cur_val

print(total)