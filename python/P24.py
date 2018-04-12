# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        if not head:
            return head
        if not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        new_head = head.next
        while dummy.next and dummy.next.next:
            slow = dummy.next
            fast = dummy.next.next
            slow.next = fast.next
            fast.next = slow
            dummy.next = fast
            dummy = dummy.next.next
        return new_head
        