class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        pivot = matrix[0][-1]
        if pivot == target:
            return True
        i = 0
        j = n-1
        while pivot != target:
            if target > pivot:
                if i+1 == m:
                    return False
                pivot = matrix[i+1][j]
                i += 1
            else:
                if j == 0:
                    return False
                pivot = matrix[i][j-1]
                j -= 1
        return True