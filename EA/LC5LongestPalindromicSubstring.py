class Solution(object):
    def longestPalindrome(self, s):
        if len(s) == 1: return s
        answer = ''
        length = 0
        for i in range(len(s)):
            temp = self.findlongest(s, i, i)
            if len(temp) > length:
                answer = temp
                length = len(temp)
            if i < len(s)-1:
                if s[i] == s[i+1]:
                    temp1 = self.findlongest(s, i, i+1)
                    if len(temp1) > length:
                        answer = temp1
                        length = len(temp1)
        return answer

    def findlongest(self, string, start, end):
        while start >= 0 and end <= len(string)-1 and string[start] == string[end]:
            start -= 1
            end += 1
        return string[start+1:end]
