class Solution(object):
    def isValid(self, s):
        if not s:
            return True
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif stack and (char == ')' or char == '}' or char == ']'):
                if char == ')':
                    if stack[-1] != '(':
                        return False
                    else:
                        stack.pop()
                if char == ']':
                    if stack[-1] != '[':
                        return False
                    else:
                        stack.pop()
                if char == '}':
                    if stack[-1] != '{':
                        return False
                    else:
                        stack.pop()
            else:
                return False
        return not stack
