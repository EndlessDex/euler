#%% Create prime repo
#==============================================================================
# import pickle
# from myfuns import genPrimes
#
# x = genPrimes()
# out = set()
# for _ in range(10000000):
#     out.add(next(x))
#
#
# pickle.dump(out, open('tenMillionPrimes.p', 'wb'))
# print('done')
#
#==============================================================================
#%% Import Modules and load primes
from itertools import count
from pickle import load as pkLoad
primeSet = pkLoad(open('tenMillionPrimes.p', 'rb'))
def f(a, b):
    for n in count():
        p = n**2 + a*n + b
        if p <= 0:
            return n
        if p not in primeSet:
            return n

#%% Solve problem
maxPrimes = 0
vals = (0, 0)

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        cur = f(a, b)
        if cur > maxPrimes:
            maxPrimes = cur
            vals = (a, b)
print(vals)