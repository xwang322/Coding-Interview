class Solution(object):
    def solveSudoku(self, board):
        if not board or not board[0]:
            return False
        self.board = board
        self.solve()
        
    def isValid(self, row, col, fill):
        rowSquare = row - row%3
        colSquare = col - col%3
        for i in range(9):
            if self.board[row][i] == fill:
                return False
            if self.board[i][col] == fill:
                return False
        for i in range(rowSquare, rowSquare+3):
            for j in range(colSquare, colSquare+3):
                if self.board[i][j] == fill:
                    return False
        return True
    
    def findOneBlank(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == '.':
                    return i, j
        return -1, -1
    
    def solve(self):
        row, col = self.findOneBlank()
        if row == -1 and col == -1:
            return True
        nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for num in nums:
            if self.isValid(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                else:
                    self.board[row][col] = '.'
        return False
        
        