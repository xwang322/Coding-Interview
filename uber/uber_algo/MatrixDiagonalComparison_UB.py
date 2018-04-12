/*
* 是给定一个n*m 的matrix，然后判断是否diagonal是相同的，然后refactor了一下下，
* 最后有一个followup，答得不是很好TT，貌似是如果matrix很大，如何modify你的function使其对elements的access次数减少。
**/

def JudgeDiagonal(matrix):
    if not matrix or not matrix[0]:
        return False
    m = len(matrix)
    n = len(matrix[0])
    if m == 1 or n == 1:
        return False
    temp = []
    for i in range(m):
        if temp and temp[-1][:-1] != matrix[i][1:]:
            return False
        temp.append(matrix[i])
    return True

answer = JudgeDiagonal([[1,2,3,4], [5,1,2,3], [6,5,1,2], [7,6,5,1]])
print answer
