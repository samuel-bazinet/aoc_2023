import regex as re

numbers = []

num_to_digit = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

def find_matches(line: str):
    master_matches = []
    for key in num_to_digit.keys():
        matches = re.finditer(key, line)
        if matches:
            for match in matches:
                master_matches.append((key, match.start()))
    
    return list(sorted(master_matches, key= lambda x: x[1]))

with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        first = None
        second = None
        matches = find_matches(line)
        for match in matches:
            val = num_to_digit[match[0]]
            if first is None:
                first = val
                second = val
            else:
                second = val
        numbers.append(first*10+second)

#print(numbers)

print(sum(numbers))