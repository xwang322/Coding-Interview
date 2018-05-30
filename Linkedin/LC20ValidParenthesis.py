'''
上午刚结束的电面，1个小时候就给了onsite
/**
* This function determines if the braces ('(' and ')') in a string are properly matched.
* it ignores non-brace characters.
* Some examples:
* "()()()()" -> true
* "((45+)*a3)" -> true
* "(((())())" -> false
*/
'''
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
