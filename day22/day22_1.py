
file = open('practice.txt', 'r')
lines = file.readlines()
file.close()

# input is postion of bricks (x, y, z)
# after ~ is the other end of the brick

bricks: list[list[list[int]]] = []
max_z = 0

def settle_bricks(bricks: list[list[list[int]]]):
    taken: list[list[list[list[int]]]] = [[] for _ in max_z]
    for brick in bricks:
        taken[brick[-1][-1]].append((range(brick[0][0], brick[1][0] + 1), range(brick[0][1], brick[1][1] + 1), range(brick[0][2], brick[1][2] + 1)))
    
    for layer in reversed(taken[1:]):
        for brick in layer:
            
        # check if there is nothing below, move below
        ...
                


for line in lines:
    line = line.strip().split('~')
    s = line[0].split(',')
    s = list(map(lambda x: int(x), s))
    e = line[1].split(',')
    e = list(map(lambda x: int(x), e))
    max_z = max(max_z, e[-1])
    bricks.append([s, e])

settle_bricks(bricks)

print(len(bricks))
