class Solution(object):
    def simplifyPath(self, path):
        if not path:
            return path
        stack = []
        temp = list(path.split('/'))
        for each in temp:
            if each == '.' or not each:
                pass
            elif each == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(each)
        return '/'+'/'.join(stack)
            
                