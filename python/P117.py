# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    # bfs
    def connect(self, root):
        if not root:
            return None
        else:
            if root.left and root.right:
                root.left.next = root.right
                temp = root.next
                while temp:
                    if temp.left:
                        root.right.next = temp.left
                        break
                    if temp.right:
                        root.right.next = temp.right
                        break
                    temp = temp.next
            elif root.left and not root.right:
                temp = root.next
                while temp:
                    if temp.left:
                        root.left.next = temp.left
                        break
                    if temp.right:
                        root.left.next = temp.right
                        break
                    temp = temp.next
            elif root.right and not root.left:
                temp = root.next
                while temp:
                    if temp.left:
                        root.right.next = temp.left
                        break
                    if temp.right:
                        root.right.next = temp.right
                        break
                    temp = temp.next
            self.connect(root.right)
            self.connect(root.left)