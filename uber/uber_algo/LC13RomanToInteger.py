class Solution(object):
    def romanToInt(self, s):
        dictionary = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        if not s:
            return 0
        i = 0
        answer = 0
        while i <= len(s)-1:
            if i <= len(s)-2:
                if dictionary[s[i]] >= dictionary[s[i+1]]:
                    answer += dictionary[s[i]]
                    i += 1
                else:
                    answer += dictionary[s[i+1]] - dictionary[s[i]]
                    i += 2
            else:
                answer += dictionary[s[i]]
                i += 1
        return answer