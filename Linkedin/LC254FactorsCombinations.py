class Solution(object):
    def getFactors(self, n):
        if n <= 3:
            return []
        factors = self.factors(n)
        answer = []
        self.dfs(answer, factors, n, [])
        return answer

    def dfs(self, answer, factors, n, path):
        if n == 1:
            answer.append(path)
            return
        for index, factor in enumerate(factors):
            if n%factor == 0:
                self.dfs(answer, factors[index:], n/factor, path+[factor])

    def factors(self, n):
        answer = []
        for i in xrange(2, n):
            if n%i == 0:
                answer.append(i)
        return answer
