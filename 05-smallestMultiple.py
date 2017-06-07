high = 20
n = high
while n > 0:
    for i in range(1, high + 1):
        if n % i != 0:
            break
        elif i == high:
            print(n)
            n = -high
            break
    n += high

# from myfuns import genPrimes
# from math import log

# x = genPrimes()
# lcm, p = 1, 0
# while p < 20:
#     p = next(x)
#     lcm *= p ** int(log(20,p))
# print(lcm)
