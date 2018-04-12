class Solution(object):
    def findWords(self, board, words):
        if not board or not words:
            return []
        answer = []
        trie = {}
        for word in words:
            t = trie
            for char in word:
                if char not in t:
                    t[char] = {}
                t = t[char]
            t['#'] = '#'
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                self.dfs(answer, board, m, n, i, j, trie, '')
        final = []
        for each in answer:
            if each not in final:
                final.append(each)
        return final

    def dfs(self, answer, board, m, n, i, j, trie, path):
        if '#' in trie:
            answer.append(path)
            # every time you meet '#', there are at most 4 possible positions, so need to remove duplicate at the end
        if i < 0 or i > m-1 or j < 0 or j > n-1:
            return
        if board[i][j] != '*' and board[i][j] in trie:
            temp = board[i][j]
            board[i][j] = '*'
            self.dfs(answer, board, m, n, i+1, j, trie[temp], path+temp)
            self.dfs(answer, board, m, n, i-1, j, trie[temp], path+temp)
            self.dfs(answer, board, m, n, i, j+1, trie[temp], path+temp)
            self.dfs(answer, board, m, n, i, j-1, trie[temp], path+temp)
            board[i][j] = temp
