class Solution(object):
    def multiply(self, A, B):
        m1 = len(A)
        n1 = len(A[0])
        m2 = len(B)
        n2 = len(B[0])
        tempA = []
        tempB = []
        for i in range(m1):
            temp = []
            for j in range(n1):
                if A[i][j] != 0:
                    temp.append(j)
            tempA.append(temp)
        for i in range(n2):
            temp = []
            for j in range(m2):
                if B[j][i] != 0:
                    temp.append(j)
            tempB.append(temp)
        answer = [[0 for i in range(len(tempB))] for j in range(len(tempA))]
        for i in range(len(tempA)):
            for j in range(len(tempB)):
                temp1 = tempA[i]
                temp2 = tempB[j]
                if not temp1 or not temp2:
                    answer[i][j] = 0
                else:
                    common = list(set(temp1).intersection(temp2))
                    for each in common:
                        answer[i][j] += A[i][each]*B[each][j]
        return answer
        
        