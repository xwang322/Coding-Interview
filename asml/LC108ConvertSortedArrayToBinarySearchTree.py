# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        length = len(nums)
        root = TreeNode(nums[length/2])
        root.left = self.sortedArrayToBST(nums[:length/2])
        root.right = self.sortedArrayToBST(nums[length/2+1:])
        return root
