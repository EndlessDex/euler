from myfuns import genFib
from itertools import count

x = genFib()

for i in count(1):
    y = next(x)
    if len(str(y)) >= 1000:
        print(i)
        break
