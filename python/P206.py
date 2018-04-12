# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    '''
    def reverseList(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev
    '''
    
    def reverseList(self, head):
        return self.reverseOne(head)
    def reverseOne(self, node, prev = None):
        if not node:
            return prev
        nextnode = node.next
        node.next = prev
        return self.reverseOne(nextnode, node)
        