# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        '''BFS
        if not root:
            return []
        this_level = [root]
        next_level = []
        answer = []
        this_value = []
        while this_level:
            while this_level:
                element = this_level.pop(0)
                this_value.append(element.val)
                if element.left:
                    next_level.append(element.left)
                if element.right:
                    next_level.append(element.right)
            answer.append(this_value)
            this_level = next_level
            next_level = []
            this_value = []
        final = []
        for each in answer:
            final.append(each[-1])
        return final
        '''
        # DFS
        if not root:
            return []
        answer = []
        self.dfs(root, answer, 0)
        return answer
    
    def dfs(self, node, answer, length):
        if node:
            if length == len(answer):
                answer.append(node.val)
            self.dfs(node.right, answer, length+1)
            self.dfs(node.left, answer, length+1)