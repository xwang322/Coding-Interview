class Solution(object):
    def convert(self, s, numRows):
        if not s or len(s) == 1:
            return s
        if numRows == 1:
            return s
        temp_list = ['']*numRows
        j = 0
        sign = 1
        for i in range(len(s)):
            temp_list[j] += s[i]
            j += sign
            if j == numRows:
                j = numRows-2
                sign = -1
            elif j == -1:
                j = 1
                sign = 1
        answer = ''
        for i in range(numRows):
            answer += temp_list[i]
        return answer
                