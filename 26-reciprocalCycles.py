maxLength = 0
value = 0

for i in range(999, 0, -1):
    if maxLength >= i:
        break
    if i % 2 and i % 5:
        for r in range(1, i):
            if (10**r - 1) % i == 0:
                maxLength = r
                value = i
                break
print(maxLength, value)
