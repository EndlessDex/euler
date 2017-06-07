@profile
def mine():
    from myfuns import divisors

    bunList = set()
    answer = 0

    for i in range(1, 28123):
        if sum(divisors(i)) > 2 * i:
            bunList.add(i)
        if not any((i-a in bunList) for a in bunList):
            answer += i

    print(answer)

@profile
def PE023(limit=28123):
    somDiv = [1] * (limit + 1)
    for i in range(2, int(limit**.5)+1):
        somDiv[i*i] += i
        for k in range(i+1, limit//i+1):
            somDiv[k*i] += k+i
    abondant, res = set(), 0
    ajout = abondant.add
    for n in range(1, limit+1):
        if somDiv[n] > n: ajout(n)
        if not any((n-a in abondant) for a in abondant): res += n
    return res


mine()
print(PE023())
