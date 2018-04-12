class TicTacToe(object):

    def __init__(self, n):
        self.n = n
        self.cols = [0 for i in range(n)]
        self.rows = [0 for i in range(n)]
        self.dig = [0, 0]
        

    def move(self, row, col, player):
        point = (1.5-player)*2
        self.cols[col] += point
        self.rows[row] += point
        if row == col:
            self.dig[0] += point
        if row+col == self.n-1:
            self.dig[1] += point
        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(self.dig[0]) == self.n or abs(self.dig[1]) == self.n:
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
        