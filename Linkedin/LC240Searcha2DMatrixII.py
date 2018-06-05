class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        i = 0
        j = len(matrix[0])-1
        pivot = matrix[i][j]
        m = len(matrix)
        n = len(matrix[0])
        while i < m and j >= 0:
            if target == pivot:
                return True
            elif target > pivot:
                if i+1 == m:
                    return False
                pivot = matrix[i+1][j]
                i += 1
            else:
                if j == 0:
                    return False
                pivot = matrix[i][j-1]
                j -= 1
