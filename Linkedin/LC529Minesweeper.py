class Solution(object):
    def updateBoard(self, board, click):
        if not board:
            return []
        m = len(board)
        n = len(board[0])
        level = set()
        level.add(tuple(click))
        flag = False
        while level:
            next_level = set()
            while level:
                coord = level.pop()
                row = coord[0]
                col = coord[1]
                if board[row][col] == 'M':
                    board[row][col] = 'X'
                    flag = True
                    break
                elif board[row][col] == 'E':
                    mines = 0
                    if row >= 1 and board[row-1][col] == 'M':
                        mines += 1
                    if row <= m-2 and board[row+1][col] == 'M':
                        mines += 1
                    if col >= 1 and board[row][col-1] == 'M':
                        mines += 1
                    if col <= n-2 and board[row][col+1] == 'M':
                        mines += 1
                    if row >= 1 and col >= 1 and board[row-1][col-1] == 'M':
                        mines += 1
                    if row <= m-2 and col >= 1 and board[row+1][col-1] == 'M':
                        mines += 1
                    if row >= 1 and col <= n-2 and board[row-1][col+1] == 'M':
                        mines += 1
                    if row <= m-2 and col <= n-2 and board[row+1][col+1] == 'M':
                        mines += 1
                    if mines:
                        board[row][col] = str(mines)
                    else:
                        board[row][col] = 'B'
                        if row >= 1 and board[row-1][col] == 'E':
                            next_level.add((row-1, col))
                        if row <= m-2 and board[row+1][col] == 'E':
                            next_level.add((row+1, col))
                        if col >= 1 and board[row][col-1] == 'E':
                            next_level.add((row, col-1))
                        if col <= n-2 and board[row][col+1] == 'E':
                            next_level.add((row, col+1))
                        if row >= 1 and col >= 1 and board[row-1][col-1] == 'E':
                            next_level.add((row-1, col-1))
                        if row <= m-2 and col >= 1 and board[row+1][col-1] == 'E':
                            next_level.add((row+1, col-1))
                        if row >= 1 and col <= n-2 and board[row-1][col+1] == 'E':
                            next_level.add((row-1, col+1))
                        if row <= m-2 and col <= n-2 and board[row+1][col+1] == 'E':
                            next_level.add((row+1, col+1))
                if flag:
                    return board
                else:
                    level = next_level
            return board
