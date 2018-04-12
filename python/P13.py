class Solution(object):
    def romanToInt(self, s):
        if not s:
            return 0
        dictionary = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        answer = 0
        for i in range(len(s)-1):
            if dictionary[s[i]] >= dictionary[s[i+1]]:
                answer += dictionary[s[i]]
            else:
                answer -= dictionary[s[i]]
        answer += dictionary[s[len(s)-1]]
        return answer
        