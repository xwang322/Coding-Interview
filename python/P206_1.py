# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        #iterative
        dummy = ListNode(0)
        while head:
            temp = head.next
            head.next = dummy.next
            dummy.next = head
            head = temp
        return dummy.next