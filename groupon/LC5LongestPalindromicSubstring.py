class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ''
        if len(s) == 1:
            return s
        answer = ''
        for i in range(len(s)):
            temp = self.extension(s, i, i)
            if len(temp) > len(answer):
                answer = temp
            temp = self.extension(s, i, i+1)
            if len(temp) > len(answer):
                answer = temp
        return answer

    def extension(self, string, start, end):
        while start >= 0 and end < len(string) and string[start] == string[end]:
            start -= 1
            end += 1
        return string[start+1:end]
