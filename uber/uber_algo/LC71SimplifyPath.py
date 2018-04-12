class Solution(object):
    def simplifyPath(self, path):
        if not path:
            return '/'
        stack = []
        lists = path.split('/')
        for item in lists:
            if item == '..':
                if stack:
                    stack.pop()
            elif item != '' and item != '.':
                stack.append(item)
        return '/'+'/'.join(stack)
        
