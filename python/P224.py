class Solution(object):
    def calculate(self, s):
        answer = 0
        temp = 0
        sign = 1
        stack = []
        for char in s:
            if char.isdigit():
                temp = 10*temp+int(char)
            elif char == '+' or char == '-':
                if char == '+':
                    answer += sign*temp
                    temp = 0
                    sign = 1
                else:
                    answer += sign*temp
                    temp = 0
                    sign = -1
            elif char == '(':
                stack.append(answer)
                stack.append(sign)
                sign = 1
                answer = 0
            elif char == ')':
                answer += sign*temp
                answer *= stack.pop()
                answer += stack.pop()
                temp = 0
        return answer + temp*sign