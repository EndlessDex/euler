N = 1000
for b in range(N//2):
    for a in range(b):
        c = (a**2+b**2)**0.5
        if a+b+c == N:
            print((a, b, int(c)), int(a*b*c))
