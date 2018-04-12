/*
* 面的是 诶踢寄 组， 实现计算器， 没有括号， 只有加减乘除，可能结果有小数， 需要跑test
**/
class Solution(object):
    def calculate(self, s):
        if not s:
            return 0
        sign = '+'
        stack = []
        i = 0
        num = 0
        while i <= len(s)-1:
            if s[i].isdigit():
                num = ord(s[i])-ord('0')
                while i+1<=len(s)-1 and s[i+1].isdigit():
                    num = num*10+ord(s[i+1])-ord('0')
                    i += 1
            if (s[i] != ' ' and not s[i].isdigit()) or i == len(s)-1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                elif sign == '/':
                    if stack[-1]%num != 0:
                        if stack[-1]/num < 0:
                            stack.append(stack.pop()/num+1)
                        else:
                            stack.append(stack.pop()/num)
                    else:
                        stack.append(stack.pop()/num)
                sign = s[i]
                num = 0
            i += 1
        print stack
        return sum(stack)
