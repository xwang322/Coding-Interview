# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        '''
        # this method is up to bottom which consumes too many times
        if not root:
            return 0
        val = 0
        if root.left:
            val += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            val += self.rob(root.right.left) + self.rob(root.right.right)
        return max(root.val + val, self.rob(root.left)+self.rob(root.right))
        '''
        def superrob(node):
            if not node: return (0, 0)
            left, right = superrob(node.left), superrob(node.right)
            now = node.val + left[1] + right[1]
            later = max(left) + max(right)
            return (now, later)
        return max(superrob(root))
