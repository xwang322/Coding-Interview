class Solution(object):
    def solveNQueens(self, n):
        answer = []
        self.dfs(answer, n, [], [-1]*n, 0)
        return answer

    def dfs(self, answer, n, path, curr, index):
        if index == n:
            answer.append(path)
            return
        for i in range(n):
            curr[index] = i
            if self.checkValid(curr, index, n):
                temp = '.'*n
                self.dfs(answer, n, path+[temp[:i]+'Q'+temp[i+1:]], curr, index+1)

    def checkValid(self, curr, index, n):
        for i in range(index):
            if curr[i] == curr[index]:
                return False
            elif index-i == abs(curr[i]-curr[index]):
                return False
        return True
            
