from myfuns import genPrimes

x = genPrimes()
a = next(x)
s = 0
while a < 2000000:
    s += a
    a = next(x)

print(s)
