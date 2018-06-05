# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        inorder = []
        while head:
            inorder.append(head.val)
            head = head.next
        n = len(inorder) 
        return self.convertListToBST(inorder, n)
    
    def convertListToBST(self, inorder, n):
        if not n:
            return 
        root = TreeNode(inorder[n/2])
        if n%2:
            root.left = self.convertListToBST(inorder[:n/2], n/2)
            root.right = self.convertListToBST(inorder[n/2+1:], n/2)
        else:
            root.left = self.convertListToBST(inorder[:n/2], n/2)
            root.right = self.convertListToBST(inorder[n/2+1:], n/2-1)
        return root