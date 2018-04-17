class Solution(object):
    def generateMatrix(self, n):
        if not n:
            return []
        answer = [[0 for i in range(n)] for j in range(n)]
        row_up = 0
        row_down = n-1
        col_up = 0
        col_down = n-1
        count = 1
        while row_up <= row_down and col_up <= col_down:
            for i in range(col_up, col_down+1):
                answer[row_up][i] = count
                count += 1
            row_up += 1
            for i in range(row_up, row_down+1):
                answer[i][col_down] = count
                count += 1
            col_down -= 1
            if row_up <= row_down:
                for i in range(col_down, col_up-1, -1):
                    answer[row_down][i] = count
                    count += 1
                row_down -= 1
            if col_up <= col_down:
                for i in range(row_down, row_up-1, -1):
                    answer[i][col_up] = count
                    count += 1
                col_up += 1
        return answer

        
