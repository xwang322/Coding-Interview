# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        return self.helper(root.left, root.right)

    def helper(self, node1, node2):
        if not node1 and not node2:
            return True
        elif node1 and not node2:
            return False
        elif node2 and not node1:
            return False
        else:
            if node1.val != node2.val:
                return False
            else:
                return self.helper(node1.left, node2.right) and self.helper(node1.right, node2.left)
