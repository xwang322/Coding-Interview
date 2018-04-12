class Solution(object):
    def setZeroes(self, matrix):
        if not matrix or not matrix[0]:
            return matrix
        rowflag = False
        colflag = False
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if matrix[i][0] == 0:
                rowflag = True
                break
        for i in range(n):
            if matrix[0][i] == 0:
                colflag = True
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
        if rowflag:
            for i in range(m):
                matrix[i][0] = 0
        if colflag:
            for i in range(n):
                matrix[0][i] = 0
