class Solution(object):
    def setZeroes(self, matrix):
        if not matrix or not matrix[0]:
            return
        flag1 = False
        flag2 = False
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if not matrix[i][0]:
                flag1 = True
                break
        for i in range(n):
            if not matrix[0][i]:
                flag2 = True
                break
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        for i in range(1, n):
            if matrix[0][i] == 0:
                for j in range(m):
                    matrix[j][i] = 0
        if flag1:
            for i in range(m):
                matrix[i][0] = 0
        if flag2:
            for i in range(n):
                matrix[0][i] = 0

        
