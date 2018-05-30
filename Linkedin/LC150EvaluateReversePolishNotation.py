class Solution(object):
    def evalRPN(self, tokens):
        if not tokens:
            return 0
        stack = []
        signs = ['+','-','*','/']
        for token in tokens:
            if token not in signs:
                stack.append(int(token))
            else:
                temp1 = stack.pop()
                temp2 = stack.pop()
                if token == '+':
                    stack.append(temp2 + temp1)
                elif token == '-':
                    stack.append(temp2 - temp1)
                elif token == '*':
                    stack.append(temp2 * temp1)
                elif token == '/':
                    if temp2%temp1 != 0 and temp2*temp1 < 0:
                        stack.append(temp2 / temp1 + 1)
                    else:
                        stack.append(temp2 / temp1)
        return stack.pop()


'''
followup 哪些地方应该handle exception。答了number和operator数对不上，还有number不valid，operator不valid的情况。
之后按照要求写了try throw和catch。
'''
class Error(Exception):
    pass

class Mismatch(Error):
    pass

class NotValidNumber(Error):
    pass

class NotValidOperator(Error):
    pass

def evalRPN(self, tokens):
    if not tokens:
        return 0
    stack = []
    signs = ['+','-','*','/']
    for token in tokens:
        if token not in signs:
            try:
                if token.isdigit() == False:
                    raise NotValidNumber
            except:
                print 'This input is not a valid number'
            stack.append(int(token))
        else:
            temp1 = stack.pop()
            temp2 = stack.pop()
            if token == '+':
                stack.append(temp2 + temp1)
            elif token == '-':
                stack.append(temp2 - temp1)
            elif token == '*':
                stack.append(temp2 * temp1)
            elif token == '/':
                if temp2%temp1 != 0 and temp2*temp1 < 0:
                    stack.append(temp2 / temp1 + 1)
                else:
                    stack.append(temp2 / temp1)
    try:
        if len(stack) != 1:
            raise Mismatch
    except Mismatch:
        print 'Number and Operators are not match'
    return stack.pop()
