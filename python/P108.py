# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        root = TreeNode(nums[len(nums)/2])
        root.left = self.sortedArrayToBST(nums[:len(nums)/2])
        root.right = self.sortedArrayToBST(nums[len(nums)/2+1:])
        return root