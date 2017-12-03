import math
from collections import defaultdict
import itertools


def one(data):
    col = int(math.sqrt(data)) + 1
    btm_right = col**2
    btm_left = btm_right - col + 1
    btm_middle = sum([btm_left, btm_right]) / 2
    horizon_mv = max([btm_middle, data]) - min([btm_middle, data])
    vert_mv = col // 2
    print(horizon_mv + vert_mv)


def two(data):
    i = j = 0
    grid = defaultdict(int)
    grid[(i, j)] = 1
    enws = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # east, north, west, south
    adjacents = list(itertools.product([0, 1, -1], repeat=2))
    adjacents.remove((0, 0))
    while True:
        print(grid)
        i += enws[0][0]
        j += enws[0][1]
        if (i == j or (i < 0 and -i == j) or (i > 0 and -i+1 == j)):
            enws = enws[1:] + enws[:1]
        new_val = sum([grid[(i+x[0], j+x[1])] for x in adjacents])
        if new_val > data:
            print(new_val)
            break
        grid[(i, j)] = new_val


data = int(open('input.txt').read().strip())
one(data)
two(data)
