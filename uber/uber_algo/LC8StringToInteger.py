class Solution(object):
    def myAtoi(self, string):
        templist = list(string.strip())
        sign = 1
        if len(templist) == 0:
            return 0
        if templist[0] == '+':
            templist.pop(0)
        elif templist[0] == '-':
            sign = -1
            templist.pop(0)
        answer = 0
        i = 0
        while i <= len(templist)-1:
            if '0' <= templist[i] <= '9':
                answer = answer*10 + ord(templist[i])-ord('0')
                i += 1
            else:
                break
        if sign*answer > 2147483647:
            return 2147483647
        elif sign*answer < -2147483648:
            return -2147483648
        else:
            return sign*answer