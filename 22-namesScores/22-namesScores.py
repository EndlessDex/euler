with open('data.txt') as file:
    namesStr = file.read()

answer = 0
for index, name in enumerate(sorted(namesStr.replace('"', '').split(','))):
    answer += (index + 1) * sum([ord(i) - 64 for i in name])
print(answer)
