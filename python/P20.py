class Solution(object):
    def isValid(self, s):
        if not s or len(s) == 0:
            return True
        if len(s)%2:
            return False
        stack = []
        for each in s:
            if each == '(' or each == '[' or each == '{':
                stack.append(each)
            else:
                if stack:
                    temp = stack.pop()
                    if each == ')' and temp != '(':
                        return False
                    elif each == '}' and temp != '{':
                        return False
                    elif each == ']' and temp != '[':
                        return False
                else:
                    return False
        if stack:
            return False
        else:
            return True
        