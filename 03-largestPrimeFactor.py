from myfuns import genPrimes
N = 600851475143

x = genPrimes()

while N != 1:
    i = next(x)
    while N % i == 0:
        N /= i

print(i)
