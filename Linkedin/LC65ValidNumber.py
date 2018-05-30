class Solution(object):
    def isNumber(self, s):
        if not s:
            return False
        i = 0
        n = len(s)
        while i < n and s[i] == ' ':
             i += 1
        sign = 1
        if i < n and s[i] == '+':
            i += 1
        elif i < n and s[i] == '-':
            sign = -1
            i += 1
        number = False
        while i < n and s[i].isdigit():
            number = True
            i += 1
        if i < n and s[i] == '.':
            i += 1
        while i < n and s[i].isdigit():
            number = True
            i += 1
        if number and i < n and s[i] == 'e':
            i += 1
            number = False
            if i < n and (s[i] == '+' or s[i] == '-'):
                i += 1
            while i < n and s[i].isdigit():
                number = True
                i += 1
        while i < n and s[i] == ' ':
            i += 1
        return number and i == n
        
