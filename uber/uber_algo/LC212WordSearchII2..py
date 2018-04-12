class Solution(object):
    def findWords(self, board, words):
        if not board or not words:
            return []
        trie = {}
        temp = []
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
                self.dfs(i, j, trie, temp, '', m, n, board)
        answer = []
        for each in temp:
            if each not in answer:
                answer.append(each)
        return answer

    def dfs(self, i, j, trie, temp, path, m, n, board):
        if '#' in trie:
            temp.append(path)
        if i < 0 or i >= m or j < 0 or j >= n:
            return
        if board[i][j] in trie:
            char = board[i][j]
            board[i][j] = '*'
            self.dfs(i+1, j, trie[char], temp, path+char, m, n, board)
            self.dfs(i-1, j, trie[char], temp, path+char, m, n, board)
            self.dfs(i, j+1, trie[char], temp, path+char, m, n, board)
            self.dfs(i, j-1, trie[char], temp, path+char, m, n, board)
            board[i][j] = char
