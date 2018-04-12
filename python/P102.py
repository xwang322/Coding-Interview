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
        this_level = [root]
        this_level_val = []
        next_level = []
        answer = []
        while this_level:
            while this_level:
                current = this_level.pop(0)
                this_level_val.append(current.val)
                if current.left:
                    next_level.append(current.left)
                if current.right:
                    next_level.append(current.right)
            answer.append(this_level_val)
            this_level_val = []
            this_level = next_level
            next_level = []
        return answer
        