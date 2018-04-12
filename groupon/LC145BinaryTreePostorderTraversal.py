# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        if not root:
            return []
        answer = []
        if root.left:
            answer += self.postorderTraversal(root.left)
        if root.right:
            answer += self.postorderTraversal(root.right)
        answer += [root.val]
        return answer
