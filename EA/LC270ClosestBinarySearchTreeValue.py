# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        if not root:
            return float('inf')
        answer = root
        diff = float('inf')
        while root:
            tempdiff = abs(root.val - target)
            if tempdiff < diff:
                answer = root
                diff = tempdiff
            if root.val > target:
                root = root.left
            elif root.val < target:
                root = root.right
            else:
                break
        return answer.val
