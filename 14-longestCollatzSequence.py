#from sys import argv
memo = {1: 1}

@profile
def collatz(n):
    if n in memo:
        return memo[n]
    elif n % 2 is not 0:
        memo[n] = 2 + collatz((3 * n + 1) // 2)
    else:
        memo[n] = 1 + collatz(n // 2)
    return memo[n]


maxA = -1
maxS = -1
limit = 1000000  # int(argv[1])
lowerLimit = limit // 2 + 1 if limit % 2 == 0 else limit // 2
for i in range(lowerLimit, limit, 2):
    cur = collatz(i)
    if cur > maxA:
        maxA = cur
        maxS = i

print(maxS, '->', maxA)
