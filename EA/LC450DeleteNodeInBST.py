# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        if not root:
            return root
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            temp = root.right
            tempval = temp.val
            while temp.left:
                temp = temp.left
                tempval = temp.val
            root.val = tempval
            root.right = self.deleteNode(root.right, tempval)
        return root

        
