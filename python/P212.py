class TriNode(object):
    def __init__(self):
        self.word = None
        self.children = {}
        
class Trie(object):
    def __init__(self):
        self.root = TriNode()
    
    def insert(self, word):
        root = self.root
        for char in word:
            root = root.children.setdefault(char, TriNode())
        root.word = word



class Solution(object):
    def findWords(self, board, words):
        if not board:
            return []
        tree = Trie()
        [tree.insert(word) for word in words]
        answer = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.search(board, i, j, tree.root, answer)
        return answer
    
    def search(self, board, i, j, root, answer):
        char = board[i][j]
        if not (char and char in root.children):
            return
        board[i][j] = '#'
        root = root.children[char]
        if root.word:
            answer.append(root.word)
            root.word = None
        for x, y in ((-1, 0),(1, 0),(0, 1),(0, -1)):
            ii,jj = i+x, j+y
            if 0<=ii<len(board) and 0<=jj<len(board[0]):
                self.search(board, ii, jj, root, answer)
        board[i][j] = char
        