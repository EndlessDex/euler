from itertools import count


# Postpone Method - based on Will Ness
def genPrimes(mer=False):
    yield 2
    yield 3
    yield 5
    yield 7
    D = {}
    ps = genPrimes()
    p = next(ps) and next(ps)
    q = p ** 2
    for c in count(9, 2):
        s = D.pop(c, None)
        if s:
            pass
        elif c < q:
            yield c
            continue
        else:
            s = count(q + p*2, p*2)
            p = next(ps)
            q = p ** 2
        for m in s:
            if m not in D:
                break
        D[m] = s

# Non-Postpone Method - based on David Eppstein
# def genPrimes():
#     yield 2
#     D = {}
#     for q in count(3, 2):
#         p = D.pop(q, None)
#         if p:
#             x = p + q
#             while x in D:
#                 x += p
#             D[x] = p
#         else:
#             D[q * q] = 2 * q
#             yield q


def genTris():
    for i in count(1):
        yield i * (i + 1) // 2


def primeFactors(N):
    factors = []
    for p in genPrimes():
        if p ** 2 > N:
            factors.append((N, 1))
            break
        i = 0
        while N % p == 0:
            i += 1
            N //= p
        if i:
            factors.append((p, i))
        if N == 1: break
    return factors


def divisors(N):
    facs = primeFactors(N)
    divs = set([1])
    for p, i in facs:
        temp = set()
        for d in divs.copy():
            for e in range(i+1):
                temp.add(d * p**e)
        divs = temp
    return divs
