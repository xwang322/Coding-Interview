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
        else:
            return self.judge(root.left, root.right)
    
    def judge(self, p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.judge(p.right, q.left) and self.judge(p.left, q.right)
        return False
}