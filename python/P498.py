class Solution(object):
    def findDiagonalOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        if m == 1:
            return matrix[0]
        if n == 1:
            return [matrix[i][0] for i in range(m)]
        answer = []
        visited = [[False for i in range(n)] for j in range(m)]
        self.traverse(0, 0, matrix, answer, m, n, False, visited)
        return answer
    
    def traverse(self, i, j, matrix, answer, m, n, direction, visited):
        if not any(False in sublist for sublist in visited):
            return answer
        if i == 0 and j == 0:
            answer.append(matrix[i][j])
            visited[i][j] = True
            j += 1
        if not direction:
            while 0 <=i <=m-1 and 0 <=j <=n-1 and not visited[i][j]:
                answer.append(matrix[i][j])
                visited[i][j] = True
                j -= 1
                i += 1
            if j<0 and 0 <=i <=m-1:
                self.traverse(i, j+1, matrix, answer, m, n, not direction, visited)
            elif i==m:
                self.traverse(i-1, j+2, matrix, answer, m, n, not direction, visited)
        if direction:
            while 0 <=i <=m-1 and 0 <=j <=n-1 and not visited[i][j]:
                answer.append(matrix[i][j])
                visited[i][j] = True
                j += 1
                i -= 1
            if i<0 and 0 <=j <=n-1:
                self.traverse(0, j, matrix, answer, m, n, not direction, visited)
            elif j==n:
                self.traverse(i+2, j-1, matrix, answer, m, n, not direction, visited)