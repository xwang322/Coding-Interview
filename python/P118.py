class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            answer = [[1], [1,1]]
            for i in range(2, numRows):
                length = i+1
                temp = [1]*length
                for j in range(1, length-1):
                    temp[j] = answer[i-1][j-1] + answer[i-1][j] 
                temp[length-1] = 1
                answer.append(temp)
            return answer