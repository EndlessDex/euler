from myfuns import divisors


def d(n):
    return sum(divisors(n)[:-1])

aNums = []

for a in range(10000):
    b = d(a)
    if b < a:
        continue
    if a == d(b) and a != b:
        aNums.extend([a, b])

print(aNums, sum(aNums))
