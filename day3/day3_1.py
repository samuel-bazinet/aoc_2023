import re
from typing import List

class Number:
    value: int
    pos_start_x: int
    pos_end_x: int
    pos_y: int
    
    def __init__(self, value, pos_start_x, post_end_x, pos_y):
        self.value = value
        self.pos_start_x = pos_start_x
        self.pos_end_x = post_end_x
        self.pos_y = pos_y

class Symbol:
    symbol: str
    pos_x: int
    pos_y: int

    def __init__(self, symbol, x, y):
        self.symbol = symbol
        self.pos_x = x
        self.pos_y = y 

NUMBER_PATTERN = r'\d+'
SYMBOL_PATTERN = r'(?!([0-9]|\.)).'

numbers: List[Number] = []
symbols: List[Symbol] = []

with open('input.txt', 'r') as file:
    lines = file.readlines()
    for (idx, line) in enumerate(lines):
        matches = re.finditer(NUMBER_PATTERN, line)
        for m in matches:
            numbers.append(Number(int(m.group()), m.start(), m.end()-1, idx))
        
        matches = re.finditer(SYMBOL_PATTERN, line)
        for m in matches:
            symbols.append(Symbol(m.group(), m.start(), idx))

total = 0

for number in numbers:
    for symbol in symbols:
        if symbol.pos_x >= number.pos_start_x -1 and symbol.pos_x <= number.pos_end_x + 1 and symbol.pos_y >= number.pos_y -1 and symbol.pos_y <= number.pos_y + 1:
            #print(number.value, number.pos_start_x, number.pos_end_x, number.pos_y)
            total += number.value
            break


print(f'total: {total}')