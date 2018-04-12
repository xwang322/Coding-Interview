# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        stack = []
        answer = []
        while root or stack:
            if root:
                stack.append(root)
                answer.append(root.val)
                root = root.left
            else:
                root = stack.pop()
                root = root.right
        return answer