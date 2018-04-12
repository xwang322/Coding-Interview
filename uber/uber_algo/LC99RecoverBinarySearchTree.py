# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        inorderlist = []
        self.inOrderTranverse(root, inorderlist)
        first = None
        second = None
        temp = float('inf')
        sortedlist = sorted(inorderlist)
        for index in range(len(inorderlist)):
            if inorderlist[index] != sortedlist[index]:
                if first == None:
                    first = inorderlist[index]
                else:
                    second = inorderlist[index]
        self.SwapNode(root, first, temp)
        self.SwapNode(root, second, first)
        self.SwapNode(root, temp, second)

    def inOrderTranverse(self, root, inorderlist):
        if not root:
            return
        self.inOrderTranverse(root.left, inorderlist)
        inorderlist.append(root.val)
        self.inOrderTranverse(root.right, inorderlist)

    def SwapNode(self, root, defaultvalue, changevalue):
        if not root:
            return
        if root.val == defaultvalue:
            root.val = changevalue
            return
        self.SwapNode(root.left, defaultvalue, changevalue)
        self.SwapNode(root.right, defaultvalue, changevalue)
