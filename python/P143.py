# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        if not head:
            return None
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        prev = None
        while slow:
            curr = slow
            slow = slow.next
            curr.next = prev
            prev = curr
        head1 = head
        head2 = prev
        while head2.next:
            head1.next, head1 = head2, head1.next
            head2.next, head2 = head1, head2.next
        return 