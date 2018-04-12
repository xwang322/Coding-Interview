# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        answer = []
        stack = [root]
        while stack:
            temp = stack.pop()
            if temp:
                answer.append(temp.val)
                stack.append(temp.left)
                stack.append(temp.right)
        return answer[::-1]
