/*
* Given an integer matrix that is sorted ascending in each row and each column write an algorithm that find an integer X or returns false.
**/
def searchMatrix(self, matrix, target):
    if matrix == [] or matrix == [[]]:
        return False
    i = 0; j = len(matrix[0])-1
    while i < len(matrix) and j >= 0:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            j -= 1
        else:
            i += 1
    return False
