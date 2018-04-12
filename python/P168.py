class Solution(object):
    def convertToTitle(self, n):
        answer = ''
        while n:
            n, temp = divmod(n-1, 26)
            answer = chr(temp+65)+answer
        return answer
            