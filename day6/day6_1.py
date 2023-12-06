RATE_OF_SPEED_INCREASE = 1 # 1 mm/s per sec

with open('input.txt', 'r') as file:
    lines = file.readlines()
    times = list(map(lambda x: int(x), list(filter( lambda x: x != '', lines[0].strip().split(':')[1].strip().split(' ')))))
    distances = list(map(lambda x: int(x), list(filter( lambda x: x != '', lines[1].strip().split(':')[1].strip().split(' ')))))

    print(times)
    print(distances)

    total = 1

    for (time, distance) in zip(times, distances):
        race_ways = 0
        for i in range(time):
            try_dis = i*(time-i)
            if try_dis > distance:
                race_ways += 1
        total *= race_ways

    print(total)