class Solution(object):
    def titleToNumber(self, s):
        if not s:
            return 0
        answer = 0
        length = len(s)
        for i in range(len(s)):
            answer += (26**(length-i-1)) * (ord(s[i])-ord('A')+1)
        return answer
        