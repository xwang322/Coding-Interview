# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        # while...else...statement 
        if not head:
            return None
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        else:
            return None
        slow1 = head
        while slow1 != slow:
            slow1 = slow1.next
            slow = slow.next
        return slow
        