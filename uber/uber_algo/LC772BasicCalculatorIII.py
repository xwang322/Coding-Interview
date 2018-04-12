import re
class Solution(object):
    def calculate(self, s):
        op_stack = []
        num_stack = []
        level = {'+':1, '-':1, '*':2, '/':2, '(':0, ')':0}
        for i in re.compile('\d+|[()+-/\*]').findall(s):
            if i in level:
                if len(op_stack) == 0 or i == '(' or level[i] > level[op_stack[-1]]:
                    op_stack.append(i)
                elif i == ')':
                    while op_stack[-1] != '(':
                        num_stack.append(self.cal(num_stack.pop(), num_stack.pop(), op_stack.pop()))
                    op_stack.pop()
                elif level[i] <= level[op_stack[-1]]:
                    num_stack.append(self.cal(num_stack.pop(), num_stack.pop(), op_stack.pop()))
                    op_stack.append(i)
            else:
                num_stack.append(int(i))
        while len(op_stack) != 0:
            num_stack.append(self.cal(num_stack.pop(), num_stack.pop(), op_stack.pop()))
        return num_stack[0]

    def cal(self, num1, num2, operator):
        if operator == '+':
            return num2+num1
        elif operator == '-':
            return num2-num1
        elif operator == '*':
            return num2*num1
        elif operator == '/':
            return num2//num1





                
