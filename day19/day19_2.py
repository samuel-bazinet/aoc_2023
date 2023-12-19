def gen_check(is_greater: bool, check: int, code: int):
    if is_greater:
        def fun(input: dict[str, tuple[int, int]]) -> dict[int, tuple[int, int]]:
            new_input = input.copy()
            new_input[code] = (max(input[code][0], check+1), input[code][1])
            return new_input
    else:
         def fun(input: dict[str, tuple[int, int]]) -> dict[int, tuple[int, int]]:
            new_input = input.copy()
            new_input[code] = (input[code][0], min(input[code][1], check-1))
            return new_input
    return fun

def process_gates(gates: list[str]) -> list:
    new_gates: list[tuple] = []
    for gate in gates:
        if ':' in gate:
            gate = gate.split(':')
            is_greater = '>' in gate[0]
            check = gate[0].split('>') if is_greater else gate[0].split('<')

            new_gates.append((gen_check(is_greater, int(check[1]), xmas_int[check[0]]), gate[1]))
        else:
            new_gates.append((lambda input: input.copy(), gate))
    return new_gates

# list[tuple[dict[str, (min, max)], dest]]
# maybe have the check modify the range to get the valid values?

xmas_int = {
    'x':0,
    'm':1,
    'a':2,
    's':3
}

file = open('input.txt', 'r')
lines = file.readlines()
file.close()

tasks = {}

def update_input(input, result):
    for i in range(4):
        if input[i] != result[i]:
            if input[i][0] == result[i][0]:
                input[i] = (result[i][1]+1, input[i][1])
            else:
                input[i] = (input[i][0], result[i][0]-1)
    return input


def main_recurse(input: dict[str, tuple[int, int]], task: str) -> set[tuple[tuple[int, int], tuple[int, int], tuple[int, int], tuple[int, int]]]:
    global tasks
    gates = tasks[task]
    out = set()
    for gate in gates:
        result = gate[0](input)
        input = update_input(input, result)
        if gate[1] == 'A':
            out.add((result[0], result[1], result[2], result[3]))
        elif gate[1] != 'R':
            out = out.union(main_recurse(result, gate[1]))
    return out

for line in lines:
    line = line.strip()
    if len(line) == 0:
        break
    line = line.split('{')
    name = line[0]
    gates = line[1][:-1]
    gates = [cond for cond in gates.split(',')]
    gates = process_gates(gates)
    tasks[name] = gates

# check the inputs of all tasks/gates
# check how many x, m, a, s can go through
# then multiply them together

combs = 0

start_input = {i: (1, 4000) for i in range(4)}

result = main_recurse(start_input, 'in')

print(len(result))

# Try to make a list of list of tuples and then reduce it so that you get all the ranges that you need


for r in result:
    set_comb = 1
    for i in range(4):
        set_comb *= (r[i][1]-r[i][0])+1
    combs += set_comb

print(combs)

#10830254066823043
#199828226137500
#199985791895500
#188773710904828
#201772702170510
#201612981392240
#201772702170510
#951866610240
#167010937327821
#167409079868000