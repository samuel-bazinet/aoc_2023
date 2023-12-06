from functools import reduce

with open('input.txt', 'r') as file:
    lines = file.readlines()
    times = list(filter( lambda x: x != '', lines[0].strip().split(':')[1].strip().split(' ')))
    distances = list(filter( lambda x: x != '', lines[1].strip().split(':')[1].strip().split(' ')))

    print(times)
    print(distances)

    total = 0

    time = 0
    distance = 0

    for (i, j) in zip(times, distances):
        time = time*10**len(i) + int(i)
        distance = distance * 10**len(j) + int(j)

    print(time)
    print(distance)

    
    for i in range(time):
        try_dis = i*(time-i)
        if try_dis > distance:
            total += 1

    print(total)