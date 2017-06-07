from myfuns import divisors

bunList = set()
answer = 0

for i in range(1, 28123):
    if sum(divisors(i)) > 2 * i:
        bunList.add(i)
    if not any(i-a in bunList for a in bunList):
        answer += i

print(answer)

  # somDiv = [1] * (limit+1) # jusk 28123 inclus
  # for i in range(2, int(limit**.5)+1):
  #   somDiv[i*i] += i
  #   for k in range(i+1, limit//i+1):
  #       somDiv[k*i] += k+i
