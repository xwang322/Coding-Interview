class Solution(object):
    def multiply(self, A, B):
        m1 = len(A)
        n1 = len(A[0])
        n2 = len(B[0])
        answer = [[0 for i in range(n2)] for j in range(m1)]
        for i in range(m1):
            for j in range(n1):
                if A[i][j]:
                    for k in range(n2):
                        answer[i][k] += A[i][j] * B[j][k]
        return answer
                    
