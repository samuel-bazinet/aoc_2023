import threading


def verify_line(line: str, expected: list[int]) -> bool:
    b = 0
    b_set = 0
    b_count = 0
    for idx, char in enumerate(line):
        if b_set >= len(expected):
            if '#' not in line[idx:]:
                return True
            else:
                return False
        if char == '#':
            b += 1
            b_count += 1
        else:
            if b > 0:
                if b != expected[b_set]:
                    return False
                b_set += 1
                b = 0
    if b > 0:
        if b != expected[b_set]:
            return False
    if (b_set != len(expected) and b_set != len(expected) -1 ) or b_count != sum(expected):
        return False
    return True

def count_p_b(option: str, expected: int) -> bool:
    b_count = 0
    for char in option:
        if char == '1':
            b_count += 1
    return b_count == expected

class myThread (threading.Thread):
    def __init__(self, input, index):
        threading.Thread.__init__(self)
        self.input = input
        self.index = index
        self.output = 0
    
    def run(self):
        self.output, self.index = main_loop(self.input, self.index)

def main_loop(line : list, indx: int) -> tuple[int, int]:
    line_t = 0
    q_count = 0
    q_pos = []
    b_count = 0
    expected = [int(i) for i in line[1]]
    expected_b_count = sum(expected)
    for idx, char in enumerate(line[0]):
        if char == '?':
            q_count += 1
            q_pos.append(idx)
        elif char == '#':
            b_count += 1
    
    comb_len = len(bin(2**q_count)[2:])-1
    for i in range(2**q_count):
        t_line = line[0]
        option = bin(i)[2:].zfill(comb_len)
        if not count_p_b(option, expected_b_count-b_count):
            continue
        for idx, pos in enumerate(q_pos):
            t_line = t_line[:pos] + ('.' if option[idx] == '0' else '#') + t_line[pos+1:]
        if verify_line(t_line, expected):
            line_t += 1
    return line_t, indx

file = open('input.txt')
lines = file.readlines()
file.close()

lines = [line.strip().split(' ') for line in lines]
lines = [(line[0], line[1].strip().split(',')) for line in lines]

o_l_t = [0 for _ in lines]

threads: list[myThread] = []

for idx, line in enumerate(lines):
    thread = myThread(line, idx)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
    o_l_t[thread.index] = thread.output

print(o_l_t)


lines = [(((line[0]+'?')*2)[:-1], line[1]*2) for line in lines]

s_l_t = [0 for _ in lines]
threads: list[myThread] = []

for idx, line in enumerate(lines):
    thread = myThread(line, idx)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
    s_l_t[thread.index] = thread.output

print(s_l_t)

total = 0

for a, b in zip(o_l_t, s_l_t):
    arr = a*((b//a)**4)
    total += arr

print(total)