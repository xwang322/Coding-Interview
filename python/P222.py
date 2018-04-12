# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def finddepth(self, root):
        if not root:
            return 0
        else:
            depth = 0
            root = root.right
            while root:
                depth += 1
                root = root.left
            return depth
    
    
    def countNodes(self, root):
        if not root:
            return 0
        depth = 1
        temp = root
        while temp.left:
            depth += 1
            temp = temp.left
            
        rest = 0
        cur_root = root
        cur_dep = 1
        while cur_dep < depth:
            dd = self.finddepth(cur_root)
            if dd+cur_dep == depth:
                cur_root = cur_root.right
                rest += 2**(dd-1)
                cur_dep += 1
            else:
                cur_root = cur_root.left
                cur_dep += 1
        return 2**(depth-1) + rest