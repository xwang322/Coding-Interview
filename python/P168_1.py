class Solution(object):
    def convertToTitle(self, n):
        answer = ''
        while n:
            answer = chr(ord('A') +(n-1)%26) + answer  
            # backward going forward for each digit
            n = (n-1)/26
        return answer