from collections import deque
from math import lcm

file = open('input.txt', 'r')
lines = file.readlines()
file.close()

# %
# need low pulse to toggle
#turn on -> high pulse
# turn off -> low pulse

# &
# rem type of most recent pulse rom each of connected mods (default low)
# sends high pulse if not all inputs are high (send low when all inputs are high)

def handle_pulse(pulse: int, comp: str) -> bool:
    result = False
    if comp == 'cs':
        for com in prev[comp]:
            if states[com] == 1:
                targets[com] = total
    if comp_tool[comp] == '%':
        if pulse == 0:
            states[comp] = 0 if states[comp] == 1 else 1
            pulse = states[comp]
        else:
            return result
    if comp_tool[comp] == '&':
            pulse = check_sources(comp)
            states[comp] = pulse
    for con_comp in connected_comp[comp]:
        queue.appendleft((pulse, con_comp))
        #print(comp, con_comp, pulse)
    while len(queue) != 0:
        pulse, con_comp = queue.pop()
        if con_comp in comp_tool:
            result = handle_pulse(pulse, con_comp)
        if result:
            return result
    return result

def check_sources(comp):
    all_high = True
    for com in prev[comp]:
        if states[com] == 0:
            all_high = False
    if all_high:
        pulse = 0
    else:
        pulse = 1
    return pulse

connected_comp: dict[str, list[str]] = {}

comp_tool: dict[str, str] = {}

states: dict[str, int] = {}

prev: dict[str, set[str]] = {}

queue = deque()

start = 'broadcaster'[1:]

for line in lines:
    line = line.split('->')
    connected_comp[line[0].strip()[1:]] = [i.strip() for i in line[1].split(',')]
    comp_tool[line[0].strip()[1:]] = line[0].strip()[0]
    states[line[0].strip()[1:]] = 0

for k, v in connected_comp.items():
    for item in v:
        if item not in prev:
            prev[item] = set()
        prev[item].add(k)

targets: dict[str, int] = {t:0 for t in prev['cs']}

total = 1
for i in range(5000):
    handle_pulse(0, start)
    total += 1

answer = 1
for i in targets.values():
    answer = lcm(answer, i)

print(answer)
