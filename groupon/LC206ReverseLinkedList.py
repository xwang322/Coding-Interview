# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        if not head:
            return None
        prev = None
        while head:
            curr = head
            head = head.next
            # those two lines are not interchangeable because curr and head is referring to the same node
            curr.next = prev
            prev = curr
        return prev
