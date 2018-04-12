class Solution(object):
    def isValid(self, s):
        stack = []
        dict = {']':'[','}':'{',')':'('}
        for char in s:
            if char in dict.keys():
                if stack == [] or stack.pop() != dict[char]:
                    return False
            elif char in dict.values():
                stack.append(char)
            else:
                return False
        return stack == []
        