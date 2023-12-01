numbers = []

with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        first = None
        second = None
        for char in line:
            if first is None and char.isnumeric():
                first = int(char)
                second = int(char)
            elif char.isnumeric():
                second = int(char)
        numbers.append(first*10+second)

print(numbers)

print(sum(numbers))