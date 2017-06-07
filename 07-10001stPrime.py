from myfuns import genPrimes

N = 10001
p = genPrimes()
[next(p) for _ in range(N-1)]
print(next(p))
