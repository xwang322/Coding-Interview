# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        answer = []
        queue = [root]
        this_level = []
        next_level = []
        while queue:
            while queue:
                node = queue.pop(0)
                this_level.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            answer.append(this_level)
            queue = next_level
            next_level = []
            this_level = []
        return answer
