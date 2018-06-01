class Solution(object):
    def isValid(self, s):
        if not s:
            return True
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif char == ')' or char == '}' or char == ']':
                if not stack:
                    return False
                elif char == ')':
                    if stack[-1] != '(':
                        return False
                    stack.pop()
                elif char == ']':
                    if stack[-1] != '[':
                        return False
                    stack.pop()
                elif char == '}':
                    if stack[-1] != '{':
                        return False
                    stack.pop()
        if not stack:
            return True
        return False
