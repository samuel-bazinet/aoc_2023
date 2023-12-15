file = open('input.txt', 'r')
lines = file.readlines()
file.close()

def hash_algo(cur_val: int, input: str) -> int:
    cur_val += ord(input)
    cur_val *= 17
    cur_val = cur_val % 256
    return cur_val

def focusing_power(len_pow: int, box: int, pos_len: int) -> int:
    power = 1+box
    power *= pos_len
    power *= len_pow
    return power

total = 0
boxes: list[list[str]] = [[] for _ in range(256)]
lens: dict[str, int] = {}
box_pos: dict[str, int] = {}
line = lines[0].split(',')

for word in line:
    if '-' in word:
        split_word = word.split('-')[0]
        if split_word in box_pos and split_word in boxes[box_pos[split_word]]:
            boxes[box_pos[split_word]].remove(split_word)
        continue

    hash = 0
    
    split_word = word.split('=')
    for char in split_word[0]:
        hash = hash_algo(hash, char)
    
    box_pos[split_word[0]] = hash
    if split_word[0] in boxes[hash]:
        lens[split_word[0]] = int(split_word[-1])
    else:
        boxes[hash].append(split_word[0])
        lens[split_word[0]] = int(split_word[-1])

for (box, boxed_lens) in enumerate(boxes):
    for i, this_len in enumerate(boxed_lens):
        total += focusing_power(lens[this_len], box, i+1)

print(total)