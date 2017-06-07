digits = 3
i = 0
for x in range(10 ** digits):
    for y in range(10 ** digits):
        p = str(x * y)
        if p == p[::-1] and int(p) > i:
            i = int(p)
print(i)
