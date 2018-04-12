class Solution(object):
    def getPermutation(self, n, k):
        if n == 1:
            return '1'
        answer = ''
        self.templist = []
        self.listreturn([i+1 for i in range(n)], n, k)
        return answer.join(self.templist)
        
    def listreturn(self, listtodo, n, k):
        if n == 1:
            self.templist.append(str(listtodo[0]))
            return
        i = 1
        while i*self.getnumber(n-1) <= k:
            if i*self.getnumber(n-1) < k:
                i += 1
            else:
                break
        self.templist.append(str(listtodo[i-1]))
        self.listreturn(sorted(listtodo[:i-1]+listtodo[i:]), n-1, k-(i-1)*self.getnumber(n-1))
                       
        
    def getnumber(self, n):
        if n == 1:
            return 1
        return n*self.getnumber(n-1)
        