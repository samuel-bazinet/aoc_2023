def gen_check(is_greater: bool, check: int, code: str):
    if is_greater:
        return lambda input: input[code] > check
    else:
        return lambda input: input[code] < check

def process_gates(gates: list[str]) -> list:
    new_gates: list[tuple] = []
    for gate in gates:
        if ':' in gate:
            gate = gate.split(':')
            is_greater = '>' in gate[0]
            check = gate[0].split('>') if is_greater else gate[0].split('<')
            new_gates.append((gen_check(is_greater, int(check[1]), check[0]), gate[1]))
        else:
            new_gates.append((lambda _: True, gate))
    return new_gates

        
file = open('input.txt', 'r')
lines = file.readlines()
file.close()

tasks = {}
inputs: list[dict[str, int]] = []


def main_recurse(input: dict[str, int], task: str) -> str:
    global tasks
    gates = tasks[task]
    for gate in gates:
        if gate[0](input):
            if gate[1] not in ['R', 'A']:
                return main_recurse(input, gate[1])
            else:
                return gate[1]
    print('failed')
    return ''

done_tasks = False
for line in lines:
    line = line.strip()
    if len(line) == 0:
        done_tasks = True
        continue
    if not done_tasks:
        line = line.split('{')
        name = line[0]
        gates = line[1][:-1]
        gates = [cond for cond in gates.split(',')]
        gates = process_gates(gates)
        tasks[name] = gates
    else:
        line = line.strip('{}').split(',')
        input = {}
        for i in line:
            i = i.split('=')
            input[i[0]] = int(i[1])
        inputs.append(input)

accepted = []

for input in inputs:
    result = main_recurse(input, 'in')
    if result == 'A':
        accepted.append(input['x'] + input['m'] + input['a'] + input['s'])

print(sum(accepted))