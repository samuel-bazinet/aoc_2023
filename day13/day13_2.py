file = open('input.txt', 'r')
lines = file.readlines()
file.close()

def find_num_diff_char(a: str, b: str) -> int:
    return sum( a[i] != b[i] for i in range(len(a)))

def check_rows_old(idx: int, pattern: list[str]) -> bool:
    i = idx
    #print(idx)
    while i >= 0 and (2*idx - i) < len(pattern)-1:
        #print(pattern[i], pattern[2*idx - i + 1])
        if pattern[i] != pattern[2*idx - i + 1]:
            return False
        i -= 1
    return True

def check_columns_old(idx: int, pattern: list[str]) -> bool:
    i = idx
    while i >= 0 and (2*idx - i) < len(pattern[0])-1:
        if get_col(i, pattern) != get_col(2*idx - i + 1, pattern):
            return False
        i -= 1
    return True

def check_rows(idx: int, pattern: list[str]) -> bool:
    smudged_used = False
    i = idx
    #print(idx)
    while i >= 0 and (2*idx - i) < len(pattern)-1:
        #print(pattern[i], pattern[2*idx - i + 1])
        a = pattern[i]
        b = pattern[2*idx - i + 1]
        if a != b:
            if find_num_diff_char(a, b) == 1:
                print(a, b)
                if not smudged_used:
                  i -= 1
                  smudged_used = True
                  continue  
            return False
        i -= 1
    if check_rows_old(idx, pattern):
        return False
    return True

def get_col(idx: int, pattern: list[str]) -> str:
    output = ''
    for line in pattern:
        output+= line[idx]
    return output

def check_columns(idx: int, pattern: list[str]) -> bool:
    smudged_used = False
    i = idx
    while i >= 0 and (2*idx - i) < len(pattern[0])-1:
        a = get_col(i, pattern)
        b = get_col(2*idx - i + 1, pattern)
        if a != b:
            if find_num_diff_char(a, b) == 1:
                print(a, b)
                if not smudged_used:
                  i -= 1
                  smudged_used = True
                  continue  
            return False
        i -= 1
    if check_columns_old(idx, pattern):
        return False
    return True

def find_reflection(pattern: list[str]):
    #print(pattern)
    for i in range(len(pattern)-1):
        if check_rows(i, pattern):
            return (i+1)*100
    for i in range(len(pattern[0])-1):
        if check_columns(i, pattern):
            return (i+1)
            
                

pattern = []
total = 0
for line in lines:
    if pattern != [] and len(line) < len(pattern[0]):
        result = find_reflection(pattern)
        print(result)
        total += result
        pattern = []
    if len(line.strip()) > 0: 
        pattern.append(line.strip())

result = find_reflection(pattern)
print(result)
total += result

print(total)