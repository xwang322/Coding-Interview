class Solution(object):
    def exist(self, board, word):
        if not board:
            return False
        answer = False
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, m, n, i, j):
                    answer = True
        return answer
    
    def dfs(self, board, word, m, n, i, j):
        if not word:
            return True
        if i < 0 or i > m-1 or j < 0 or j > n-1:
            return False
        if board[i][j] == word[0]:
            temp = board[i][j]
            board[i][j] = '*'
            answer = self.dfs(board, word[1:], m, n, i+1, j) or self.dfs(board, word[1:], m, n, i-1, j) or self.dfs(board, word[1:], m, n, i, j+1) or self.dfs(board, word[1:], m, n, i, j-1)
            board[i][j] = temp
            return answer
        else:
            return False