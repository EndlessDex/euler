with open('data.txt') as file:
    triStr = file.read()

triArr = [[int(num) for num in row.split()] for row in triStr.strip('\n').split('\n')]

for level in range(len(triArr) - 2, -1, -1):
    for index, _ in enumerate(triArr[level]):
        triArr[level][index] += max(triArr[level+1][index],
                                    triArr[level+1][index+1])
print(triArr[0][0])
