from myfuns import primeFactors
from myfuns import genTris
from numpy import prod
# from myfuns import divisors

# 30% faster
for x in genTris():
    if prod([i+1 for p, i in primeFactors(x)]) > 500:
        break

# for x in genTris():
#     if len(divisors(x)) > 500:
#         break
