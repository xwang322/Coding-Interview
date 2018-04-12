class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        if n == 0:
            return 1
        temp = [9,9,8,7,6,5,4,3,2,1]
        answer = 0
        for i in range(n):
            tmp = 1
            j = 0
            while j < i+1:
                tmp *= temp[j]
                j += 1
            answer += tmp
        return answer+1