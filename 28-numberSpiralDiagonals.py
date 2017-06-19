#%% Make Spiral
import numpy as np
turn = {(-1, 0): (0, 1),
        (0, 1): (1, 0),
        (1, 0): (0, -1),
        (0, -1): (-1, 0)}

def makeSpiral(n):
    if n % 2 == 0:
        raise ValueError('Spiral size can not be even.')
    spiral = np.zeros((n, n))
    cursor = (n//2 + 1, n//2)
    direction = (0, -1)

    for i in range(1, spiral.size + 1):
        while True:
            temp = tuple(sum(x) for x in zip(cursor, turn[direction]))
            if spiral[temp] == 0:
                direction = turn[direction]
                cursor = temp
                break
            else:
                direction = [cur for cur, nxt in turn.items() if nxt == direction][0]
        spiral[cursor] = i
    return spiral
#%% solve problem
spi = makeSpiral(1001)
print(sum(np.diag(spi) + np.diag(np.fliplr(spi))) - 1)