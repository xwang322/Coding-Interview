class Solution(object):
    def isToeplitzMatrix(self, matrix):
        if not matrix or not matrix[0]:
            return False
        temp = matrix[0]
        for i in range(1, len(matrix)):
            if temp[:-1] != matrix[i][1:]:
                return False
            temp = matrix[i]
        return True
        
