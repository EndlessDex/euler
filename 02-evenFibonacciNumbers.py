x = [1, 2]
while True:
    x.append(x[-1] + x[-2])
    if x[-1] > 4000000:
        x.pop()
        break
print(sum([i for i in x if i % 2 == 0]))
