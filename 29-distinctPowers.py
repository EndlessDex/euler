#%%
mine = set()
for a in range(2, 101):
    for b in range(2, 101):
        mine.add(a ** b)
print(len(mine))