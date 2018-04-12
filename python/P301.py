class Solution(object):
    # bfs
    def removeInvalidParentheses(self, s):
        answer = []
        curr_list = [s]
        visited = set([s])
        done = False
        while curr_list:
            test = curr_list.pop(0)
            if self.isValid(test):
                done = True
                answer.append(test)
            if done:
                continue
            for i in range(len(test)):
                if test[i] != '(' and test[i] != ')':
                    continue
                sep = test[:i] + test[i+1:]
                if sep not in visited:
                    curr_list.append(sep)
                    visited.add(sep)
        return answer
        
        
    def isValid(self, s):
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
            if count < 0:
                return False
        else:
            return count == 0