'''
打印所有的factor可以是负数，心态崩了估计就挂这了。。
'''
def getFactors(n):
    if 0 <= n <= 3:
        return []
    if n < 0:
        return getFactors(-n)
    pos_factors = factors(n)
    answer = []
    n = len(pos_factors)
    for i in range(n):
        answer.append(pos_factors[i])
    for i in range(n):
        answer.append(-pos_factors[i])
    return answer

def factors(n):
    answer = []
    for i in xrange(2, n):
        if n%i == 0:
            answer.append(i)
    return answer

answer = getFactors(-10)
print answer
