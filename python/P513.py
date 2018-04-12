# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        curr_list = [root]
        for each in curr_list:
            curr_list += filter(None, (each.right, each.left))
        return curr_list[-1].val