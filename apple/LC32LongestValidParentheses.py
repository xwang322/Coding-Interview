class Solution(object):
    def longestValidParentheses(self, s):
        if not s:
            return 0
        stack = []
        answer = 0
        flag = -1
        for index, char in enumerate(s):
            if char == '(':
                if flag == -1:
                    stack.append(index)
                else:
                    stack.append(flag)
                    flag = -1
            else:
                if not stack:
                    flag = -1
                else:
                    temp = stack.pop()
                    answer = max(answer, index-temp+1)
                    flag = temp
        return answer
        
