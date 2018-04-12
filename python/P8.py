class Solution(object):
    def myAtoi(self, str):
        if not str:
            return 0
        temp = str.strip()
        sign = 0
        if temp[0] == '+' or temp[0] == '-':
            sign = temp[0]
            tmp = temp[1:]
        else:
            tmp = temp
        answer = 0
        for char in tmp:
            if char.isdigit():
                answer = answer*10+int(char)
            else:
                break
        if sign == '-':
            if answer > 2147483648:
                return -2147483648
            else:
                return -answer
        elif sign == '+':
            if answer > 2147483647:
                return 2147483647
            else:
                return answer
        else:
            if answer >= 2147483648:
                return 2147483647
            else:
                return answer
        