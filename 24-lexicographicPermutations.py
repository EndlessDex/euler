from math import factorial as f
objs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
out = []
target = 1000000 - 1

for i in range(len(objs) - 1, -1, -1):
    index = target // f(i)
    out.append(objs.pop(index))
    target -= f(i) * index

print(*out, sep='')
