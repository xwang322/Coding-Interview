class Solution(object):
    def isValidSudoku(self, board):
        m = len(board)
        n = len(board[0])
        if not self.horizontalValid(board, m, n):
            return False
        if not self.verticalValid(board, m, n):
            return False
        if not self.diagonalValid(board, m, n):
            return False
        return True
        
    def horizontalValid(self, board, m, n):
        for i in range(m):
            temp = set()
            for j in range(n):
                if board[i][j] != '.':
                    if board[i][j] in temp:
                        return False
                    else:
                        temp.add(board[i][j])
        return True
    
    def verticalValid(self, board, m, n):
        for i in range(n):
            temp = set()
            for j in range(m):
                if board[j][i] != '.':
                    if board[j][i] in temp:
                        return False
                    else:
                        temp.add(board[j][i])
        return True

    def diagonalValid(self, board, m, n):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                temp = set()
                temp_board = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                for each in temp_board:
                    if each != '.':
                        if each in temp:
                            return False
                        else:
                            temp.add(each)
        return True