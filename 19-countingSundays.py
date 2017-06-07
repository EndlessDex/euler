from calendar import weekday as w
print(len([1 for y in range(1901, 2001) for m in range(1, 13) if w(y, m, 1) is 6]))
