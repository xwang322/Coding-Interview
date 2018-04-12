/*
* 刚结束的电面 妥妥跪一个烙印
* 上来寒暄两句开始做题 是利口原题尔尔丝 但是之前没看过也没做过 而且他把数字变成了两位数
* 题目：
* # input -> "23+(34*4-(5*6))+4-5"
* # output -> 128
**/
class Solution(object):
    def calculate(self, s):
        answer = 0
        stack = []
        sign = 1
        i = 0
        while i <= len(s)-1:
            if s[i].isdigit():
                num = ord(s[i])-ord('0')
                while i+1 <= len(s)-1 and s[i+1].isdigit():
                    num = num*10+ord(s[i+1])-ord('0')
                    i += 1
                answer += sign*num
            elif s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i] == '(':
                stack.append(answer)
                stack.append(sign)
                answer = 0
                sign = 1
            elif s[i] == ')':
                answer = answer*stack.pop()+stack.pop()
            i += 1
        return answer
