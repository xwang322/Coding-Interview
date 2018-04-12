class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        row_up = 0
        row_down = len(matrix)-1
        col_up = 0
        col_down = len(matrix[0])-1
        answer = []
        while row_up <= row_down and col_up <= col_down:
            i = col_up
            while i <= col_down:
                answer.append(matrix[row_up][i])
                i += 1
            row_up += 1
            i = row_up
            while i <= row_down:
                answer.append(matrix[i][col_down])
                i += 1
            col_down -= 1
            if row_up <= row_down:
                i = col_down
                while i >= col_up:
                    answer.append(matrix[row_down][i])
                    i -= 1
                row_down -= 1
            if col_up <= col_down:
                i = row_down
                while i >= row_up:
                    answer.append(matrix[i][col_up])
                    i -= 1
                col_up += 1
        return answer
