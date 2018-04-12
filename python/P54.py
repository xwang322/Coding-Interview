class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        answer = []
        m, n = len(matrix), len(matrix[0])
        up, down, left, right = 0, m-1, 0, n-1
        while left<right and up<down:
            answer.extend(matrix[up][j] for j in range(left, right))
            answer.extend(matrix[i][right] for i in range(up, down))
            answer.extend(matrix[down][j] for j in range(right, left, -1))
            answer.extend(matrix[i][left] for i in range(down, up, -1))
            up, down, left, right = up+1, down-1, left+1, right-1
        if left == right:
            answer.extend(matrix[i][left] for i in range(up, down+1))
        elif up == down:
            answer.extend(matrix[up][j] for j in range(left, right+1))
        return answer