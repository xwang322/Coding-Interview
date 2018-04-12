class Solution(object):
    def romanToInt(self, s):
        pair = {'IV':4, 'IX':9, 'XL': 40, 'XC':90, 'CD':400, 'CM':900}
        initial = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        length = len(s)
        answer = 0
        char_list = list(s)
        number_list = [0] * len(s)
        for i in range(len(s)):
            number_list[i] = initial[s[i]]
        for i in range(len(s)-1):
            if number_list[i] < number_list[i+1]:
                answer -= number_list[i]
            else:
                answer += number_list[i]
        return answer+number_list[-1]