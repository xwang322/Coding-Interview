class Solution(object):
    def rotate(self, matrix):
        if not matrix or not matrix[0]:
            return
        m = len(matrix)
        n = len(matrix[0])
        if m != n:
            return
        for i in range(m):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(m):
            for j in range(m/2):
                matrix[i][j], matrix[i][m-1-j] = matrix[i][m-1-j], matrix[i][j]
        return
        
