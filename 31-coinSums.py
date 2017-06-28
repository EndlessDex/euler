#%%
coins = [1, 2, 5, 10, 20, 50, 100, 200]
solutions = [1] + [0]*200

for coin in  coins:
    for i in range(coin, 201):
        solutions[i] += solutions[i - coin]

print(solutions[-1])