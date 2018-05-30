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
        queue = []
        answer = []
        next_level = []
        queue.append(root)
        temp = []
        while queue:
            while queue:
                node = queue.pop(0)
                temp.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            queue = next_level
            next_level = []
            answer.append(temp)
            temp = []
        return answer
