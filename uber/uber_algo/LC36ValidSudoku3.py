class Solution(object):
    def isValidSudoku(self, board):
        if not board or not board[0]:
            return False
        return self.rowcheck(board) and self.colcheck(board) and self.digcheck(board)

    def rowcheck(self, board):
        for i in range(9):
            temp = set()
            for j in range(9):
                if board[i][j] in temp:
                    return False
                elif board[i][j] not in temp and board[i][j] != '.':
                    temp.add(board[i][j])
        return True

    def colcheck(self, board):
        for i in range(9):
            temp = set()
            for j in range(9):
                if board[j][i] in temp:
                    return False
                elif board[j][i] not in temp and board[j][i] != '.':
                    temp.add(board[j][i])
        return True

    def digcheck(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                temp = set()
                candidates = [board[m][n] for m in range(i, i+3) for n in range(j, j+3)]
                for candidate in candidates:
                    if candidate in temp:
                        return False
                    elif candidate != '.':
                        temp.add(candidate)
        return True
