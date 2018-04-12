class Solution(object):
    def isValidSudoku(self, board):
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] != '.' and not self.isvalid(i, j, board):
                    return False
        return True

    def isvalid(self, x, y, board):
        m = len(board)
        n = len(board[0])
        for i in range(m):
            if board[i][y] == board[x][y] and i != x:
                return False
        for i in range(n):
            if board[x][y] == board[x][i] and i != y:
                return False
        for i in range(3):
            for j in range(3):
                if board[x/3*3+i][y/3*3+j] == board[x][y] and x/3*3+i != x and y/3*3+j != y:
                    return False
        return True