
class Solution(object):
    def isValidSudoku(self, board):
        if not board or not board[0]:
            return False
        m = len(board)
        n = len(board[0])
        return self.rowcheck(board, m, n) and self.colcheck(board, m, n) and self.squarecheck(board, m, n)

    def rowcheck(self, board, m, n):
        for i in range(9):
            temp = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in temp:
                        return False
                    temp.add(board[i][j])
        return True

    def colcheck(self, board, m, n):
        for i in range(9):
            temp = set()
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] in temp:
                        return False
                    temp.add(board[j][i])
        return True

    def squarecheck(self, board, m, n):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                temp = set()
                temp_board = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                for each in temp_board:
                    if each != '.':
                        if each in temp:
                            return False
                        temp.add(each)
        return True
