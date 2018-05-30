class Solution(object):
    def countSubstrings(self, s):
        if not s:
            return 0
        answer = 0
        i = 0
        while i < len(s):
            answer += self.countPalin(s, i, i)
            if i < len(s)-1:
                if s[i] == s[i+1]:
                    answer += self.countPalin(s, i, i+1)
            i += 1
        return answer

    def countPalin(self, s, start, end):
        answer = 0
        while start >= 0 and end < len(s) and s[start] == s[end]:
            answer += 1
            start -= 1
            end += 1
        return answer
        
