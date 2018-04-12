class Solution(object):
    def getFactors(self, n):
        answer = []
        factors = self.factorsfun(n)
        if not factors:
            return []
        self.dfs(factors, answer, [], n, 0)
        return answer

    def dfs(self, factors, answer, path, n, index):
        product = reduce(lambda x,y:x*y, path, 1)
        if product == n:
            answer.append(path)
            return
        if product > n:
            return
        for i in range(index, len(factors)):
            self.dfs(factors, answer, path+[factors[i]], n, i)

    def factorsfun(self, n):
        factor_list = []
        # using xrange is faster than range
        for i in xrange(2, n):
            if not n%i:
                factor_list.append(i)
        return factor_list
